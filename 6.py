import json, urllib.request
BASE = "http://43.198.164.35:5300"

def req(path, method="GET", body=None):
    data = json.dumps(body).encode() if body else None
    r = urllib.request.Request(BASE + path, data=data,
                               headers={"Content-Type": "application/json"} if data else {})
    try:
        with urllib.request.urlopen(r, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"__err__": str(e)}

# ---- 拿一个真实 channel_id 和它的 last_msg_seq ----
top = get_top = None
with urllib.request.urlopen(BASE + "/api/connz", timeout=20) as resp:
    top = json.loads(resp.read().decode())
conn = top["connections"][0]
uid  = conn["uid"]
with urllib.request.urlopen(BASE + f"/api/conversations?uid={uid}", timeout=20) as resp:
    cv  = json.loads(resp.read().decode())

def find(o, key, out=None):
    if out is None: out = []
    if isinstance(o, list):
        for x in o: find(x, key, out)
    elif isinstance(o, dict):
        if o.get(key) is not None: out.append(o)
        else:
            for v in o.values(): find(v, key, out)
    return out

cobj = [c for c in find(cv, "channel_id") if c.get("channel_type") in (1, 2)][0]
cid  = cobj["channel_id"]
lseq = cobj.get("last_msg_seq")
print(f"test cid={cid}  uid={uid}  channel_type={cobj.get('channel_type')}  last_msg_seq={lseq}\n", flush=True)

# ---- 第一层：参数名识别（看 max_message_seq 是否 >0，代表匹配上了 channel）----
names = ["channel_id", "cid", "channel", "id", "chat_id", "conversation_id", "conv_id", "channelId"]
print("=== 参数名探测（max_message_seq>0 或 data 非空 = 命中） ===")
for n in names:
    r = req(f"/api/messages?{n}={cid}&uid={uid}&limit=50")
    mm = r.get("max_message_seq") if isinstance(r, dict) else None
    dn = len(r.get("data", [])) if isinstance(r, dict) else 0
    hit = (mm not in (0, None)) or dn > 0
    if hit:
        print(f"  ✅ {n}  ->  max_seq={mm} data_len={dn}")
    else:
        print(f"  ·  {n}  ->  空 (max_seq={mm})")

# ---- 第二层：即便参数名是 channel_id，也可能缺 seq 范围，试带 seq 组合 ----
print("\n=== 带 seq / limit 的取数实验 ===")
seqs = {
    "limit=100":                                  f"?channel_id={cid}&uid={uid}&limit=100",
    "start=0&limit=50":                           f"?channel_id={cid}&uid={uid}&start_message_seq=0&limit=50",
    f"end={lseq}&before":                          f"?channel_id={cid}&uid={uid}&end_message_seq={lseq}&limit=50",
    f"seq={lseq}&limit=50":                        f"?channel_id={cid}&uid={uid}&seq={lseq}&limit=50",
    f"before={lseq}&limit=50":                     f"?channel_id={cid}&uid={uid}&before={lseq}&limit=50",
    f"after=0&limit={lseq}":                       f"?channel_id={cid}&uid={uid}&after=0&limit={lseq}",
}
for tag, q in seqs.items():
    r = req("/api/messages" + q)
    dn = len(r.get("data", [])) if isinstance(r, dict) else 0
    mm = r.get("max_message_seq") if isinstance(r, dict) else None
    print(f"\n[{tag}]  data_len={dn} max_seq={mm}")
    if dn: print("SAMPLE:", json.dumps(r["data"][:2], ensure_ascii=False)[:500])

# ---- 第三层：POST 也试一下（很多消息接口是 POST）----
print("\n=== POST 实验 ===")
for body in (
    {"channel_id": cid, "uid": uid, "limit": 50},
    {"channel_id": cid, "uid": uid, "start_message_seq": 0, "limit": 50},
    {"cid": cid, "limit": 50},
):
    r = req("/api/messages", "POST", body)
    dn = len(r.get("data", [])) if isinstance(r, dict) else 0
    mm = r.get("max_message_seq") if isinstance(r, dict) else None
    print(f"\nPOST {json.dumps(body)} -> data_len={dn} max_seq={mm}")
    if dn: print("SAMPLE:", json.dumps(r["data"][:2], ensure_ascii=False)[:500])
