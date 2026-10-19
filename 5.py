import json, urllib.request
BASE = "http://43.198.164.35:5300"

def get(p):
    try:
        with urllib.request.urlopen(BASE + p, timeout=20) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"__err__": str(e)}

# 先拿一个真实 channel_id
top = get("/api/connz")
conn = top["connections"][0]
uid = conn["uid"]
convs = get(f"/api/conversations?uid={uid}")
# 从 conversations 里抠出第一个 channel_id
def find(o, key, out=None):
    if out is None: out = []
    if isinstance(o, list):
        for x in o: find(x, key, out)
    elif isinstance(o, dict):
        if o.get(key) is not None: out.append(o[key])
        else:
            for v in o.values(): find(v, key, out)
    return out

cids = find(convs, "channel_id")
cid = cids[0]
print("test channel_id =", cid, " uid =", uid, flush=True)

# 探针:逐个试消息接口
candidates = [
    f"/api/messages?channel_id={cid}",
    f"/api/messages?uid={uid}&channel_id={cid}",
    f"/api/msgs?channel_id={cid}",
    f"/api/chats/{cid}",
    f"/api/chats?channel_id={cid}",
    f"/api/conversations/{cid}/messages",
    f"/api/conversations/messages?channel_id={cid}",
    f"/api/message/list?channel_id={cid}&limit=50",
    f"/api/getmsg?channel_id={cid}",
]
for p in candidates:
    r = get(p)
    s = json.dumps(r, ensure_ascii=False)
    looks_like_msgs = ("content" in s.lower()) or ("msg" in s.lower() and "seq" in s.lower()) or ("body" in s.lower())
    print("\n=== " + p)
    print("HIT?" , looks_like_msgs)
    print(s[:400])
