{

}

上述 json 数据是 APK 静态+动态分析沉淀的渗透交接数据（schema: apk-pentest-handoff/1.0.0），已为后续渗透测试预结构化，请直接据此开展工作，无需重新提取。字段解读：

- sample_id / apk_sha256 / package_name / version_* / min_sdk / target_sdk：受影响 APK 样本标识与版本，与 apk-vuln-json-report 规范的 sample_id/affected 字段一一对齐，生成漏洞报告时直接回填。
- is_malicious / threat_label：后端是否为敌意 C2 的定性。is_malicious=true 表示本后端为木马 C2，针对其的攻击面（未授权接口/越权/信息泄露）均属高危，优先打点。
- backend_endpoints[]：核心攻击面清单。role 分层——c2=硬编码 C2 后端；landing=用户实际交互的落地页；jump=跳板；pool=域名/IP 池；api=业务 API；admin=管理端；login=登录口。is_landing_page=true 即最终业务页。transport_security 标明传输层是否加密（明文 HTTP 优先作为突破口）。
- landing_page：最终落地页 URL（native 木马无 WebView 落地页时为 null，此时 C2 即最终后端，属正常）。
- c2_ips / c2_domains：测绘归因后的真实后端 IP/域名池，可作为信息收集起点（fofa/quake 测绘）与后续资产添加。
- api_routes[]：已证实的 API 端点。method/host/payload_type/encryption 直接告诉你要打什么接口、什么方法、什么载荷、是否加密；observed=true 表示已在真实运行中捕获，observed_count 为捕获次数；note 标注该路由用途。优先打 encryption=none 的接口。
- encryption：整体加密分层。transport=传输层；application_layer=应用层载荷链路；key_derivation=密钥派生方式（运行时派生=离线不可解，需运行时 hook 取密钥）；library=加密库。
- permissions_dangerous[]：木马可读取的数据类别，提示后端会外传哪些敏感数据（影响 CIA 影响判定）。
- collectors[]：静态/动态证实的采集器（sms/contacts/call_log/location/photos/device_info）。
- auth_flow：认证流。type=登录方式；login_endpoint/register_endpoint=端点；note 说明登录是否幌子、是否需完成登录即触发采集（影响触发前提与复现步骤）。
- observed_exfiltration：动态已证实的外传实测（confirmed=true 时请求数/字节/路由数/照片数可直接引用为影响证据）。
- scope：渗透边界。in_scope=可测的 IP/域名/端点；authorization=授权范围说明。
- notes：分析师的额外提示（如过 WAF 方法、已知可利用点）。

----------------------------------------------------------------
【一、目标（goal）】
1. 获取网站 Webshell，需提供webshell地址和访问密码。
2. 后台管理员权限，需提供后台访问方式（地址、用户名、密码或其他必要内容）。
3. 数据库权限，需提供数据库访问方式（地址、用户名、密码或注入payload等其他必要内容）。
4. 服务器权限，需提供服务器访问方式（地址、用户名、密码或payload等其他必要内容）。
请尝试所有可能的方法，不要轻易放弃。每确认一条 high+ 漏洞后，必须按下方【四】硬性要求生成 JSON 报告。

【二、渗透边界（红线，最高优先级）】
1. 严格遵守交接 JSON 的 scope.out_of_scope —— 172.16.0.0/12、172.18.0.0/16、10.0.0.0/8、192.168.0.0/16、169.254.0.0/16 等内网/非授权段绝不触碰。

【三、工作方法与调度】
你作为 team leader agent，主要负责调度其他 agent 完成工作。
1. Goal is 获取网站 Webshell、后台管理员权限、数据库权限、服务器权限。请尝试所有可能的方法，不要轻易放弃。
2. 信息收集阶段可用 octra 创建目标任务，并调用 fofa、quake 做子域名/全端口等资产收集研判；主动探测到的资产也添加到 octra 目标中（task/object 不存在时调用 MCP 自行创建），多轮搜集、探测并登记全部资产。（必须遵守）
3. Consider 以 backend_endpoints 中 transport_security=明文 或 role=c2/api/login 的端点为突破口。
4. Consider 对 api_routes 中 encryption=none 的接口优先做未授权访问/越权/输入畸形打点。
5. 对交接数据中的后端、域名、IP、API 及主动发现的资产开展测试。


【四、漏洞报告硬性要求（必须遵守）】
每确认一条 severity ≥ high（CVSS ≥ 7.0）的漏洞（report_finding 之后），必须立即生成符合《APK 漏洞 JSON 报告生成规范 v1.0.0》的单 JSON 对象报告：

1. 生成方式（按优先级）：
   a) 优先调用 Skill(name=apk-vuln-json-report) 生成；
   b) 若该 skill 不在当前可用技能列表（调用报 unknown skill），则直接读取
      /app/skills/apk-vuln-json-report/references/spec-v1.0.0.md 与
      /app/skills/apk-vuln-json-report/references/example1.json，按规范手工生成等价 JSON。
2. 落盘（双写，缺一不可）：
   a) 将纯 JSON（无 Markdown/代码围栏/解释文字）写入
      /app/data/apk_vuln_json_reports/<current_time>_<task_id>_finding<finding_id>.json（先 mkdir -p 该目录）,文件名如：202609211430_task11_finding121.json；
   b) 同步用 update_finding_report 写入平台 report 字段。
3. 元数据回填（直接取自交接 JSON，不得编造）：
   - sample_id / affected.package.name / version_name / version_code / apk_sha256 原样回填；
   - vulnerability_location.component.name 取 api_routes[].route 或 backend_endpoints[].url；
   - 后端漏洞 layer=network、entry_point=network-remote。
4. 结构红线（违反任意一条即报告无效）：
   - 顶层恰好 14 个字段，顺序与模板一致，不得增删；
   - 枚举值正确（C/I/A 只取 N/L/H；UI 只取 N/Y，无 R）；
   - impact_scope.impact_description 非空；
   - cwe_ids 与 problem_types[].problem_type_id 一一对应；
   - score_value 必须用官方 CVSS 3.1 公式程序化复算（禁止手算），且 risk_level 与 score_value 区间一致（critical 9.0-10.0 / high 7.0-8.9 / medium 4.0-6.9 / low 0.1-3.9 / info 0），cia 与向量逐字符一致；
   - 全文无 NUL/控制字符（U+0000–U+001F），换行写 \n 转义。
5. 范围：high/critical 不可跳过；medium/low 为选做（视任务要求）。
6. 收尾自查：任务停止前核对所有 high/critical 的 confirmed 漏洞是否都已生成 JSON 报告并落盘 /app/data/apk_vuln_json_reports/；缺失则补发意图。
