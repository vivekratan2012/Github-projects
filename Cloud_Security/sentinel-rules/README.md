
# Brute-Force Authentication Detection Analytics Rule (Microsoft Sentinel)

## Overview

This analytics rule detects potential **brute-force authentication attacks** by identifying multiple failed Windows logon attempts within a short time window.
It is designed to reduce noise while reliably surfacing credential attack behavior commonly seen during initial access attempts.

The rule was developed and validated in a **Microsoft Sentinel sandbox environment provided by Cloud Academy**, using intentionally generated Windows Security telemetry.

---

## Detection Use Case

Brute-force attacks attempt to gain unauthorized access by repeatedly guessing passwords for a valid account.
In Windows environments, these attempts are recorded as **Event ID 4625 – An account failed to log on**.

This rule focuses on:

* Network-based logon attempts
* NTLM authentication failures
* Rapid, repeated failures against the same account

---

## Data Source

| Source       | Details         |
| ------------ | --------------- |
| Log Table    | `SecurityEvent` |
| Event ID     | `4625`          |
| Logon Type   | `3` (Network)   |
| Auth Package | NTLM            |

---

## Detection Logic (KQL)

```kql
SecurityEvent
| where EventID == 4625
| where LogonType == 3
| where AuthenticationPackageName == "NTLM"
| where Account !endswith "$"
| summarize FailedAttempts = count()
    by Account, Computer, IpAddress,
       AuthenticationPackageName,
       LogonType,
       bin(TimeGenerated, 5m)
| where FailedAttempts >= 5
| extend
    AccountEntity = Account,
    HostEntity = Computer,
    IPEntity = IpAddress
```

### Logic Summary

* Aggregates failed logons in **5-minute windows**
* Triggers when **5 or more failures** occur
* Filters out machine accounts
* Extracts user, host, and IP entities for investigation

---

## Rule Configuration

| Setting           | Value                  |
| ----------------- | ---------------------- |
| Query Frequency   | 5 minutes              |
| Lookup Window     | 30 minutes             |
| Threshold         | ≥ 5 failed attempts    |
| Severity          | Medium                 |
| Incident Creation | Enabled                |
| Alert Grouping    | Enabled (entity-based) |

Alert grouping ensures multiple related failures are combined into a **single incident**, preventing alert fatigue.

---

## Sample Data & Validation

A sanitized dataset is included to demonstrate and validate the detection logic:

```
/kql/sample-data/windows_4625_bruteforce_sanitized.csv
```

### Observed Behavior in Sample Data

* 6 failed logon attempts
* Same user account
* Same host and source IP
* Occurred within ~15 seconds
* NTLM network authentication failures

### Validation Outcome

The sample data reliably triggers the analytics rule under the configured schedule and thresholds, confirming that the detection logic aligns with real-world brute-force behavior.

---

## MITRE ATT&CK Mapping

| Tactic               | Technique           |
| -------------------- | ------------------- |
| Initial Access       | T1110 – Brute Force |
| Credential Access    | T1110 – Brute Force |
| Privilege Escalation | T1110 – Brute Force |

---

## Sandbox Environment Notes

* Detection was developed and tested in a **Sentinel sandbox environment**
* No production or customer data was used
* All included datasets are **fully sanitized**
* No tenant-specific identifiers are exposed

This mirrors standard detection engineering workflows, where analytics rules are validated in non-production environments before deployment.

---

## Why This Detection Matters

* Uses correct Windows Security telemetry (4625)
* Applies aggregation to reduce false positives
* Provides rich entity context for analysts
* Reflects real SOC detection engineering practices
* Easily extensible with SOAR automation

---

## Possible Enhancements

* Add exclusions for known VPN or jump-box IP ranges
* Apply different thresholds for externally facing systems
* Attach SOAR playbooks for enrichment or account containment

---

**Author’s Note:**
This rule demonstrates practical detection engineering skills aligned with Microsoft SC-200 objectives, including KQL development, analytics rule configuration, validation, and documentation.

---
