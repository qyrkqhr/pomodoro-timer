import json, urllib.request
BASE = "http://43.198.164.35:5300"

def get(p):
    r = urllib.request.urlopen(BASE + p, timeout=30)
    return json.loads(r.read().decode())

# 1) 看 connz 真实结构
c = get("/api/connz")
print("=== /api/connz 顶层类型:", type(c).__name__)
if isinstance(c, dict):
    print("顶层 keys:", list(c.keys()))
print("RAW connz(前600字):", json.dumps(c, ensure_ascii=False)[:600])

# 2) 按你截图的真实字段 conns 取 uid
conns = c.get("conns") if isinstance(c, dict) else c
uids = []
for it in conns:
    if isinstance(it, dict):
        for k in ("uid", "user_id", "id"):
            if it.get(k) is not None:
                uids.append(it[k]); break
    elif isinstance(it, (str, int)):
        uids.append(it)
print("\n解析出的 uid 列表:", uids)

# 3) 用第一个 uid 直接看 conversations 的原始结构
for u in uids[:1]:
    raw = get(f"/api/conversations?uid={u}")
    print(f"\n=== uid={u}  /api/conversations 顶层类型:", type(raw).__name__)
    if isinstance(raw, dict):
        print("顶层 keys:", list(raw.keys()))
    print("RAW(前1500字):")
    print(json.dumps(raw, ensure_ascii=False, indent=2)[:1500])
