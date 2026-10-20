{
  "findings": [
    {
      "affected": [
        {
          "package": {
            "ecosystem": "Android-APK",
            "ecosystem_specific": {
              "apk_md5": "541ec3e08aa913ce5cfc2e7c272b0cdd",
              "apk_sha256": "7f8a31834b0d2199ac344c5f135764e1bcaa7a4447909a171f0d7b941baf38b3",
              "min_sdk": "21",
              "package_format": "APK",
              "package_name_source": "aapt2 dump badging（JADX 解析失败，加固/资源混淆包）",
              "sample_file": "541ec3e08aa913ce5cfc2e7c272b0cdd.apk",
              "target_sdk": "34",
              "version_code": "17",
              "version_name": "1.0.0",
              "version_source": "aapt2 dump badging（JADX 解析失败，加固/资源混淆包）"
            },
            "name": "com.boeamjcj.dudnywiw",
            "versions": [
              "1.0.0(17)"
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
      "details": "在 dex 字符串表与资源中匹配到 1 类凭据：Google API Key×1。根因是将密钥/口令以字面量形式固化在客户端（CWE-798）。证据示例：Google API Key=AIza********3Nyw（完整值见证据文件）。APK 可被任何人反编译，硬编码凭据等同于公开。触发前提：攻击者持有样本即可离线提取，无需运行应用。未验证边界：未确认这些凭据是否仍在有效期内、权限范围多大，也未调用对应云服务验证其可用性。（CWE 在线核对未完成，名称取自本地映射。）",
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
              "value": "在 dex 字符串表与资源中匹配到 1 类凭据：Google API Key×1。根因是将密钥/口令以字面量形式固化在客户端（CWE-798）。证据示例：Google API Key=AIza********3Nyw（完整值见证据文件）。APK 可被任何人反编译，硬编码凭据等同于公开。触发前提：攻击者持有样本即可离线提取，无需运行应用。未验证边界：未确认这些凭据是否仍在有效期内、权限范围多大，也未调用对应云服务验证其可用性。（判定置信度：medium）"
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
            "actual": "提取到 125888 条字符串，匹配 1 类凭据特征。",
            "evidence_refs": [
              "evidence/hardcoded-secrets.txt"
            ],
            "expected": "敏感凭据不应以明文出现在客户端。",
            "seq": 1
          }
        ]
      },
      "sample_id": "541ec3e08aa913ce5cfc2e7c272b0cdd",
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
    }
  ],
  "report": {
    "apk_sha256": "7f8a31834b0d2199ac344c5f135764e1bcaa7a4447909a171f0d7b941baf38b3",
    "class_count": 3,
    "finding_count": 1,
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
      }
    ],
    "min_sdk": "21",
    "package_name": "com.boeamjcj.dudnywiw",
    "sample_file": "541ec3e08aa913ce5cfc2e7c272b0cdd.apk",
    "sample_id": "541ec3e08aa913ce5cfc2e7c272b0cdd",
    "target_sdk": "34",
    "version_code": "17",
    "version_name": "1.0.0"
  }
}
