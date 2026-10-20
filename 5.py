{
  "findings": [
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-926"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "组件导出暴露"
      },
      "details": "清单中 18 个 Activity 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity, com.ss.android.ugc.aweme.ttopenapi.TtEntryActivity, com.ss.android.ugc.aweme.main.MainActivity, com.ss.android.ugc.aweme.detail.ui.DetailActivity, com.ss.android.ugc.aweme.wttsharesdk.WttShareActivity 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "L"
        },
        "impact_description": "任意同设备应用可向该 Activity 发送 Intent 触发其逻辑，可能造成越权操作、界面劫持或状态篡改。",
        "preconditions": [
          "攻击者应用可与目标应用安装在同一 Android 设备上",
          "目标组件在清单中导出且未声明 android:permission",
          "无需 root 或系统权限"
        ],
        "scope_note": "本地攻击面（同设备应用），非远程可利用；组件被调用后的真实业务影响未经动态验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "清单中 18 个 Activity 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity, com.ss.android.ugc.aweme.ttopenapi.TtEntryActivity, com.ss.android.ugc.aweme.main.MainActivity, com.ss.android.ugc.aweme.detail.ui.DetailActivity, com.ss.android.ugc.aweme.wttsharesdk.WttShareActivity 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Improper Export of Android Application Components"
            }
          ],
          "name": "Android 应用组件的不当导出",
          "problem_type_id": "CWE-926",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "18 个组件对任意同设备应用可达。",
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
        "expected_result": "导出组件应通过 android:permission 限定可调用方，或设置为 exported=\"false\"。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包样本 APK，用 JADX 解码 AndroidManifest.xml。",
            "actual": "成功解码清单，application 下共 18 个待确认组件。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "获得完整、可读的清单声明。",
            "seq": 1
          },
          {
            "action": "逐个检查 Activity 的 android:exported 与 android:permission 声明。",
            "actual": "18 个组件导出且无权限约束。",
            "evidence_refs": [
              "evidence/exported-components.txt"
            ],
            "expected": "导出组件应声明 android:permission 限制调用方。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N",
          "score_value": 5.1,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "导出的 Activity（18 个）未设置权限保护，任意应用可调用",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity；com.ss.android.ugc.aweme.ttopenapi.TtEntryActivity；com.ss.android.ugc.aweme.main.MainActivity；com.ss.android.ugc.aweme.detail.ui.DetailActivity；com.ss.android.ugc.aweme.wttsharesdk.WttShareActivity；com.ss.android.ugc.aweme.wxapi.WXEntryActivity；com.ss.android.ugc.aweme.rocketopen.RocketEntryActivity；com.ss.android.ugc.aweme.iesapi.AuthActivity 等共 18 个",
          "name": "多个Activity组件",
          "type": "activity"
        },
        "entry_point": "exported-component",
        "layer": "manifest"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-926"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "组件导出暴露"
      },
      "details": "清单中 28 个 Service 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.message.NotifyService, com.baidu.android.pushservice.CommandService, com.igexin.sdk.PushService, cn.jpush.android.service.DaemonService, com.ss.android.ugc.aweme.MiPushAliveServiceService 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "L"
        },
        "impact_description": "任意同设备应用可向该 Service 发送 Intent 触发其逻辑，可能造成越权操作、界面劫持或状态篡改。",
        "preconditions": [
          "攻击者应用可与目标应用安装在同一 Android 设备上",
          "目标组件在清单中导出且未声明 android:permission",
          "无需 root 或系统权限"
        ],
        "scope_note": "本地攻击面（同设备应用），非远程可利用；组件被调用后的真实业务影响未经动态验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "清单中 28 个 Service 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.message.NotifyService, com.baidu.android.pushservice.CommandService, com.igexin.sdk.PushService, cn.jpush.android.service.DaemonService, com.ss.android.ugc.aweme.MiPushAliveServiceService 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Improper Export of Android Application Components"
            }
          ],
          "name": "Android 应用组件的不当导出",
          "problem_type_id": "CWE-926",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "28 个组件对任意同设备应用可达。",
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
        "expected_result": "导出组件应通过 android:permission 限定可调用方，或设置为 exported=\"false\"。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包样本 APK，用 JADX 解码 AndroidManifest.xml。",
            "actual": "成功解码清单，application 下共 28 个待确认组件。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "获得完整、可读的清单声明。",
            "seq": 1
          },
          {
            "action": "逐个检查 Service 的 android:exported 与 android:permission 声明。",
            "actual": "28 个组件导出且无权限约束。",
            "evidence_refs": [
              "evidence/exported-components.txt"
            ],
            "expected": "导出组件应声明 android:permission 限制调用方。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N",
          "score_value": 5.1,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "导出的 Service（28 个）未设置权限保护，任意应用可调用",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "com.ss.android.message.NotifyService；com.baidu.android.pushservice.CommandService；com.igexin.sdk.PushService；cn.jpush.android.service.DaemonService；com.ss.android.ugc.aweme.MiPushAliveServiceService；com.bytedance.push.alliance.partner.Service1；com.bytedance.push.alliance.partner.Service2；com.bytedance.push.alliance.partner.Service3 等共 28 个",
          "name": "多个Service组件",
          "type": "service"
        },
        "entry_point": "exported-component",
        "layer": "manifest"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-926"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "组件导出暴露"
      },
      "details": "清单中 19 个 BroadcastReceiver 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.ugc.aweme.common.net.NetWorkStateReceiver, com.ss.android.ugc.aweme.playerservice.plugin.mediasession.MediaSessionReceiver, com.ss.android.message.MessageReceiver, com.ss.android.message.sswo.SswoReceiver, com.baidu.android.pushservice.RegistrationReceiver 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "L"
        },
        "impact_description": "任意同设备应用可向该 BroadcastReceiver 发送 Intent 触发其逻辑，可能造成越权操作、界面劫持或状态篡改。",
        "preconditions": [
          "攻击者应用可与目标应用安装在同一 Android 设备上",
          "目标组件在清单中导出且未声明 android:permission",
          "无需 root 或系统权限"
        ],
        "scope_note": "本地攻击面（同设备应用），非远程可利用；组件被调用后的真实业务影响未经动态验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "清单中 19 个 BroadcastReceiver 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.ss.android.ugc.aweme.common.net.NetWorkStateReceiver, com.ss.android.ugc.aweme.playerservice.plugin.mediasession.MediaSessionReceiver, com.ss.android.message.MessageReceiver, com.ss.android.message.sswo.SswoReceiver, com.baidu.android.pushservice.RegistrationReceiver 等 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Improper Export of Android Application Components"
            }
          ],
          "name": "Android 应用组件的不当导出",
          "problem_type_id": "CWE-926",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "19 个组件对任意同设备应用可达。",
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
        "expected_result": "导出组件应通过 android:permission 限定可调用方，或设置为 exported=\"false\"。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包样本 APK，用 JADX 解码 AndroidManifest.xml。",
            "actual": "成功解码清单，application 下共 19 个待确认组件。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "获得完整、可读的清单声明。",
            "seq": 1
          },
          {
            "action": "逐个检查 BroadcastReceiver 的 android:exported 与 android:permission 声明。",
            "actual": "19 个组件导出且无权限约束。",
            "evidence_refs": [
              "evidence/exported-components.txt"
            ],
            "expected": "导出组件应声明 android:permission 限制调用方。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N",
          "score_value": 5.1,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "导出的 BroadcastReceiver（19 个）未设置权限保护，任意应用可调用",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "com.ss.android.ugc.aweme.common.net.NetWorkStateReceiver；com.ss.android.ugc.aweme.playerservice.plugin.mediasession.MediaSessionReceiver；com.ss.android.message.MessageReceiver；com.ss.android.message.sswo.SswoReceiver；com.baidu.android.pushservice.RegistrationReceiver；com.igexin.sdk.PushReceiver；com.ss.android.push.window.oppo.ScreenReceiver；com.meizu.message.MzMessageReceiver 等共 19 个",
          "name": "多个BroadcastReceiver组件",
          "type": "receiver"
        },
        "entry_point": "exported-component",
        "layer": "manifest"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-926"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "组件导出暴露"
      },
      "details": "清单中 1 个 ContentProvider 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.bytedance.sdk.account.share.provider.AccountShareProvider 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
          "I": "N"
        },
        "impact_description": "未授权应用可查询/插入/删除该 Provider 暴露的数据，具体影响取决于该 Provider 的查询实现与底层数据敏感度。",
        "preconditions": [
          "攻击者应用可与目标应用安装在同一 Android 设备上",
          "目标组件在清单中导出且未声明 android:permission",
          "无需 root 或系统权限"
        ],
        "scope_note": "本地攻击面（同设备应用），非远程可利用；组件被调用后的真实业务影响未经动态验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "清单中 1 个 ContentProvider 声明为 exported=\"true\"（或未显式声明但因含 intent-filter 而默认导出），且组件与 application 均未声明 android:permission。根因是组件导出缺少权限约束（CWE-926）。证据：解码后的 AndroidManifest.xml 中可见 com.bytedance.sdk.account.share.provider.AccountShareProvider 满足上述条件。触发前提：攻击应用与目标安装在同一设备，无需特殊权限即可构造显式 Intent。未验证边界：各组件被调用后的具体业务后果需结合实现判断，本报告仅确认导出可达性。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Improper Export of Android Application Components"
            }
          ],
          "name": "Android 应用组件的不当导出",
          "problem_type_id": "CWE-926",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "1 个组件对任意同设备应用可达。",
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
        "expected_result": "导出组件应通过 android:permission 限定可调用方，或设置为 exported=\"false\"。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包样本 APK，用 JADX 解码 AndroidManifest.xml。",
            "actual": "成功解码清单，application 下共 1 个待确认组件。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "获得完整、可读的清单声明。",
            "seq": 1
          },
          {
            "action": "逐个检查 ContentProvider 的 android:exported 与 android:permission 声明。",
            "actual": "1 个组件导出且无权限约束。",
            "evidence_refs": [
              "evidence/exported-components.txt"
            ],
            "expected": "导出组件应声明 android:permission 限制调用方。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 6.2,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "导出的 ContentProvider（1 个）未设置权限保护，任意应用可访问其数据",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "com.bytedance.sdk.account.share.provider.AccountShareProvider",
          "name": "com.bytedance.sdk.account.share.provider.AccountShareProvider",
          "type": "provider"
        },
        "entry_point": "exported-component",
        "layer": "manifest"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "medium",
        "cwe_ids": [
          "CWE-939"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "DeepLink漏洞"
      },
      "details": "清单中 4 个导出 Activity 通过 intent-filter/data 注册了自定义 Scheme：aweme:///pluginlist, snssdk1128://*, taobao://detail.aweme.sdk.com, taobao://main.aweme.sdk.com。此类深链入口默认可被任意应用或浏览器构造 Intent 唤起，若 Activity 直接信任 Intent 中的参数（如跳转地址、token、金额）即形成越权。根因是为自定义 URL Scheme 的处理器缺少授权校验（CWE-939）。证据：com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity, com.ss.android.ugc.aweme.main.MainActivity, com.ss.android.ugc.aweme.detail.ui.DetailActivity, com.ss.android.ugc.aweme.plugin.ui.PluginListActivity。未验证边界：未确认这些 Activity 是否对参数做校验，实际可利用性需结合实现判断。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "L"
        },
        "impact_description": "攻击者可构造深链唤起目标页面并注入参数，可能导致越权跳转、敏感操作被诱导执行；具体后果取决于 Activity 对参数的信任程度。",
        "preconditions": [
          "目标 Activity 导出且注册了自定义 Scheme",
          "攻击者可通过网页或同设备应用构造 Intent",
          "需用户点击链接（存在交互前提）"
        ],
        "scope_note": "本地/浏览器触发，需用户交互；参数校验情况未验证。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "清单中 4 个导出 Activity 通过 intent-filter/data 注册了自定义 Scheme：aweme:///pluginlist, snssdk1128://*, taobao://detail.aweme.sdk.com, taobao://main.aweme.sdk.com。此类深链入口默认可被任意应用或浏览器构造 Intent 唤起，若 Activity 直接信任 Intent 中的参数（如跳转地址、token、金额）即形成越权。根因是为自定义 URL Scheme 的处理器缺少授权校验（CWE-939）。证据：com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity, com.ss.android.ugc.aweme.main.MainActivity, com.ss.android.ugc.aweme.detail.ui.DetailActivity, com.ss.android.ugc.aweme.plugin.ui.PluginListActivity。未验证边界：未确认这些 Activity 是否对参数做校验，实际可利（判定置信度：medium）"
            },
            {
              "lang": "en",
              "value": "Improper Authorization in Handler for Custom URL Scheme"
            }
          ],
          "name": "自定义 URL Scheme 处理器中的不当授权",
          "problem_type_id": "CWE-939",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "4 个深链入口对任意调用方可达。",
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
        "expected_result": "深链处理入口应校验调用方身份与参数白名单。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "离线解包并解码 AndroidManifest.xml。",
            "actual": "解码成功。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "获得组件与 intent-filter 声明。",
            "seq": 1
          },
          {
            "action": "筛出含 <data android:scheme> 的导出 Activity。",
            "actual": "发现 4 个深链入口：aweme:///pluginlist, snssdk1128://*, taobao://detail.aweme.sdk.com, taobao://main.aweme.sdk.com。",
            "evidence_refs": [
              "evidence/deeplinks.txt"
            ],
            "expected": "深链入口应对调用方来源做校验。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N",
          "score_value": 4.4,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "导出 Activity 注册了 4 条自定义 URL Scheme，未校验来源即可被任意应用或浏览器唤起",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "com.ss.android.ugc.aweme.main.deeplink.DeepLinkHandlerActivity [snssdk1128://*]；com.ss.android.ugc.aweme.main.MainActivity [taobao://main.aweme.sdk.com]；com.ss.android.ugc.aweme.detail.ui.DetailActivity [taobao://detail.aweme.sdk.com]；com.ss.android.ugc.aweme.plugin.ui.PluginListActivity [aweme:///pluginlist]",
          "name": "多个 Activity（4 个）",
          "type": "activity"
        },
        "entry_point": "deeplink",
        "layer": "manifest"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "medium",
        "cwe_ids": [
          "CWE-319"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "不安全网络通信"
      },
      "details": "代码/资源中存在 29 个 http:// 明文地址；并配置了自定义 networkSecurityConfig，需人工确认是否放行明文。根因是未强制使用 TLS（CWE-319）。证据：http://abroad.apilocate.amap.com/mobile/binary, http://ad.toutiao.com/advertiser_package/, http://alog.umeng.com/app_logs, http://alog.umengcloud.com/app_logs, http://apilocate.amap.com/mobile/binary。在公共 Wi-Fi 等不可信网络下，攻击者可对明文流量进行嗅探与篡改，导致凭据、会话或业务数据泄露。未验证边界：未实测这些地址是否仍在使用，也未验证是否存在证书固定等补偿措施。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
          "I": "N"
        },
        "impact_description": "同一网络下的攻击者可嗅探、篡改明文流量，可能导致凭据泄露或业务数据被篡改。",
        "preconditions": [
          "攻击者与用户处于同一网络（如公共 Wi-Fi）或可实施中间人攻击",
          "应用实际通过 http:// 传输业务或认证数据"
        ],
        "scope_note": "远程网络位置利用，需中间人前提；未验证明文接口是否为生产在用。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "代码/资源中存在 29 个 http:// 明文地址；并配置了自定义 networkSecurityConfig，需人工确认是否放行明文。根因是未强制使用 TLS（CWE-319）。证据：http://abroad.apilocate.amap.com/mobile/binary, http://ad.toutiao.com/advertiser_package/, http://alog.umeng.com/app_logs, http://alog.umengcloud.com/app_logs, http://apilocate.amap.com/mobile/binary。在公共 Wi-Fi 等不可信网络下，攻击者可对明文流量进行嗅探与篡改，导致凭据、会话或业务数据泄露。未验证边界：未实测这些地址是否仍在使用，也未验证是否存在证书固定等补偿措施。（判定置信度：medium）"
            },
            {
              "lang": "en",
              "value": "Cleartext Transmission of Sensitive Information"
            }
          ],
          "name": "敏感信息的明文传输",
          "problem_type_id": "CWE-319",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "存在明文传输放行配置与 http:// 地址。",
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
        "expected_result": "应用应仅使用 HTTPS，并通过 networkSecurityConfig 禁止明文。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "解码 AndroidManifest.xml 并检查 usesCleartextTraffic 与 networkSecurityConfig。",
            "actual": "代码/资源中存在 29 个 http:// 明文地址；并配置了自定义 networkSecurityConfig，需人工确认是否放行明文。",
            "evidence_refs": [
              "evidence/manifest.xml"
            ],
            "expected": "生产应用应禁止明文传输。",
            "seq": 1
          },
          {
            "action": "扫描 dex 字符串表与资源，提取以 http:// 开头的接口地址。",
            "actual": "命中 29 个明文地址。",
            "evidence_refs": [
              "evidence/cleartext-endpoints.txt"
            ],
            "expected": "不应存在明文接口地址。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "应用允许 HTTP 明文传输，且存在硬编码的 http:// 接口地址，流量可被中间人窃听或篡改",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "代码/资源中存在 29 个 http:// 明文地址；并配置了自定义 networkSecurityConfig，需人工确认是否放行明文",
          "name": "网络通信配置",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "low",
        "cwe_ids": [
          "CWE-749"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "JSBridge漏洞"
      },
      "details": "dex 字符串中存在 addJavascriptInterface 调用，同时存在 setJavaScriptEnabled。根因是向 WebView 暴露了原生方法而未限制可加载页面的来源（CWE-749）。证据：字符串表中命中 addJavascriptInterface与 setJavaScriptEnabled。若 WebView 加载了外部或可被劫持的页面，页面脚本即可调用被暴露的原生方法，读取本地数据或触发敏感操作；在 API 17 以下该接口可直接反射执行任意方法。未验证边界：未确认 WebView 实际加载的 URL 来源、是否校验域名、注入对象暴露了哪些方法，因此实际可利用性未证实。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "L"
        },
        "impact_description": "若满足前提，页面脚本可调用原生方法，可能读取本地数据或触发敏感操作。",
        "preconditions": [
          "WebView 加载了攻击者可影响的内容（外部链接、被劫持的 HTTP 页面）",
          "注入对象包含敏感方法",
          "需用户交互打开页面"
        ],
        "scope_note": "远程内容触发但需用户交互；加载源与注入方法未验证，属候选结论。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "dex 字符串中存在 addJavascriptInterface 调用，同时存在 setJavaScriptEnabled。根因是向 WebView 暴露了原生方法而未限制可加载页面的来源（CWE-749）。证据：字符串表中命中 addJavascriptInterface与 setJavaScriptEnabled。若 WebView 加载了外部或可被劫持的页面，页面脚本即可调用被暴露的原生方法，读取本地数据或触发敏感操作；在 API 17 以下该接口可直接反射执行任意方法。未验证边界：未确认 WebView 实际加载的 URL 来源、是否校验域名、注入对象暴露了哪些方法，因此实际可利用性未证实。（判定置信度：low）"
            },
            {
              "lang": "en",
              "value": "Exposed Dangerous Method or Function"
            }
          ],
          "name": "暴露危险方法或函数",
          "problem_type_id": "CWE-749",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "存在原生对象注入与 JavaScript 启用迹象。",
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
        "expected_result": "应使用 WebViewClient 白名单限制可加载域名，并最小化暴露的原生方法。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "扫描 dex 字符串表中的 WebView 相关 API 引用。",
            "actual": "命中 addJavascriptInterface，且启用 JavaScript。",
            "evidence_refs": [
              "evidence/webview-js-interface.txt"
            ],
            "expected": "不应向不可信页面暴露原生对象。",
            "seq": 1
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N",
          "score_value": 4.2,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "应用通过 addJavascriptInterface 向 WebView 注入 Java 对象，若加载不可信页面可被调用",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "addJavascriptInterface；setJavaScriptEnabled",
          "name": "WebView JavaScript 接口",
          "type": "other"
        },
        "entry_point": "other",
        "layer": "webview"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "low",
        "cwe_ids": [
          "CWE-295"
        ],
        "detection_method": "static",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "证书校验缺陷"
      },
      "details": "字符串表命中 onReceivedSslError、checkServerTrusted。根因是证书/主机名校验可被自定义实现放宽（CWE-295）。覆写 onReceivedSslError 后若直接调用 proceed()，或使用 ALLOW_ALL_HOSTNAME_VERIFIER，会使 HTTPS 失去身份认证能力，攻击者可借伪造证书实施中间人攻击。证据：上述符号出现在 dex 字符串表中。未验证边界：未反编译确认回调内是否真的调用了 proceed()，也未确认该校验是否覆盖全部网络请求，属候选结论。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
          "I": "N"
        },
        "impact_description": "若校验确被放宽，中间人可解密或篡改 HTTPS 流量。",
        "preconditions": [
          "应用实际使用被覆写的校验逻辑处理 HTTPS 连接",
          "攻击者可实施中间人攻击（如伪造 CA 或劫持网络）"
        ],
        "scope_note": "远程需中间人前提；回调实现未反编译确认，属候选。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "字符串表命中 onReceivedSslError、checkServerTrusted。根因是证书/主机名校验可被自定义实现放宽（CWE-295）。覆写 onReceivedSslError 后若直接调用 proceed()，或使用 ALLOW_ALL_HOSTNAME_VERIFIER，会使 HTTPS 失去身份认证能力，攻击者可借伪造证书实施中间人攻击。证据：上述符号出现在 dex 字符串表中。未验证边界：未反编译确认回调内是否真的调用了 proceed()，也未确认该校验是否覆盖全部网络请求，属候选结论。（判定置信度：low）"
            },
            {
              "lang": "en",
              "value": "Improper Certificate Validation"
            }
          ],
          "name": "证书校验不当",
          "problem_type_id": "CWE-295",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "存在自定义证书校验符号。",
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
        "expected_result": "证书校验应使用系统默认 TrustManager，不得在 onReceivedSslError 中无条件 proceed。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "扫描 dex 字符串表中的证书校验相关符号。",
            "actual": "命中 onReceivedSslError、checkServerTrusted。",
            "evidence_refs": [
              "evidence/ssl-validation.txt"
            ],
            "expected": "不应实现放行全部证书的校验逻辑。",
            "seq": 1
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "应用覆写了 WebView/HTTP 的证书校验逻辑，存在忽略证书错误、绕过校验的风险",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "onReceivedSslError、checkServerTrusted",
          "name": "证书校验实现",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "code"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "min_sdk": "17",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性（JADX 解码）",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "target_sdk": "26",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 package 属性（JADX 解码）"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "low",
        "cwe_ids": [
          "CWE-327"
        ],
        "detection_method": "static",
        "risk_level": "low",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1"
          ]
        },
        "vuln_class": "加密算法误用"
      },
      "details": "字符串表命中弱算法标识：/ECB/、AES/ECB、DES/、DESede、RC4、SHA1withRSA。根因是选用已被证明不安全的加密算法或分组模式（CWE-327）。DES/RC4 密钥空间不足，ECB 模式对相同明文产生相同密文、泄露数据结构，均可被离线分析破解。证据：上述算法标识出现在 dex 中。未验证边界：可能来自第三方库的兼容代码而非业务关键路径，也未确认其保护的数据敏感度，属候选结论。（CWE 在线核对未完成，名称取自本地映射。）",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "L",
          "I": "N"
        },
        "impact_description": "使用弱算法保护的敏感数据存在被离线破解的风险。",
        "preconditions": [
          "弱算法实际用于保护业务数据或凭据",
          "攻击者能获取密文"
        ],
        "scope_note": "结论基于符号存在性，未确认调用路径与保护对象，属候选。"
      },
      "problem_types": [
        {
          "descriptions": [
            {
              "lang": "zh",
              "value": "字符串表命中弱算法标识：/ECB/、AES/ECB、DES/、DESede、RC4、SHA1withRSA。根因是选用已被证明不安全的加密算法或分组模式（CWE-327）。DES/RC4 密钥空间不足，ECB 模式对相同明文产生相同密文、泄露数据结构，均可被离线分析破解。证据：上述算法标识出现在 dex 中。未验证边界：可能来自第三方库的兼容代码而非业务关键路径，也未确认其保护的数据敏感度，属候选结论。（判定置信度：low）"
            },
            {
              "lang": "en",
              "value": "Use of a Broken or Risky Cryptographic Algorithm"
            }
          ],
          "name": "使用已被攻破或存在风险的加密算法",
          "problem_type_id": "CWE-327",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "存在弱算法/ECB 模式的使用痕迹。",
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
        "expected_result": "应使用 AES/GCM 等安全算法与模式，并正确管理密钥与 IV。",
        "reproducibility": "unverified",
        "steps": [
          {
            "action": "扫描 dex 字符串表中的加密算法标识。",
            "actual": "命中 /ECB/、AES/ECB、DES/、DESede、RC4、SHA1withRSA。",
            "evidence_refs": [
              "evidence/weak-crypto.txt"
            ],
            "expected": "应使用 AES-GCM 等现代算法与随机 IV。",
            "seq": 1
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N",
          "score_value": 3.7,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "应用使用弱加密算法或 ECB 模式（/ECB/, AES/ECB, DES/, DESede），加密数据易被破解",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "/ECB/、AES/ECB、DES/、DESede、RC4、SHA1withRSA",
          "name": "加密实现",
          "type": "other"
        },
        "entry_point": "other",
        "layer": "crypto"
      }
    },
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 aweme.snssdk.com（分类：api，评分 234），共 24 条完整 URL、22 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex, classes4.dex。地址形态：HTTPS。URL 示例：https://aweme.snssdk.com | https://aweme.snssdk.com/aweme/v1/multiple/login/unbind/ | https://aweme.snssdk.com/aweme/v1/notice/ | https://aweme.snssdk.com/aweme/v1/urge/history/list/。接口路径：/aweme/v1/multiple/login/unbind/、/aweme/v1/notice/、/aweme/v1/urge/history/list/、/aweme/v1/urge/list/、/aweme/v1/user/set/settings/。 动态探活：地址可达，HTTP 404，Server=Tengine，TLS=valid，延迟 210ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 aweme.snssdk.com（分类：api，评分 234），共 24 条完整 URL、22 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex, classes4.dex。地址形态：HTTPS。URL 示例：https://aweme.snssdk.com | https://aweme.snssdk.com/aweme/v1/multiple/login/unbind/ | https://aweme.snssdk.com/aweme/v1/notice/ | https://aweme.snssdk.com/aweme/v1/urge/history/list/。接口路径：/aweme/v1/multiple/login/unbind/、/aweme/v1/notice/、/aweme/v1/urge/history/list/、/aweme/v1/urge/list/、/aweme/v1/user/set/settings/。 动态探活：地址可达，HTTP 404，Server=Tengine，TLS=valid，延迟 210ms。 未验（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 aweme.snssdk.com 及 24 条接口 URL。",
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
            "actual": "命中 aweme.snssdk.com，累计 56 次引用，来源 classes.dex, classes2.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-01-aweme.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 aweme.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=valid，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-01-aweme.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 aweme.snssdk.com（api），24 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 24 条；路径 22 条；来源 classes.dex, classes2.dex, classes3.dex",
          "name": "aweme.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-319"
        ],
        "detection_method": "hybrid",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "不安全网络通信"
      },
      "details": "从样本中静态提取到后台地址 mon.snssdk.com（分类：api，评分 147），共 7 条完整 URL、7 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：明文 HTTP。URL 示例：http://mon.snssdk.com/monitor/collect/c/cloudcontrol/file | https://mon.snssdk.com/monitor/appmonitor/v2/settings | https://mon.snssdk.com/monitor/appmonitor/v3/settings | https://mon.snssdk.com/monitor/collect/。接口路径：/monitor/appmonitor/v2/settings、/monitor/appmonitor/v3/settings、/monitor/collect/、/monitor/collect/c/cloudcontrol/file、/monitor/collect/c/logcollect。 动态探活：地址可达，HTTP 504，Server=volc-dcdn，TLS=valid，延迟 3225ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
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
              "value": "从样本中静态提取到后台地址 mon.snssdk.com（分类：api，评分 147），共 7 条完整 URL、7 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：明文 HTTP。URL 示例：http://mon.snssdk.com/monitor/collect/c/cloudcontrol/file | https://mon.snssdk.com/monitor/appmonitor/v2/settings | https://mon.snssdk.com/monitor/appmonitor/v3/settings | https://mon.snssdk.com/monitor/collect/。接口路径：/monitor/appmonitor/v2/settings、/monitor/appmonitor/v3/settings、/monitor/collect/、/monitor/collect/c/cloudcontrol/file、/monitor/collect/c/logcollect。 动态探活：地址可达，HTTP 504，Server=volc-dcdn，TL（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Cleartext Transmission of Sensitive Information"
            }
          ],
          "name": "敏感信息的明文传输",
          "problem_type_id": "CWE-319",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 mon.snssdk.com 及 7 条接口 URL。",
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
            "actual": "命中 mon.snssdk.com，累计 15 次引用，来源 classes.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-02-mon.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 mon.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 504，TLS=valid，Server=volc-dcdn",
            "evidence_refs": [
              "evidence/endpoint-02-mon.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置明文后台地址 mon.snssdk.com（api），7 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 7 条；路径 7 条；来源 classes.dex, classes3.dex",
          "name": "mon.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 log.snssdk.com（分类：unknown，评分 122），共 7 条完整 URL、7 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://log.snssdk.com/monitor/collect/c/crash | https://log.snssdk.com/monitor/collect/c/exception | https://log.snssdk.com/monitor/collect/c/exception/dump_collection | https://log.snssdk.com/monitor/collect/c/native_bin_crash。接口路径：/monitor/collect/c/crash、/monitor/collect/c/exception、/monitor/collect/c/exception/dump_collection、/monitor/collect/c/native_bin_crash、/service/2/app_log/。 动态探活：地址可达，HTTP 504，Server=Tengine，TLS=valid，延迟 3233ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 log.snssdk.com（分类：unknown，评分 122），共 7 条完整 URL、7 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://log.snssdk.com/monitor/collect/c/crash | https://log.snssdk.com/monitor/collect/c/exception | https://log.snssdk.com/monitor/collect/c/exception/dump_collection | https://log.snssdk.com/monitor/collect/c/native_bin_crash。接口路径：/monitor/collect/c/crash、/monitor/collect/c/exception、/monitor/collect/c/exception/dump_collection、/monitor/collect/c/native_bin_crash、/service/2/app_log/。 动态探活：地址可达，HTT（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 log.snssdk.com 及 7 条接口 URL。",
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
            "actual": "命中 log.snssdk.com，累计 15 次引用，来源 classes.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-03-log.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 log.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 504，TLS=valid，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-03-log.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 log.snssdk.com（unknown），7 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 7 条；路径 7 条；来源 classes.dex, classes3.dex",
          "name": "log.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-319"
        ],
        "detection_method": "hybrid",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "不安全网络通信"
      },
      "details": "从样本中静态提取到后台地址 open.e.189.cn（分类：api，评分 118），共 4 条完整 URL、2 条接口路径。来源文件：classes.dex。地址形态：明文 HTTP。URL 示例：http://open.e.189.cn/ | http://open.e.189.cn/openapi/networkauth/preGetMobile.do | https://open.e.189.cn/ | https://open.e.189.cn/openapi/special/getTimeStamp.do。接口路径：/openapi/networkauth/preGetMobile.do、/openapi/special/getTimeStamp.do。 动态探活：地址可达，HTTP 200，Server=未知，TLS=n/a，延迟 134ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
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
              "value": "从样本中静态提取到后台地址 open.e.189.cn（分类：api，评分 118），共 4 条完整 URL、2 条接口路径。来源文件：classes.dex。地址形态：明文 HTTP。URL 示例：http://open.e.189.cn/ | http://open.e.189.cn/openapi/networkauth/preGetMobile.do | https://open.e.189.cn/ | https://open.e.189.cn/openapi/special/getTimeStamp.do。接口路径：/openapi/networkauth/preGetMobile.do、/openapi/special/getTimeStamp.do。 动态探活：地址可达，HTTP 200，Server=未知，TLS=n/a，延迟 134ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Cleartext Transmission of Sensitive Information"
            }
          ],
          "name": "敏感信息的明文传输",
          "problem_type_id": "CWE-319",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 open.e.189.cn 及 4 条接口 URL。",
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
            "actual": "命中 open.e.189.cn，累计 8 次引用，来源 classes.dex。",
            "evidence_refs": [
              "evidence/endpoint-04-open.e.189.cn.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 open.e.189.cn 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=n/a，Server=None",
            "evidence_refs": [
              "evidence/endpoint-04-open.e.189.cn.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置明文后台地址 open.e.189.cn（api），4 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 4 条；路径 2 条；来源 classes.dex",
          "name": "open.e.189.cn",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 security.snssdk.com（分类：api，评分 101），共 6 条完整 URL、6 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://security.snssdk.com/api/plugin/config/v2/ | https://security.snssdk.com/api/plugin/config/v3/ | https://security.snssdk.com/passport/safe/api/safe_center/index/?append_common_p | https://security.snssdk.com/passport/safe/aweme/center.html?did=%s。接口路径：/api/plugin/config/v2/、/api/plugin/config/v3/、/passport/safe/api/safe_center/index/、/passport/safe/aweme/center.html、/passport/safe/aweme/unlock.html。 动态探活：当前不可达（TimeoutError: The read operation timed out），可能已下线、需要内网或需特定 Host 头。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 security.snssdk.com（分类：api，评分 101），共 6 条完整 URL、6 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://security.snssdk.com/api/plugin/config/v2/ | https://security.snssdk.com/api/plugin/config/v3/ | https://security.snssdk.com/passport/safe/api/safe_center/index/?append_common_p | https://security.snssdk.com/passport/safe/aweme/center.html?did=%s。接口路径：/api/plugin/config/v2/、/api/plugin/config/v3/、/passport/safe/api/safe_center/index/、/passport/safe/aweme/center.html、/passport/sa（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 security.snssdk.com 及 6 条接口 URL。",
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
            "actual": "命中 security.snssdk.com，累计 14 次引用，来源 classes.dex, classes2.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-05-security.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 security.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "不可达：TimeoutError: The read operation timed out",
            "evidence_refs": [
              "evidence/endpoint-05-security.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 security.snssdk.com（api），6 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 6 条；路径 6 条；来源 classes.dex, classes2.dex, classes3.dex",
          "name": "security.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-319"
        ],
        "detection_method": "hybrid",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "不安全网络通信"
      },
      "details": "从样本中静态提取到后台地址 sf1-ttcdn-tos.pstatp.com（分类：unknown，评分 97），共 4 条完整 URL、4 条接口路径。来源文件：classes.dex, classes2.dex。地址形态：明文 HTTP。URL 示例：http://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/webp/DY_guess_draw_loading.webp | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/live_bg/live_audio_bg_j.png | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/live_bg/live_audio_bg_o.png | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/webp/audio_live.webp。接口路径：/obj/ttfe/ttlive/live_bg/live_audio_bg_j.png、/obj/ttfe/ttlive/live_bg/live_audio_bg_o.png、/obj/ttfe/ttlive/webp/DY_guess_draw_loading.webp、/obj/ttfe/ttlive/webp/audio_live.webp。 动态探活：地址可达，HTTP 404，Server=Tengine，TLS=n/a，延迟 223ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
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
              "value": "从样本中静态提取到后台地址 sf1-ttcdn-tos.pstatp.com（分类：unknown，评分 97），共 4 条完整 URL、4 条接口路径。来源文件：classes.dex, classes2.dex。地址形态：明文 HTTP。URL 示例：http://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/webp/DY_guess_draw_loading.webp | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/live_bg/live_audio_bg_j.png | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/live_bg/live_audio_bg_o.png | https://sf1-ttcdn-tos.pstatp.com/obj/ttfe/ttlive/webp/audio_live.webp。接口路径：/obj/ttfe/ttlive/live_bg/live_audio_bg_j.png、/obj/ttfe/ttlive/live_bg/live_au（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Cleartext Transmission of Sensitive Information"
            }
          ],
          "name": "敏感信息的明文传输",
          "problem_type_id": "CWE-319",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 sf1-ttcdn-tos.pstatp.com 及 4 条接口 URL。",
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
            "actual": "命中 sf1-ttcdn-tos.pstatp.com，累计 10 次引用，来源 classes.dex, classes2.dex。",
            "evidence_refs": [
              "evidence/endpoint-06-sf1-ttcdn-tos.pstatp.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 sf1-ttcdn-tos.pstatp.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=n/a，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-06-sf1-ttcdn-tos.pstatp.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置明文后台地址 sf1-ttcdn-tos.pstatp.com（unknown），4 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 4 条；路径 4 条；来源 classes.dex, classes2.dex",
          "name": "sf1-ttcdn-tos.pstatp.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 rc.snssdk.com（分类：unknown，评分 85），共 4 条完整 URL、3 条接口路径。来源文件：classes3.dex。地址形态：HTTPS。URL 示例：https://rc.snssdk.com | https://rc.snssdk.com/punish/toast_info | https://rc.snssdk.com/verify/get_info | https://rc.snssdk.com/verify/verify_info。接口路径：/punish/toast_info、/verify/get_info、/verify/verify_info。 动态探活：地址可达，HTTP 404，Server=Tengine，TLS=valid，延迟 223ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 rc.snssdk.com（分类：unknown，评分 85），共 4 条完整 URL、3 条接口路径。来源文件：classes3.dex。地址形态：HTTPS。URL 示例：https://rc.snssdk.com | https://rc.snssdk.com/punish/toast_info | https://rc.snssdk.com/verify/get_info | https://rc.snssdk.com/verify/verify_info。接口路径：/punish/toast_info、/verify/get_info、/verify/verify_info。 动态探活：地址可达，HTTP 404，Server=Tengine，TLS=valid，延迟 223ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 rc.snssdk.com 及 4 条接口 URL。",
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
            "actual": "命中 rc.snssdk.com，累计 8 次引用，来源 classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-07-rc.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 rc.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 404，TLS=valid，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-07-rc.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 rc.snssdk.com（unknown），4 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 4 条；路径 3 条；来源 classes3.dex",
          "name": "rc.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 schedulers.io（分类：unknown，评分 85），共 0 条完整 URL、0 条接口路径。来源文件：classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：(仅域名，无完整 URL)。接口路径：未提取到路径。 动态探活：地址可达，HTTP 200，Server=未知，TLS=valid，延迟 2608ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 schedulers.io（分类：unknown，评分 85），共 0 条完整 URL、0 条接口路径。来源文件：classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：(仅域名，无完整 URL)。接口路径：未提取到路径。 动态探活：地址可达，HTTP 200，Server=未知，TLS=valid，延迟 2608ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 schedulers.io 及 0 条接口 URL。",
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
            "actual": "命中 schedulers.io，累计 14 次引用，来源 classes2.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-08-schedulers.io.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 schedulers.io 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=None",
            "evidence_refs": [
              "evidence/endpoint-08-schedulers.io.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 schedulers.io（unknown），0 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 0 条；路径 0 条；来源 classes2.dex, classes3.dex",
          "name": "schedulers.io",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
            ]
          }
        }
      ],
      "aliases": [],
      "database_specific": {
        "confidence": "high",
        "cwe_ids": [
          "CWE-319"
        ],
        "detection_method": "hybrid",
        "risk_level": "medium",
        "submission": {
          "tool_chain": [
            "REA 6.5.0",
            "JADX 0.7.1",
            "apk-endpoints 1.0"
          ]
        },
        "vuln_class": "不安全网络通信"
      },
      "details": "从样本中静态提取到后台地址 restapi.amap.com（分类：api，评分 83），共 4 条完整 URL、2 条接口路径。来源文件：classes3.dex。地址形态：明文 HTTP。URL 示例：http://restapi.amap.com | http://restapi.amap.com/v3/geocode/regeo | http://restapi.amap.com/v3/iasdkauth | https://restapi.amap.com/v3/iasdkauth。接口路径：/v3/geocode/regeo、/v3/iasdkauth。 动态探活：地址可达，HTTP 200，Server=Tengine，TLS=n/a，延迟 100ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
      "impact_scope": {
        "affected_devices_or_os": null,
        "affected_versions": [],
        "cia": {
          "A": "N",
          "C": "H",
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
              "value": "从样本中静态提取到后台地址 restapi.amap.com（分类：api，评分 83），共 4 条完整 URL、2 条接口路径。来源文件：classes3.dex。地址形态：明文 HTTP。URL 示例：http://restapi.amap.com | http://restapi.amap.com/v3/geocode/regeo | http://restapi.amap.com/v3/iasdkauth | https://restapi.amap.com/v3/iasdkauth。接口路径：/v3/geocode/regeo、/v3/iasdkauth。 动态探活：地址可达，HTTP 200，Server=Tengine，TLS=n/a，延迟 100ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
            },
            {
              "lang": "en",
              "value": "Cleartext Transmission of Sensitive Information"
            }
          ],
          "name": "敏感信息的明文传输",
          "problem_type_id": "CWE-319",
          "source_name": "CWE"
        }
      ],
      "related": [],
      "reproduction": {
        "actual_result": "可直接从样本中提取 restapi.amap.com 及 4 条接口 URL。",
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
            "actual": "命中 restapi.amap.com，累计 8 次引用，来源 classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-09-restapi.amap.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 restapi.amap.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=n/a，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-09-restapi.amap.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score_value": 5.9,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置明文后台地址 restapi.amap.com（api），4 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 api；URL 4 条；路径 2 条；来源 classes3.dex",
          "name": "restapi.amap.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 i.snssdk.com（分类：unknown，评分 82），共 6 条完整 URL、5 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://i.snssdk.com | https://i.snssdk.com/ies/antispam/verification_code/get_pic_code/ | https://i.snssdk.com/ies/antispam/verification_code/verify_pic_code/ | https://i.snssdk.com/inspect/aegis/client/page/。接口路径：/ies/antispam/verification_code/get_pic_code/、/ies/antispam/verification_code/verify_pic_code/、/inspect/aegis/client/page/、/monitor/collect/c/core_dump_collect、/monitor/collect/c/rapheal_file_collect。 动态探活：当前不可达（TimeoutError: The read operation timed out），可能已下线、需要内网或需特定 Host 头。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 i.snssdk.com（分类：unknown，评分 82），共 6 条完整 URL、5 条接口路径。来源文件：classes.dex, classes2.dex, classes3.dex。地址形态：HTTPS。URL 示例：https://i.snssdk.com | https://i.snssdk.com/ies/antispam/verification_code/get_pic_code/ | https://i.snssdk.com/ies/antispam/verification_code/verify_pic_code/ | https://i.snssdk.com/inspect/aegis/client/page/。接口路径：/ies/antispam/verification_code/get_pic_code/、/ies/antispam/verification_code/verify_pic_code/、/inspect/aegis/client/page/、/monitor/collect/c/core_dump_collect、/monitor/collect/（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 i.snssdk.com 及 6 条接口 URL。",
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
            "actual": "命中 i.snssdk.com，累计 18 次引用，来源 classes.dex, classes2.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-10-i.snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 i.snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "不可达：TimeoutError: The read operation timed out",
            "evidence_refs": [
              "evidence/endpoint-10-i.snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 i.snssdk.com（unknown），6 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 6 条；路径 5 条；来源 classes.dex, classes2.dex, classes3.dex",
          "name": "i.snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 snssdk.com（分类：unknown，评分 75），共 0 条完整 URL、0 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：HTTPS。URL 示例：(仅域名，无完整 URL)。接口路径：未提取到路径。 动态探活：地址可达，HTTP 200，Server=Tengine，TLS=valid，延迟 657ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 snssdk.com（分类：unknown，评分 75），共 0 条完整 URL、0 条接口路径。来源文件：classes.dex, classes3.dex。地址形态：HTTPS。URL 示例：(仅域名，无完整 URL)。接口路径：未提取到路径。 动态探活：地址可达，HTTP 200，Server=Tengine，TLS=valid，延迟 657ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 snssdk.com 及 0 条接口 URL。",
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
            "actual": "命中 snssdk.com，累计 9 次引用，来源 classes.dex, classes3.dex。",
            "evidence_refs": [
              "evidence/endpoint-11-snssdk.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 snssdk.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 200，TLS=valid，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-11-snssdk.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 snssdk.com（unknown），0 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 0 条；路径 0 条；来源 classes.dex, classes3.dex",
          "name": "snssdk.com",
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
              "apk_md5": "0b105ce24b7a3ff232dc4a054994532d",
              "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
              "package_format": "APK",
              "package_name_source": "APK 清单 package 属性",
              "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
              "version_code": "160301",
              "version_name": "16.3.0",
              "version_source": "APK 清单 versionName/versionCode"
            },
            "name": "com.ss.android.ugc.aweme",
            "versions": [
              "16.3.0(160301)"
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
      "details": "从样本中静态提取到后台地址 unpkg.pstatp.com（分类：unknown，评分 71），共 2 条完整 URL、2 条接口路径。来源文件：classes.dex。地址形态：HTTPS。URL 示例：https://unpkg.pstatp.com/byted/secsdk-captcha/2.1.15/build/index.html | https://unpkg.pstatp.com/byted/secsdk-mobile-original/1.8.1/build/index.html。接口路径：/byted/secsdk-captcha/2.1.15/build/index.html、/byted/secsdk-mobile-original/1.8.1/build/index.。 动态探活：地址可达，HTTP 403，Server=Tengine，TLS=valid，延迟 351ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。",
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
              "value": "从样本中静态提取到后台地址 unpkg.pstatp.com（分类：unknown，评分 71），共 2 条完整 URL、2 条接口路径。来源文件：classes.dex。地址形态：HTTPS。URL 示例：https://unpkg.pstatp.com/byted/secsdk-captcha/2.1.15/build/index.html | https://unpkg.pstatp.com/byted/secsdk-mobile-original/1.8.1/build/index.html。接口路径：/byted/secsdk-captcha/2.1.15/build/index.html、/byted/secsdk-mobile-original/1.8.1/build/index.。 动态探活：地址可达，HTTP 403，Server=Tengine，TLS=valid，延迟 351ms。 未验证边界：静态提取只能证明地址被写入客户端，无法证明其为生产在用、也无法确认鉴权方式与数据敏感度；若未启用探活或探活失败，需结合抓包确认。（判定置信度：high）"
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
        "actual_result": "可直接从样本中提取 unpkg.pstatp.com 及 2 条接口 URL。",
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
            "actual": "命中 unpkg.pstatp.com，累计 5 次引用，来源 classes.dex。",
            "evidence_refs": [
              "evidence/endpoint-12-unpkg.pstatp.com.txt"
            ],
            "expected": "获得客户端内置的全部网络地址候选。",
            "seq": 1
          },
          {
            "action": "对 unpkg.pstatp.com 发起一次 HEAD 探活（User-Agent 伪装为 Android 客户端，6s 超时）。",
            "actual": "HTTP 403，TLS=valid，Server=Tengine",
            "evidence_refs": [
              "evidence/endpoint-12-unpkg.pstatp.com.txt"
            ],
            "expected": "仅用于确认地址是否真实存在，不进行任何业务请求。",
            "seq": 2
          }
        ]
      },
      "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
      "schema_version": "1.0.0",
      "severity": [
        {
          "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:N",
          "score_value": 0,
          "source": "team-self",
          "type": "CVSS_V3.1"
        }
      ],
      "summary": "客户端内置后台地址 unpkg.pstatp.com（unknown），2 个接口 URL 可直接提取",
      "upstream": [],
      "vulnerability_location": {
        "component": {
          "extra": "分类 unknown；URL 2 条；路径 2 条；来源 classes.dex",
          "name": "unpkg.pstatp.com",
          "type": "other"
        },
        "entry_point": "network-remote",
        "layer": "network"
      }
    }
  ],
  "report": {
    "apk_sha256": "f0dd10eb671dfd71d15a430707965403e6250bacaf8ba05ee018bb155c5d48c8",
    "class_count": 18555,
    "endpoints": {
      "api_admin": 22,
      "categories": {
        "admin": 1,
        "api": 21,
        "unknown": 70,
        "website": 8
      },
      "primary": {
        "alive": true,
        "base_urls": [
          "https://aweme.snssdk.com"
        ],
        "brand": true,
        "category": "api",
        "host": "aweme.snssdk.com",
        "http_status": 404,
        "path_count": 22,
        "paths_sample": [
          "/aweme/v1/multiple/login/unbind/",
          "/aweme/v1/notice/",
          "/aweme/v1/urge/history/list/",
          "/aweme/v1/urge/list/",
          "/aweme/v1/user/set/settings/",
          "/aweme/v1/user/settings/",
          "/aweme/v2/ads/entry/check"
        ],
        "reason": "域名携带产品品牌词，且域名标签命中 接口 关键字；探活可达（HTTP 404）",
        "scheme": "https",
        "score": 234,
        "server": "Tengine",
        "tls": "valid",
        "url_count": 24
      },
      "probed": true,
      "top": [
        {
          "alive": true,
          "category": "api",
          "host": "aweme.snssdk.com",
          "http_status": 404,
          "score": 234
        },
        {
          "alive": true,
          "category": "api",
          "host": "mon.snssdk.com",
          "http_status": 504,
          "score": 147
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "log.snssdk.com",
          "http_status": 504,
          "score": 122
        },
        {
          "alive": true,
          "category": "api",
          "host": "open.e.189.cn",
          "http_status": 200,
          "score": 118
        },
        {
          "alive": false,
          "category": "api",
          "host": "security.snssdk.com",
          "http_status": null,
          "score": 101
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "sf1-ttcdn-tos.pstatp.com",
          "http_status": 404,
          "score": 97
        },
        {
          "alive": true,
          "category": "website",
          "host": "www.douyin.com",
          "http_status": 200,
          "score": 90
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "rc.snssdk.com",
          "http_status": 404,
          "score": 85
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "schedulers.io",
          "http_status": 200,
          "score": 85
        },
        {
          "alive": true,
          "category": "api",
          "host": "restapi.amap.com",
          "http_status": 200,
          "score": 83
        },
        {
          "alive": false,
          "category": "unknown",
          "host": "i.snssdk.com",
          "http_status": null,
          "score": 82
        },
        {
          "alive": true,
          "category": "unknown",
          "host": "snssdk.com",
          "http_status": 200,
          "score": 75
        }
      ],
      "total": 100
    },
    "finding_count": 21,
    "findings": [
      {
        "confidence": "high",
        "cwe": [
          "CWE-926"
        ],
        "file": "findings/01-cwe-926-组件导出暴露.json",
        "risk_level": "medium",
        "score": 5.1,
        "summary": "导出的 Activity（18 个）未设置权限保护，任意应用可调用",
        "vuln_class": "组件导出暴露"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-926"
        ],
        "file": "findings/02-cwe-926-组件导出暴露.json",
        "risk_level": "medium",
        "score": 5.1,
        "summary": "导出的 Service（28 个）未设置权限保护，任意应用可调用",
        "vuln_class": "组件导出暴露"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-926"
        ],
        "file": "findings/03-cwe-926-组件导出暴露.json",
        "risk_level": "medium",
        "score": 5.1,
        "summary": "导出的 BroadcastReceiver（19 个）未设置权限保护，任意应用可调用",
        "vuln_class": "组件导出暴露"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-926"
        ],
        "file": "findings/04-cwe-926-组件导出暴露.json",
        "risk_level": "medium",
        "score": 6.2,
        "summary": "导出的 ContentProvider（1 个）未设置权限保护，任意应用可访问其数据",
        "vuln_class": "组件导出暴露"
      },
      {
        "confidence": "medium",
        "cwe": [
          "CWE-939"
        ],
        "file": "findings/05-cwe-939-DeepLink漏洞.json",
        "risk_level": "medium",
        "score": 4.4,
        "summary": "导出 Activity 注册了 4 条自定义 URL Scheme，未校验来源即可被任意应用或浏览器唤起",
        "vuln_class": "DeepLink漏洞"
      },
      {
        "confidence": "medium",
        "cwe": [
          "CWE-319"
        ],
        "file": "findings/06-cwe-319-不安全网络通信.json",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "应用允许 HTTP 明文传输，且存在硬编码的 http:// 接口地址，流量可被中间人窃听或篡改",
        "vuln_class": "不安全网络通信"
      },
      {
        "confidence": "low",
        "cwe": [
          "CWE-749"
        ],
        "file": "findings/07-cwe-749-JSBridge漏洞.json",
        "risk_level": "medium",
        "score": 4.2,
        "summary": "应用通过 addJavascriptInterface 向 WebView 注入 Java 对象，若加载不可信页面可被调用",
        "vuln_class": "JSBridge漏洞"
      },
      {
        "confidence": "low",
        "cwe": [
          "CWE-295"
        ],
        "file": "findings/08-cwe-295-证书校验缺陷.json",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "应用覆写了 WebView/HTTP 的证书校验逻辑，存在忽略证书错误、绕过校验的风险",
        "vuln_class": "证书校验缺陷"
      },
      {
        "confidence": "low",
        "cwe": [
          "CWE-327"
        ],
        "file": "findings/09-cwe-327-加密算法误用.json",
        "risk_level": "low",
        "score": 3.7,
        "summary": "应用使用弱加密算法或 ECB 模式（/ECB/, AES/ECB, DES/, DESede），加密数据易被破解",
        "vuln_class": "加密算法误用"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e01-cwe-200-aweme.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 aweme.snssdk.com（api），24 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-319"
        ],
        "file": "findings/e02-cwe-319-mon.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "客户端内置明文后台地址 mon.snssdk.com（api），7 个接口 URL 可直接提取",
        "vuln_class": "不安全网络通信"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e03-cwe-200-log.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 log.snssdk.com（unknown），7 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-319"
        ],
        "file": "findings/e04-cwe-319-open.e.189.cn.json",
        "kind": "endpoint",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "客户端内置明文后台地址 open.e.189.cn（api），4 个接口 URL 可直接提取",
        "vuln_class": "不安全网络通信"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e05-cwe-200-security.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 security.snssdk.com（api），6 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-319"
        ],
        "file": "findings/e06-cwe-319-sf1-ttcdn-tos.pstatp.com.json",
        "kind": "endpoint",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "客户端内置明文后台地址 sf1-ttcdn-tos.pstatp.com（unknown），4 个接口 URL 可直接提取",
        "vuln_class": "不安全网络通信"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e07-cwe-200-rc.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 rc.snssdk.com（unknown），4 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e08-cwe-200-schedulers.io.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 schedulers.io（unknown），0 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-319"
        ],
        "file": "findings/e09-cwe-319-restapi.amap.com.json",
        "kind": "endpoint",
        "risk_level": "medium",
        "score": 5.9,
        "summary": "客户端内置明文后台地址 restapi.amap.com（api），4 个接口 URL 可直接提取",
        "vuln_class": "不安全网络通信"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e10-cwe-200-i.snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 i.snssdk.com（unknown），6 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e11-cwe-200-snssdk.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 snssdk.com（unknown），0 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      },
      {
        "confidence": "high",
        "cwe": [
          "CWE-200"
        ],
        "file": "findings/e12-cwe-200-unpkg.pstatp.com.json",
        "kind": "endpoint",
        "risk_level": "info",
        "score": 0,
        "summary": "客户端内置后台地址 unpkg.pstatp.com（unknown），2 个接口 URL 可直接提取",
        "vuln_class": "硬编码敏感信息"
      }
    ],
    "min_sdk": "17",
    "package_name": "com.ss.android.ugc.aweme",
    "sample_file": "0b105ce24b7a3ff232dc4a054994532d.apk",
    "sample_id": "0b105ce24b7a3ff232dc4a054994532d",
    "target_sdk": "26",
    "version_code": "160301",
    "version_name": "16.3.0"
  }
}
