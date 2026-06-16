# Windows System Security Audit Tool

A lightweight Python script designed to perform automated security auditing and compliance checks on Windows endpoints. It reviews firewall operational states, active listening network ports, and verifies the current execution user context.

## 🚀 Audits Performed
1. **Firewall Verification:** Validates the active status of the Windows Advanced Firewall (`netsh`).
2. **Network Footprint Enumeration:** Captures active TCP listening ports via core subsystem network utilities (`netstat`).
3. **Privilege & Context Check:** Logs current active user identification context (`whoami`).

## 💻 How To Run
Open your Windows Command Prompt (CMD) in the project directory and execute:

```bash
python security_audit.py