import json, urllib.request, urllib.error, urllib.parse

BASE = "http://43.198.164.35:5300"

def req(path, method="GET", body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(BASE + path, data=data,
        headers={"Content-Type": "application/json"} if data else {})
    try:
        with urllib.request.urlopen(r, timeout=20) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:
        return -1, str(e)

# ---- 拿一个真实 channel_id / uid / last_msg_seq ----
st, body = req("/api/connz"); top = json.loads(body)
conn = top["connections"][0]; uid = conn["uid"]
st, body = req(f"/api/conversations?uid={uid}"); cv = json.loads(body)
def find(o, key, out=None):
    if out is None: out = []
    if isinstance(o, list):
        for x in o: find(x, key, out)
    elif isinstance(o, dict):
        if o.get(key) is not None: out.append(o)
        else:
            for v in o.values(): find(v, key, out)
    return out
c = find(cv, "channel_id")[0]
cid, lseq = c["channel_id"], c.get("last_msg_seq")
print(f"cid={cid}\nuid={uid}\nlast_msg_seq={lseq}\nlast_client_msg_no={c.get('last_client_msg_no')}\nversion={c.get('version')}\n")

def look(raw):
    """判断这条响应里是否像真含消息体"""
    low = raw.lower()
    return any(k in low for k in ('"content"','"body"','"text"','"sender"','"nickname"','"msg"','"from_user"'))

# ============ 1) 路径撒网：200 的都打完整原始 JSON ============
print("========== 1) PATH 撒网 ==========")
paths = [
    f"/api/messages?channel_id={cid}&uid={uid}",
    f"/api/messages?channel_id={cid}",
    f"/api/history?channel_id={cid}&uid={uid}",
    f"/api/historymsg?channel_id={cid}&uid={uid}",
    f"/api/history/message?channel_id={cid}&uid={uid}",
    f"/api/historymsglist?channel_id={cid}&uid={uid}",
    f"/api/msglist?channel_id={cid}&uid={uid}",
    f"/api/messagelist?channel_id={cid}&uid={uid}",
    f"/api/fetchmsg?channel_id={cid}&uid={uid}",
    f"/api/pullmsg?channel_id={cid}&uid={uid}",
    f"/api/sync?channel_id={cid}&uid={uid}",
    f"/api/chatmsg?channel_id={cid}&uid={uid}",
    f"/api/chats/{cid}/messages?uid={uid}",
    f"/api/channels/{cid}/messages?uid={uid}",
    f"/api/conversations/{cid}/messages?uid={uid}",
    f"/api/conversations/{cid}?uid={uid}",
    f"/api/messages/{cid}?uid={uid}",
    f"/api/message?channel_id={cid}&uid={uid}",
]
for p in paths:
    st, body = req(p)
    tag = "HIT👉" if (st == 200 and look(body)) else f"[{st}]"
    if st == 200:
        print(f"\n{tag} {p}\n{body[:700]}")
    elif st in (404, 405, -1):
        print(f"  {tag} {p}")
    else:
        print(f"  {tag} {p}\n  {body[:200]}")

# ============ 2) /api/messages 参数矩阵：全打原始 JSON ============
print("\n========== 2) /api/messages 参数矩阵 ==========")
matrix = [
    f"?channel_id={cid}&uid={uid}&limit=20",
    f"?channel_id={cid}&uid={uid}&start_message_seq=0&max_message_seq={lseq}",
    f"?channel_id={cid}&uid={uid}&seq=0&limit=20",
    f"?channel_id={cid}&uid={uid}&seq={lseq}&limit=20",
    f"?channel_id={cid}&uid={uid}&offset=0&limit=20",
    f"?channel_id={cid}&uid={uid}&offset_msg_seq=0&limit=20",
    f"?channel_id={cid}&uid={uid}&from=0&to={lseq}",
    f"?channel_id={cid}&uid={uid}&before={lseq}&limit=20",
    f"?channel_id={cid}&uid={uid}&client_msg_no={c.get('last_client_msg_no')}&limit=20",
    f"?channel_id={cid}&uid={uid}&version={c.get('version')}&limit=20",
]
for q in matrix:
    st, body = req("/api/messages" + q)
    tag = "HIT👉" if (st==200 and look(body)) else f"[{st}]"
    print(f"\n{tag} /api/messages{q}\n{body[:500]}")

# ============ 3) POST 矩阵：全打原始 JSON ============
print("\n========== 3) POST /api/messages ==========")
bodies = [
    {"channel_id": cid, "uid": uid, "limit": 20},
    {"channel_id": cid, "uid": uid, "start_message_seq": 0, "max_message_seq": lseq, "limit": 20},
    {"channel_id": cid, "uid": uid, "seq": 0, "limit": 20},
    {"channel_id": cid, "uid": uid, "offset": 0, "limit": 20},
    {"cid": cid, "uid": uid, "limit": 20},
]
for b in bodies:
    st, body = req("/api/messages", "POST", b)
    tag = "HIT👉" if (st==200 and look(body)) else f"[{st}]"
    print(f"\n{tag} POST {json.dumps(b)}\n{body[:500]}")

print("\n[DONE]")
