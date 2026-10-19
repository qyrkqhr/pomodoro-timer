# -*- coding: utf-8 -*-
import json, base64, time, datetime, urllib.request, urllib.parse, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
START = time.time()
OUT  = f"43.198.164.35_聊天记录全量_{TS}.md"
PAGE = 100

def log(m, out=False):
    print(m, file=sys.stderr if not out else sys.stdout, flush=True)

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

def take_uid(it):
    if isinstance(it, dict):
        for k in ("uid","user_id"):
            if it.get(k) is not None: return it[k]
    elif isinstance(it,(str,int)): return it
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
    walk(obj); return out

def fetch_msgs(channel_id, ctype, limit=100, on_batch=None):
    msgs, cursor, guard = [], 0, 0
    while guard < 300:
        q = urllib.parse.urlencode({"channel_id":channel_id,"channel_type":ctype,
                                   "limit":limit,"last_message_seq":cursor})
        try: d = req("/api/messages?" + q)
        except Exception as e:
            log(f"    [!] messages 失败 cid={channel_id} cur={cursor}: {e}"); break
        arr = d.get("data") if isinstance(d, dict) else d
        if not isinstance(arr, list) or not arr: break
        msgs += arr
        if on_batch: on_batch(arr)          # 每抓到一批就实时落盘
        mx = (arr[-1].get("seq") if isinstance(arr[-1],dict) else None)
        mx = mx or ((d or {}).get("max_message_seq") if isinstance(d,dict) else None) or cursor
        if mx == cursor or len(arr) < limit: break
        cursor = mx; guard += 1
    return msgs

def b64_to_text(v):
    if isinstance(v,(dict,list)): return v
    if not isinstance(v,str): return str(v)
    try:
        dec = base64.b64decode(v, validate=False).decode("utf-8","replace")
        o = json.loads(dec)
        if isinstance(o, dict):
            for k in ("content","text","msg","body"):
                if o.get(k) is not None: return o[k]
            return dec
        return dec
    except Exception: return v

def norm(m):
    if not isinstance(m,dict): return {"time":"-","who":"-","content":b64_to_text(m)}
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

# ---------- 1) 全量 uid ----------
uids, seen = [], set()
def fetch_uids():
    off, lim = 0, 200
    while True:
        try: d = req("/api/connz?" + urllib.parse.urlencode({"offset":off,"limit":lim}))
        except Exception as e: log(f"[!] connz 失败 off={off}: {e}"); break
        arr = d.get("connections") if isinstance(d,dict) else d
        if not isinstance(arr, list): arr = []
        for it in arr:
            u = take_uid(it)
            if u not in seen: seen.add(u); uids.append(u)
        total = d.get("total") if isinstance(d, dict) else len(arr)
        off += len(arr)
        if not arr or (total and off >= total): break
fetch_uids()
TOTAL_U = len(uids)
log(f"[+] uid 总数 {TOTAL_U}")

# ---------- 2) 流式落盘（边抓边写） ----------
fp = open(OUT, "w", encoding="utf-8")
def W(*s):
    for x in s: fp.write(x + "\n")
def FL(): fp.flush()

W("# 43.198.164.35:5300 未授权聊天记录全量导出")
W("")
W(f"- 目标: `{BASE}`")
W(f"- 开始时间: {datetime.datetime.now().isoformat(timespec='seconds')}")
W(f"- uid 总数: **{TOTAL_U}**")
W("")
W("> channel_type: 1=私聊, 2=群聊；正文已 base64 解码")
W("")
FL()

P = G = M = err = 0
total_msg_counter = [0]
for idx, uid in enumerate(uids, 1):
    # ===== 实时进度 =====
    elapsed = time.time() - START
    rate = idx / elapsed if elapsed else 0
    eta = (TOTAL_U - idx) / rate if rate else 0
    log(f"[{idx}/{TOTAL_U}] uid={uid}  已存会话 {G} 消息 {M}  已用时 {elapsed/60:.1f}m  预计剩余 {eta/60:.1f}m")

    try:
        cv = req(f"/api/conversations?uid={uid}")
    except Exception as e:
        err += 1
        W(f"## uid: `{uid}`", f"> ⚠️ 拉取失败: {e}", ""); FL()
        continue

    chans = [c for c in find(cv,"channel_id") if c.get("channel_type") in (1,2)]
    if not chans:
        W(f"## uid: `{uid}`", "- (无会话)", ""); FL(); continue

    W(f"## uid: `{uid}`", ""); FL()
    for c in sorted(chans, key=lambda x:-int(x.get("timestamp") or 0)):
        ctype, cid = c["channel_type"], c["channel_id"]
        kind = "私聊" if ctype==1 else "群聊"
        G += 1
        if ctype==2: P += 1
        W(f"### {kind} · `{cid}`")
        if ctype==2:
            try:
                ch = req(f"/api/channels?channel_id={cid}&channel_type=2")
                ids = sorted({u for u in (take_uid(x) for x in (ch if isinstance(ch,list) else find(ch,"uid"))) if u})
                if not ids and isinstance(ch,dict):
                    ids = sorted({u for u in (take_uid(x) for x in ch.values()) if u})
                if ids: W(f"- 成员({len(ids)}): {', '.join(map(str,ids))}"); 
            except Exception: pass

        # 实时写消息：每批抓到就写
        def on_batch(arr):
            for m in arr:
                n = norm(m)
                W(f"- `{n['time']}` **{n['who']}**: {n['content']}")
            total_msg_counter[0] += len(arr)
            FL()

        try:
            got = fetch_msgs(cid, ctype, on_batch=on_batch)
        except Exception as e:
            log(f"[!] cid={cid} 异常: {e}"); err += 1; got = []
        M += len(got)
        W("")
    W("")
    FL()   # 每个 uid 结束都落盘一次，中断不丢

W("---")
W(f"**统计: {TOTAL_U} uid / 私聊会话 {P} / 全部会话 {G} / 消息 {M} / 失败 {err}**")
W(f"**完成于: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}  总耗时 {(time.time()-START)/60:.1f} min**")
FL(); fp.close()

log(f"\n[+] 完成: 会话 {G}, 消息 {M}, 失败 {err}")
log(f"[+] 已保存到: {OUT}")
