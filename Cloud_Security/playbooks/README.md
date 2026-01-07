
---

# Microsoft Sentinel SOAR Playbooks

This folder contains **production-ready SOAR (Security Orchestration, Automation, and Response) playbooks** implemented with **Microsoft Sentinel Logic Apps**.
These playbooks showcase advanced SOC automation and incident response capabilities, demonstrating end-to-end security operations aligned with the SC-200 certification and SOC Analyst II responsibilities.

---

## 🚀 Purpose of This Folder

The goal of these playbooks is to:

* **Enrich incidents with context**: Automatically gather threat intelligence and relevant metadata for IPs, accounts, and hosts.
* **Reduce response time**: Streamline triage and assignment to ensure timely analyst attention.
* **Enable safe automation**: Implement automation workflows while preserving human oversight and reducing risk.
* **Demonstrate SOC maturity**: Show workflow orchestration, best practices, and thoughtful automation design.

---

## 📂 Folder Structure

```
/playbooks/
├── enrich-ip-incident.json       # Adds threat intel to incident IPs
├── auto-assign-incident.json     # Automatically assigns incidents to SOC tiers
├── notify-teams.json             # Sends alerts to Teams for high-severity incidents
├── disable-user.json             # Controlled remediation for compromised accounts
└── README.md                     # This document
```

---

## 1️⃣ Enrich IP Incident

**Objective:**
Automatically enrich incidents that contain IP entities with threat intelligence and contextual information.

**Key Features:**

* Extracts IP entities from Sentinel incidents
* Queries Microsoft Defender Threat Intelligence or external threat feeds
* Annotates incidents with IP reputation, ASN, and geolocation
* Preserves analyst oversight — no automatic blocking

**Impact for SOC Teams:**

* Provides **context immediately upon incident creation**
* Reduces investigation time
* Demonstrates ability to combine **KQL detections with automated response**

---

## 2️⃣ Auto-Assign Incident

**Objective:**
Ensure incidents are **assigned to the correct analyst or team** based on severity and category.

**Key Features:**

* Auto-assigns **High severity** incidents to Tier 2 SOC analysts
* Routes **Medium/Low severity** incidents to Tier 1 queue
* Includes incident metadata for transparency and auditability

**Impact for SOC Teams:**

* Eliminates unowned incidents
* Enforces **SOC workflow discipline**
* Demonstrates understanding of **incident prioritization and escalation**

---

## 3️⃣ Notify Teams

**Objective:**
Instantly alert SOC staff when critical incidents occur.

**Key Features:**

* Conditions on **Severity = High**
* Sends rich notifications to Microsoft Teams channel
* Provides actionable details for rapid analyst response

**Impact for SOC Teams:**

* Improves **mean time to acknowledge (MTTA)** for critical incidents
* Shows ability to **integrate Sentinel with collaboration tools**
* Demonstrates SOC communication best practices

---

## 4️⃣ Disable User (Controlled Remediation)

**Objective:**
Automate user account disablement in a **safe, controlled manner**.

**Key Features:**

* Triggered **manually or conditionally**
* Disables user only after validation
* Preserves human-in-the-loop approval

**Impact for SOC Teams:**

* Showcases **judgment and risk-awareness**
* Illustrates ability to **connect detection → investigation → response**
* Demonstrates **SOC II-level operational thinking**

---

## 🔹 Design Principles

All playbooks in this folder follow **SOC best practices**:

| Principle                    | Implementation                                             |
| ---------------------------- | ---------------------------------------------------------- |
| **Human-in-the-loop**        | Manual approval for remediation; automated enrichment only |
| **Scalable automation**      | Generic connectors for IP, account, and Teams              |
| **Alert context enrichment** | Entities mapped to full names, IPs, hosts                  |
| **Safety first**             | No destructive actions without validation                  |
| **Audit-ready**              | All actions logged in Sentinel incidents                   |

---