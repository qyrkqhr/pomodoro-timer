{
  "findings": [
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "min_sdk": "23",
              "package_format": "APK",
              "package_name_source": "aapt2 dump badging（JADX 解析失败，加固/资源混淆包）",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "target_sdk": "35",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "aapt2 dump badging（JADX 解析失败，加固/资源混淆包）"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "medium",
        "cwe_ids": [
          "CWE-798"
        ],
        "detection_method": "static",
        "risk_level": "high",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "在 dex 字符串表与资源中匹配到 1 类凭据：Google API Key×1。根因是将密钥/口令以字面量形式固化在客户端（CWE-798）。证据示例：Google API Key=AIza********_3Zg（完整值见证据文件）。APK 可被任何人反编译，硬编码凭据等同于公开。触发前提：攻击者持有样本即可离线提取，无需运行应用。未验证边界：未确认这些凭据是否仍在有效期内、权限范围多大，也未调用对应云服务验证其可用性。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
          "I": "N"
        },
        "impact_description": "可离线提取的凭据可能被用于访问对应云服务、接口或数据；实际影响取决于凭据的有效期与授权范围。",
        "preconditions": [
          "攻击者持有样本 APK",
          "无需设备、账号或网络访问即可离线提取"
        ],
        "scope_note": "纯离线提取，属供应链侧泄露；凭据有效性与权限范围未验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "在 dex 字符串表与资源中匹配到 1 类凭据：Google API Key×1。根因是将密钥/口令以字面量形式固化在客户端（CWE-798）。证据示例：Google API Key=AIza********_3Zg（完整值见证据文件）。APK 可被任何人反编译，硬编码凭据等同于公开。触发前提：攻击者持有样本即可离线提取，无需运行应用。未验证边界：未确认这些凭据是否仍在有效期内、权限范围多大，也未调用对应云服务验证其可用性。（判定置信度：medium）"
            },
            {
              "lang": "en",
              "value": "Use of Hard-coded Credentials"
            }
          ],
          "name": "硬编码凭据的使用",
          "problem_type_id": "CWE-798",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "样本中可直接提取到 1 类疑似凭据。",
        "environment": {
          "device_model": null,
          "network_env": "不适用（静态分析，未发起网络请求）",
          "os": "不适用（离线静态分析，未在设备上运行）",
          "os_version": null,
          "prerequisite": "仅需样本 APK 文件",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "expected_result": "密钥应由服务端签发或使用短期凭据，不得硬编码在客户端。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "解析 classes*.dex 的 string_ids 字符串表与 resources.arsc 可打印串。",
            "actual": "提取到 65399 条字符串，匹配 1 类凭据特征。",
            "evidence_refs": [
              "evidence/hardcoded-secrets.txt"
            ],
            "expected": "敏感凭据不应以明文出现在客户端。",
            "seq": 1
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 7.5,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "代码/资源中硬编码了 1 类敏感凭据（Google API Key×1），可直接从样本中提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "Google API Key: 1 处",
          "name": "硬编码凭据",
          "type": "other"
        },
        "entry_point": "supply-chain",
        "layer": "code"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 teamgram.net（分类：api，评分 176），共 22 条完整 URL、14 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://teamgram.net | https://teamgram.net/ads | https://teamgram.net/ads/guidelines) | https://teamgram.net/core/bots/api。接口路径：/ads、/ads/guidelines)、/core/bots/api、/core/bots/webapps、/desktop/。 动态探活：地址可达，HTTP 200，Server=GitHub.com，TLS=valid，延迟 1175ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 teamgram.net（分类：api，评分 176），共 22 条完整 URL、14 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://teamgram.net | https://teamgram.net/ads | https://teamgram.net/ads/guidelines) | https://teamgram.net/core/bots/api。接口路径：/ads、/ads/guidelines)、/core/bots/api、/core/bots/webapps、/desktop/。 动态探活：地址可达，HTTP 200，Server=GitHub.com，TLS=valid，延迟 1175ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 teamgram.net 及 22 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 teamgram.net，累计 59 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-01-teamgram.net.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 teamgram.net 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=GitHub.com",
            "evidence_refs": [
              "evidence/endpoint-01-teamgram.net.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 teamgram.net（api），22 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 22 条；路径 14 条；来源 resources.arsc",
          "name": "teamgram.net",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 telegram.org（分类：unknown，评分 106），共 31 条完整 URL、10 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://telegram.org/faq | https://telegram.org/faq#general-questions | https://telegram.org/faq#q-i-have-a-new-phone-number-what-do-i-do | https://telegram.org/faq#troubleshooting。接口路径：/faq、/faq/ar、/faq/de、/faq/es、/faq/it。 动态探活：当前不可达（URLError: <urlopen error [Errno 101] Network is unreachable>），可能已下线、需要内网或需特定 Host 头。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。未确认地址是否在用。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 telegram.org（分类：unknown，评分 106），共 31 条完整 URL、10 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://telegram.org/faq | https://telegram.org/faq#general-questions | https://telegram.org/faq#q-i-have-a-new-phone-number-what-do-i-do | https://telegram.org/faq#troubleshooting。接口路径：/faq、/faq/ar、/faq/de、/faq/es、/faq/it。 动态探活：当前不可达（URLError: <urlopen error [Errno 101] Network is unreachable>），可能已下线、需要内网或需特定 Host 头。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 telegram.org 及 31 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 telegram.org，累计 62 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-02-telegram.org.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 telegram.org 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "不可达：URLError: <urlopen error [Errno 101] Network is unreachable>",
            "evidence_refs": [
              "evidence/endpoint-02-telegram.org.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 telegram.org（unknown），31 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 31 条；路径 10 条；来源 resources.arsc",
          "name": "telegram.org",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 api2-aw2453.openinstall.com（分类：api，评分 97），共 1 条完整 URL、1 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://api2-aw2453.openinstall.com/api/v2_5/android/aw2453/init?hwef=ylg965w&fe。接口路径：/api/v2_5/android/aw2453/init。 动态探活：地址可达，HTTP 404，Server=nginx，TLS=valid，延迟 336ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 api2-aw2453.openinstall.com（分类：api，评分 97），共 1 条完整 URL、1 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://api2-aw2453.openinstall.com/api/v2_5/android/aw2453/init?hwef=ylg965w&fe。接口路径：/api/v2_5/android/aw2453/init。 动态探活：地址可达，HTTP 404，Server=nginx，TLS=valid，延迟 336ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 api2-aw2453.openinstall.com 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 api2-aw2453.openinstall.com，累计 3 次引用，来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。",
            "evidence_refs": [
              "evidence/endpoint-03-api2-aw2453.openinstall.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 api2-aw2453.openinstall.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=valid，Server=nginx",
            "evidence_refs": [
              "evidence/endpoint-03-api2-aw2453.openinstall.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 api2-aw2453.openinstall.com（api），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 1 条；路径 1 条；来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har",
          "name": "api2-aw2453.openinstall.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 api.bing.com（分类：api，评分 95），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://api.bing.com/osjson.aspx?query=。接口路径：/osjson.aspx。 动态探活：地址可达，HTTP 400，Server=未知，TLS=valid，延迟 487ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 api.bing.com（分类：api，评分 95），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://api.bing.com/osjson.aspx?query=。接口路径：/osjson.aspx。 动态探活：地址可达，HTTP 400，Server=未知，TLS=valid，延迟 487ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 api.bing.com 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 api.bing.com，累计 2 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-04-api.bing.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 api.bing.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 400，TLS=valid，Server=None",
            "evidence_refs": [
              "evidence/endpoint-04-api.bing.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 api.bing.com（api），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 1 条；路径 1 条；来源 resources.arsc",
          "name": "api.bing.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 fragment.com（分类：unknown，评分 69），共 2 条完整 URL、2 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://fragment.com/ads/topup | https://fragment.com/stars。接口路径：/ads/topup、/stars。 动态探活：地址可达，HTTP 200，Server=cloudflare，TLS=valid，延迟 1505ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 fragment.com（分类：unknown，评分 69），共 2 条完整 URL、2 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://fragment.com/ads/topup | https://fragment.com/stars。接口路径：/ads/topup、/stars。 动态探活：地址可达，HTTP 200，Server=cloudflare，TLS=valid，延迟 1505ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 fragment.com 及 2 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 fragment.com，累计 4 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-05-fragment.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 fragment.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=cloudflare",
            "evidence_refs": [
              "evidence/endpoint-05-fragment.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 fragment.com（unknown），2 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 2 条；路径 2 条；来源 resources.arsc",
          "name": "fragment.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 teamgram.me（分类：unknown，评分 68），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://teamgram.me/TeamgramTips。接口路径：/TeamgramTips。 动态探活：地址可达，HTTP 200，Server=GitHub.com，TLS=valid，延迟 1163ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 teamgram.me（分类：unknown，评分 68），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://teamgram.me/TeamgramTips。接口路径：/TeamgramTips。 动态探活：地址可达，HTTP 200，Server=GitHub.com，TLS=valid，延迟 1163ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 teamgram.me 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 teamgram.me，累计 6 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-06-teamgram.me.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 teamgram.me 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=GitHub.com",
            "evidence_refs": [
              "evidence/endpoint-06-teamgram.me.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 teamgram.me（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 1 条；来源 resources.arsc",
          "name": "teamgram.me",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 res2-aw2453.opinstallinit.com（分类：unknown，评分 62），共 1 条完整 URL、1 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://res2-aw2453.opinstallinit.com/aw2453.dnc?t=1792408583079。接口路径：/aw2453.dnc。 动态探活：地址可达，HTTP 404，Server=nginx/1.20.1，TLS=valid，延迟 244ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 res2-aw2453.opinstallinit.com（分类：unknown，评分 62），共 1 条完整 URL、1 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://res2-aw2453.opinstallinit.com/aw2453.dnc?t=1792408583079。接口路径：/aw2453.dnc。 动态探活：地址可达，HTTP 404，Server=nginx/1.20.1，TLS=valid，延迟 244ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 res2-aw2453.opinstallinit.com 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 res2-aw2453.opinstallinit.com，累计 3 次引用，来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。",
            "evidence_refs": [
              "evidence/endpoint-07-res2-aw2453.opinstallinit.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 res2-aw2453.opinstallinit.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=valid，Server=nginx/1.20.1",
            "evidence_refs": [
              "evidence/endpoint-07-res2-aw2453.opinstallinit.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 res2-aw2453.opinstallinit.com（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 1 条；来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har",
          "name": "res2-aw2453.opinstallinit.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 web.teamgram.net（分类：unknown，评分 62），共 1 条完整 URL、0 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://web.teamgram.net/。接口路径：未提取到路径。 动态探活：地址可达，HTTP 403，Server=未知，TLS=valid，延迟 430ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 web.teamgram.net（分类：unknown，评分 62），共 1 条完整 URL、0 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://web.teamgram.net/。接口路径：未提取到路径。 动态探活：地址可达，HTTP 403，Server=未知，TLS=valid，延迟 430ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 web.teamgram.net 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 web.teamgram.net，累计 4 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-08-web.teamgram.net.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 web.teamgram.net 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 403，TLS=valid，Server=None",
            "evidence_refs": [
              "evidence/endpoint-08-web.teamgram.net.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 web.teamgram.net（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 0 条；来源 resources.arsc",
          "name": "web.teamgram.net",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 223.5.5.5（分类：unknown，评分 60），共 1 条完整 URL、0 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://223.5.5.5/。接口路径：未提取到路径。 动态探活：地址可达，HTTP 404，Server=未知，TLS=valid，延迟 135ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 223.5.5.5（分类：unknown，评分 60），共 1 条完整 URL、0 条接口路径。来源文件：c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。地址形态：HTTPS。URL 示例：https://223.5.5.5/。接口路径：未提取到路径。 动态探活：地址可达，HTTP 404，Server=未知，TLS=valid，延迟 135ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 223.5.5.5 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 223.5.5.5，累计 3 次引用，来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har。",
            "evidence_refs": [
              "evidence/endpoint-09-223.5.5.5.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 223.5.5.5 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=valid，Server=None",
            "evidence_refs": [
              "evidence/endpoint-09-223.5.5.5.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 223.5.5.5（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 0 条；来源 c84dfdc1df5a8111cc1f23634aec21f9-dyn.har",
          "name": "223.5.5.5",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 legal.yahoo.com（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://legal.yahoo.com/us/en/yahoo/privacy/index.html。接口路径：/us/en/yahoo/privacy/index.html。 动态探活：地址可达，HTTP 200，Server=ATS，TLS=valid，延迟 1589ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 legal.yahoo.com（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://legal.yahoo.com/us/en/yahoo/privacy/index.html。接口路径：/us/en/yahoo/privacy/index.html。 动态探活：地址可达，HTTP 200，Server=ATS，TLS=valid，延迟 1589ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 legal.yahoo.com 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 legal.yahoo.com，累计 2 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-10-legal.yahoo.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 legal.yahoo.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=ATS",
            "evidence_refs": [
              "evidence/endpoint-10-legal.yahoo.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 legal.yahoo.com（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 1 条；来源 resources.arsc",
          "name": "legal.yahoo.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 privacy.microsoft.com（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://privacy.microsoft.com/en-us/privacystatement。接口路径：/en-us/privacystatement。 动态探活：地址可达，HTTP 200，Server=未知，TLS=valid，延迟 7791ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 privacy.microsoft.com（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://privacy.microsoft.com/en-us/privacystatement。接口路径：/en-us/privacystatement。 动态探活：地址可达，HTTP 200，Server=未知，TLS=valid，延迟 7791ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 privacy.microsoft.com 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 privacy.microsoft.com，累计 2 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-11-privacy.microsoft.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 privacy.microsoft.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=None",
            "evidence_refs": [
              "evidence/endpoint-11-privacy.microsoft.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 privacy.microsoft.com（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 1 条；来源 resources.arsc",
          "name": "privacy.microsoft.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "c84dfdc1df5a8111cc1f23634aec21f9",
              "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
              "version_code": "66919",
              "version_name": "12.5.107",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "qxd.esyi.ac",
            "versions": [
              "12.5.107(66919)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-200"
        ],
        "detection_method": "hybrid",
        "risk_level": "info",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "硬编码敏感信息"
      },
      "details": "从样本中静态提取到后台地址 sugg.search.yahoo.net（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://sugg.search.yahoo.net/sg/?output=json&nresults=10&command=。接口路径：/sg/。 动态探活：地址可达，HTTP 500，Server=ATS，TLS=valid，延迟 1325ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "N",
          "I": "N"
        },
        "impact_description": "攻击者可离线枚举后台域名与接口路径，缩小攻击面并为后续越权、注入或数据抓取提供入口；地址本身不直接造成数据泄露。",
        "preconditions": [
          "攻击者可获取样本 APK（应用商店/安装包/设备提取）",
          "无需账号、设备或特殊权限即可离线提取"
        ],
        "scope_note": "属信息暴露类，本身不构成直接危害；风险来自地址可被用于后续测试。已通过探活确认地址可达。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "从样本中静态提取到后台地址 sugg.search.yahoo.net（分类：unknown，评分 60），共 1 条完整 URL、1 条接口路径。来源文件：resources.arsc。地址形态：HTTPS。URL 示例：https://sugg.search.yahoo.net/sg/?output=json&nresults=10&command=。接口路径：/sg/。 动态探活：地址可达，HTTP 500，Server=ATS，TLS=valid，延迟 1325ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Exposure of Sensitive Information to an Unauthorized Actor"
            }
          ],
          "name": "敏感信息暴露给未授权方",
          "problem_type_id": "CWE-200",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 sugg.search.yahoo.net 及 1 条接口 URL。",
        "environment": {
          "device_model": null,
          "network_env": "公网可达测试网络",
          "os": "不适用（静态提取+ HTTP 探活，未运行 APK）",
          "os_version": null,
          "prerequisite": "样本 APK 文件；探活需网络可达",
          "root_or_jailbreak": null,
          "tooling": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "expected_result": "后台地址属于服务端资产，不应以明文常量形式固化在客户端供任意人提取。",
        "reproducibility": "always",
        "steps": [
          {
            "action": "离线解包 APK，解析 classes*.dex 字符串表、resources.arsc、assets 与 .so 明文串，按 URL/域名/路径三类规则提取候选地址。",
            "actual": "命中 sugg.search.yahoo.net，累计 2 次引用，来源 resources.arsc。",
            "evidence_refs": [
              "evidence/endpoint-12-sugg.search.yahoo.net.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 sugg.search.yahoo.net 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 500，TLS=valid，Server=ATS",
            "evidence_refs": [
              "evidence/endpoint-12-sugg.search.yahoo.net.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 sugg.search.yahoo.net（unknown），1 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 1 条；路径 1 条；来源 resources.arsc",
          "name": "sugg.search.yahoo.net",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    }
  ],
  "report": {
    "apk_sha256": "eec57030d38f4083de56060a5b048f627e35ae05110f9cd1f4e4faf586935541",
    "class_count": 4,
    "endpoints": {
      "api_admin": 4,
      "categories": {
        "api": 4,
        "unknown": 17,
        "website": 2
      },
      "primary": {
        "alive": true,
        "base_urls": [
          "https://teamgram.net"
        ],
        "brand": false,
        "category": "api",
        "host": "teamgram.net",
        "http_status": 200,
        "path_count": 14,
        "paths_sample": [
          "/core/bots/api"
        ],
        "reason": "域名标签命中 接口 关键字；探活可达（HTTP 200）",
        "scheme": "https",
        "score": 176,
        "server": "GitHub.com",
        "tls": "valid",
        "url_count": 22
      },
      "probed": true,
      "top": [
        {
          "alive": true,
          "category": "api",
          "host": "teamgram.net",
          "http_status": 200,
          "score": 176
        },
        {
          "alive": false,
          "category": "unknown",
          "host": "telegram.org",
          "http_status": null,
          "score": 106
        },
        {
          "alive": true,
          "category": "api",
          "host": "api2-aw2453.openinstall.com",
          "http_status": 404,
          "score": 97
        },
        {
          "alive": true,
          "category": "api",
          "host": "api.bing.com",
          "http_status": 400,
          "score": 95
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "fragment.com",
          "http_status": 200,
          "score": 69
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "teamgram.me",
          "http_status": 200,
          "score": 68
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "res2-aw2453.opinstallinit.com",
          "http_status": 404,
          "score": 62
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "web.teamgram.net",
          "http_status": 403,
          "score": 62
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "223.5.5.5",
          "http_status": 404,
          "score": 60
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "legal.yahoo.com",
          "http_status": 200,
          "score": 60
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "privacy.microsoft.com",
          "http_status": 200,
          "score": 60
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "sugg.search.yahoo.net",
          "http_status": 500,
          "score": 60
        }
      ],
      "total": 23
    },
    "finding_count": 13,
    "findings": [
      {
        "confidence": "medium",
        "cwe": [
          "CWE-798"
        ],
        "file": "findings/01-cwe-798-硬编码敏感信息.json",
        "risk_level": "high",
        "score": 7.5,
        "summary": "代码/资源中硬编码了 1 类敏感凭据（Google API Key×1），可直接从样本中提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e01-cwe-200-teamgram.net.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 teamgram.net（api），22 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e02-cwe-200-telegram.org.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 telegram.org（unknown），31 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e03-cwe-200-api2-aw2453.openinstall.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 api2-aw2453.openinstall.com（api），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e04-cwe-200-api.bing.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 api.bing.com（api），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e05-cwe-200-fragment.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 fragment.com（unknown），2 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e06-cwe-200-teamgram.me.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 teamgram.me（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e07-cwe-200-res2-aw2453.opinstallinit.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 res2-aw2453.opinstallinit.com（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e08-cwe-200-web.teamgram.net.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 web.teamgram.net（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e09-cwe-200-223.5.5.5.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 223.5.5.5（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e10-cwe-200-legal.yahoo.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 legal.yahoo.com（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e11-cwe-200-privacy.microsoft.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 privacy.microsoft.com（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e12-cwe-200-sugg.search.yahoo.net.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 sugg.search.yahoo.net（unknown），1 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      }
    ],
    "min_sdk": "23",
    "package_name": "qxd.esyi.ac",
    "sample_file": "c84dfdc1df5a8111cc1f23634aec21f9.apk",
    "sample_id": "c84dfdc1df5a8111cc1f23634aec21f9",
    "target_sdk": "35",
    "version_code": "66919",
    "version_name": "12.5.107"
  }
}
