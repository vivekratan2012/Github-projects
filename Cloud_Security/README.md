

---

# SC-200 SOC Analyst Portfolio

## Overview

Welcome to my Microsoft Sentinel SOC Analyst portfolio, showcasing hands-on detection engineering, threat hunting, and automation aligned with the SC-200 certification objectives.
This repository demonstrates real-world skills that protect enterprise environments by detecting, investigating, and automating responses to security threats.

---

## Core Capabilities Demonstrated

| Skill Area             | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| **KQL Threat Hunting** | Advanced queries targeting authentication, endpoint, and email threats                 |
| **Analytics Rules**    | Scheduled, production-grade Microsoft Sentinel detection rules                         |
| **SOAR Playbooks**     | Automated workflows for incident enrichment, assignment, notification, and remediation |
| **Incident Response**  | End-to-end detection and response thinking, aligned to MITRE ATT&CK                    |
| **Data Sanitization**  | Real-world data sanitized for safe sharing and compliance                              |
| **Best Practices**     | Clear documentation, entity mapping, and alert grouping to reduce noise                |

---

## Portfolio Structure

```
sc200-soc-portfolio/
├── README.md                     # This portfolio overview
├── kql/                          # Kusto Query Language threat hunting queries
│   ├── authentication/
│   │   ├── brute_force.kql
│   │   └── impossible_travel.kql
│   ├── endpoint/
│   │   └── suspicious_powershell.kql
│   ├── email/
│   │   └── phishing_clicks.kql
│   └── sample-data/
│       └── windows_4625_bruteforce_sanitized.csv
├── sentinel-rules/               # Production-ready Sentinel analytic rule JSON and docs
│   ├── Azure_Sentinel_analytic_rule.json
│   └── README.md
├── playbooks/                    # SOAR automation playbooks JSON templates
│   ├── enrich-ip-incident.json
│   ├── auto-assign-incident.json
│   ├── notify-teams.json
│   ├── disable-user.json
│   └── README.md
```

---

## 1️⃣ KQL Threat Hunting Queries

**Location:** `/kql`

This folder contains detection queries focused on key SOC use cases:

* **Brute Force Authentication**
  Detects rapid, repeated failed logon attempts targeting the same user account and host.

* **Impossible Travel**
  Flags suspicious user logons from geographically improbable locations within a short timeframe.

* **Suspicious PowerShell**
  Hunts for potentially malicious PowerShell commands indicating post-exploitation activity.

* **Phishing Email Clicks**
  Identifies users clicking multiple suspicious email URLs within a defined time window.

---

## 2️⃣ Microsoft Sentinel Analytics Rules

**Location:** `/sentinel-rules`

* Includes a **production-grade brute-force detection rule JSON** ready for deployment.
* Configured with appropriate aggregation, alert grouping, and entity mapping.
* Validated with sanitized, real-world sample data from a Sentinel sandbox.
* Fully documented for clarity and maintainability.

---

## 3️⃣ SOAR Automation Playbooks

**Location:** `/playbooks`

* JSON templates automating incident enrichment, assignment, notification, and remediation.
* Examples include IP threat intel enrichment, auto-assignment by severity, Teams notifications, and user disablement.
* Demonstrates ability to build scalable, repeatable SOC processes leveraging Microsoft Sentinel Logic Apps.

---

## 4️⃣ How This Portfolio Maps to SC-200 Skills

| Skill                            | Covered |
| -------------------------------- | ------- |
| KQL / Threat Hunting             | ✅       |
| Sentinel Analytics Rules         | ✅       |
| SOAR Playbook Automation         | ✅       |
| Defender XDR Awareness           | ✅       |
| Incident Response Best Practices | ✅       |
| MITRE ATT&CK Mapping             | ✅       |

---

## Sample Validation: Brute-Force Detection

The brute-force analytics rule was validated using a sanitized dataset of failed Windows logons (`EventID 4625`) showing:

* Multiple failed authentication attempts for the same user
* Network logon type and NTLM authentication package
* Multiple failures within a 5-minute window, triggering the rule as expected

This demonstrates understanding of Windows security telemetry and the ability to craft effective detections.

---

## Why This Portfolio Stands Out

* **Realistic Data & Scenarios:** Uses sanitized, realistic event logs, not synthetic or toy data
* **Clear Documentation:** Each component is well explained with rationale and context
* **Technical Rigor:** Aggregated, thresholded queries with entity enrichment
* **End-to-End Detections:** From query through rule to automated playbook response
* **Alignment to Industry Frameworks:** MITRE ATT&CK and SC-200 mapped

---

## Final Note for Recruiters & Hiring Managers

This portfolio showcases proven SOC Analyst II skills focused on:

* Rapid threat detection using KQL
* Building scalable Sentinel analytics rules
* Automating response workflows
* Clear communication through documentation

All content is safe for sharing — sanitized, tenant-agnostic, and deployable — demonstrating production readiness.

