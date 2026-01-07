
---

# KQL Queries for SOC Threat Hunting

This folder contains a collection of advanced **Kusto Query Language (KQL)** queries used for proactive threat hunting and detection within Microsoft Sentinel.
Each query targets key SOC use cases and demonstrates real-world detection techniques aligned with Microsoft SC-200 certification objectives.

---

## Folder Structure

```
/kql/
├── authentication/         # Authentication-related queries
│   ├── brute_force.kql    # Detect rapid failed logons (brute force)
│   └── impossible_travel.kql  # Detect impossible travel logins
├── endpoint/               # Endpoint activity queries
│   └── suspicious_powershell.kql  # Detect suspicious PowerShell activity
├── email/                  # Email-related threat detection
│   └── phishing_clicks.kql  # Detect phishing email link clicks
└── sample-data/            # Sanitized sample logs for validation
    └── windows_4625_bruteforce_sanitized.csv
```

---

## Queries Overview

### 1. Brute Force Authentication

Detects multiple failed Windows logon attempts (`EventID 4625`) from the same account and host within a short time frame, indicating possible brute force attacks.

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
| extend AccountEntity = Account, HostEntity = Computer, IPEntity = IpAddress
```

---

### 2. Impossible Travel Detection

Identifies suspicious logins from geographically distant locations within an unrealistically short time frame, a common sign of account compromise.

```kql
SecurityEvent
| where EventID == 4624
| where Account !endswith "$"
| extend PreviousLogon = prev(TimeGenerated) over (partition by Account order by TimeGenerated)
| extend TimeDiff = datetime_diff('hour', TimeGenerated, PreviousLogon)
| where TimeDiff < 2
| extend PreviousLocation = prev(IpAddress) over (partition by Account order by TimeGenerated)
| where IpAddress != PreviousLocation
| extend AccountEntity = Account, IPEntity = IpAddress
```

---

### 3. Suspicious PowerShell Activity

Hunts for potentially malicious PowerShell command executions often used by attackers during post-exploitation.

```kql
SecurityEvent
| where EventID == 4104
| where CommandLine contains_cs "Invoke-WebRequest" or CommandLine contains_cs "IEX"
| extend HostEntity = Computer, AccountEntity = Account
| project TimeGenerated, Computer, Account, CommandLine
```

---

### 4. Phishing Email Clicks

Detects multiple clicks on suspicious URLs by the same recipient, which may indicate phishing engagement.

```kql
EmailEvents
| where NetworkMessageId != ""
| where EventType == "Click"
| summarize ClickCount = count() by RecipientEmailAddress, UrlClicked, bin(TimeGenerated, 1h)
| where ClickCount > 5
| extend EmailEntity = RecipientEmailAddress
```

---

## Sample Data for Validation

The `/kql/sample-data/windows_4625_bruteforce_sanitized.csv` file contains sanitized Windows Security Event ID 4625 records that demonstrate brute force activity.
This dataset can be used to test and validate the brute force detection query logic.

---


