# 🔐 Linux OS Hardening Automation Framework

A production-grade Python-based Linux OS hardening automation framework that securely connects to multiple Linux servers over SSH and applies security hardening aligned with CIS benchmark recommendations.

Designed for:
- DevSecOps Engineers
- SRE Teams
- Security Engineers
- Infrastructure Teams
- Cloud Operations
- Enterprise Linux Administration

---

## 🚀 Features

✅ Automated Linux OS Hardening  
✅ Multi-server Parallel Execution  
✅ SSH-Based Secure Automation  
✅ CIS Benchmark Inspired Controls  
✅ Sysctl Kernel Hardening  
✅ SSH Security Enforcement  
✅ Fail2Ban Protection  
✅ Firewall Automation  
✅ Auditd Configuration  
✅ Logging & Reporting  
✅ Modular Production Architecture  
✅ Backup & Rollback Ready  
✅ YAML Inventory Driven  
✅ Extensible Security Modules

---

### 🏗️ Project Architecture

```text
                          ┌──────────────────────────┐
                          │     Control Node         │
                          │  Python Automation Host  │
                          └─────────────┬────────────┘
                                        │
                             Secure SSH Connections
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
┌───────▼────────┐              ┌────────▼────────┐             ┌────────▼────────┐
│ Target Server 1 │             │ Target Server 2 │             │ Target Server 3 │
│ Ubuntu/CentOS   │             │ RHEL/Debian     │             │ Rocky/AlmaLinux │
└─────────────────┘             └─────────────────┘             └─────────────────┘
```

---

#### 📂 Project Structure

```text
linux-hardening-framework/
│
├── harden.py
│
├── inventory/
│   └── hosts.yaml
│
├── policies/
│   └── cis_baseline.yaml
│
├── modules/
│   ├── ssh_hardening.py
│   ├── firewall.py
│   ├── sysctl_hardening.py
│   ├── fail2ban.py
│   ├── auditing.py
│   ├── password_policy.py
│   └── package_security.py
│
├── logs/
│   └── hardening.log
│
├── backups/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ How It Works

---

### Step 1 — Inventory Loading

The framework dynamically loads all target Linux servers from the inventory file.

### File:
```text
inventory/hosts.yaml
```

### Example:

```yaml
servers:
  - host: 192.168.1.10
    username: ubuntu
    key: /home/admin/.ssh/id_rsa

  - host: 192.168.1.11
    username: ubuntu
    key: /home/admin/.ssh/id_rsa
```

## ✅ Production Benefit

- Centralized infrastructure management
- Easy server onboarding
- Environment segregation (Dev/UAT/Prod)
- Supports large-scale infrastructure

---

# Step 2 — Secure SSH Authentication

The framework securely connects to Linux servers using SSH private key authentication.

### Security Mechanisms

- Encrypted SSH transport
- No plaintext passwords
- Key-based authentication
- Connection timeout handling
- Host verification

## ✅ Production Benefit

- Eliminates password exposure
- Prevents brute-force attack vectors
- Enables secure enterprise automation
- Works seamlessly with Bastion hosts

---

# Step 3 — Parallel Multi-Server Execution

The framework uses multithreading to harden multiple servers simultaneously.

### Mechanism Used

```python
ThreadPoolExecutor(max_workers=5)
```

## ✅ Production Benefit

- Faster enterprise deployment
- Reduced maintenance window
- Scales to hundreds of servers
- Efficient infrastructure operations

---

# Step 4 — Hardening Policy Execution

Security hardening policies are executed sequentially on each server.

### Security Controls Applied

| Control | Purpose |
|---|---|
| SSH Hardening | Prevent unauthorized access |
| Firewall Configuration | Reduce attack surface |
| Fail2Ban | Prevent brute-force attacks |
| Auditd | Security auditing |
| Sysctl Hardening | Kernel protection |
| Password Policies | Strong authentication |
| Package Updates | Patch vulnerabilities |
| File Permissions | Protect sensitive files |

---

# 🧩 Production Modules Explained

---

# 1️⃣ `harden.py`

## Purpose

Main orchestration engine of the framework.

## Responsibilities

- Reads inventory
- Establishes SSH connections
- Executes hardening modules
- Handles multithreading
- Generates reports
- Captures logs

## Production Importance

Acts as the centralized automation controller.

---

# 2️⃣ `inventory/`

## Purpose

Stores all target server definitions.

## Why Important in Production

- Environment-wise segregation
- Dynamic infrastructure scaling
- Easy onboarding/offboarding
- Cloud instance tracking

---

# 3️⃣ `policies/`

## Purpose

Contains YAML-based hardening policies.

## Example

```yaml
disable_root_login: true
enable_firewall: true
install_fail2ban: true
```

## Production Importance

- Policy-as-Code
- Compliance standardization
- Environment-specific hardening
- Easier audits

---

# 4️⃣ `modules/`

Contains reusable hardening components.

---

## 🔐 `ssh_hardening.py`

### Responsibilities

- Disable root login
- Disable password authentication
- Enforce secure ciphers
- Configure idle timeout

### Production Benefit

Reduces SSH attack vectors.

---

## 🔥 `firewall.py`

### Responsibilities

- Enable UFW/Firewalld
- Allow required ports
- Block unauthorized traffic

### Production Benefit

Minimizes exposed attack surface.

---

## ⚙️ `sysctl_hardening.py`

### Responsibilities

- Kernel parameter tuning
- Disable IP forwarding
- Prevent SYN flood attacks

### Production Benefit

Provides kernel-level protection.

---

## 🚫 `fail2ban.py`

### Responsibilities

- Detect malicious login attempts
- Ban suspicious IPs

### Production Benefit

Prevents brute-force attacks.

---

## 📋 `auditing.py`

### Responsibilities

- Configure auditd
- Track critical system events

### Production Benefit

Supports compliance & forensics.

---

## 🔑 `password_policy.py`

### Responsibilities

- PAM configuration
- Password complexity enforcement
- Password aging policies

### Production Benefit

Improves identity security.

---

## 📦 `package_security.py`

### Responsibilities

- Patch vulnerable packages
- Remove insecure software

### Production Benefit

Reduces known CVEs exposure.

---

# 5️⃣ `logs/`

## Purpose

Stores execution and security logs.

## Example

```text
logs/hardening.log
```

## Production Importance

- Troubleshooting
- Audit evidence
- Compliance tracking
- Change monitoring

---

# 6️⃣ `backups/`

## Purpose

Stores backup copies before configuration changes.

## Production Importance

- Rollback support
- Disaster recovery
- Safer deployments

---

# 7️⃣ `reports/`

## Purpose

Stores generated compliance reports.

## Example Outputs

- JSON reports
- CSV compliance status
- HTML dashboards

## Production Importance

- Audit readiness
- Security reviews
- Compliance validation

---

# 🔒 Security Controls Implemented

| Category | Controls |
|---|---|
| Authentication | SSH Key Authentication |
| Authorization | Root Login Restriction |
| Network Security | Firewall Rules |
| Intrusion Prevention | Fail2Ban |
| Kernel Security | Sysctl Hardening |
| Logging | Auditd |
| File Security | Permission Hardening |
| Patch Management | OS Updates |
| Compliance | CIS Alignment |

---

# 🏢 Production Considerations

---

# ✅ Idempotency

The framework should avoid duplicate changes.

Example:
- Avoid duplicate sysctl entries
- Validate existing SSH configuration

---

# ✅ Rollback Mechanism

Before modifying critical files:

```bash
cp /etc/ssh/sshd_config backups/
```

Prevents accidental production outages.

---

# ✅ OS Detection

Automatically detect:
- Ubuntu
- Debian
- RHEL
- CentOS
- Rocky Linux
- AlmaLinux

And use:
- apt
- yum
- dnf

accordingly.

---

# ✅ Compliance Alignment

Supports:
- CIS Benchmarks
- NIST
- STIG
- ISO 27001

---

# ✅ Secrets Management

Never hardcode:
- SSH keys
- Passwords
- Tokens

Recommended integrations:
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault

---

# ✅ Dry Run Support

```bash
python harden.py --dry-run
```

Allows validation before production rollout.

---

# ✅ Failure Isolation

If one server fails:
- Remaining servers continue execution
- Errors are logged separately

---

# ✅ Centralized Monitoring

Recommended integrations:
- Splunk
- ELK Stack
- Grafana Loki
- Wazuh

---

# 📊 Enterprise Deployment Flow

```text
Git Repository
      ↓
CI/CD Pipeline
      ↓
Security Validation
      ↓
Hardening Execution
      ↓
Compliance Scan
      ↓
SIEM Monitoring
      ↓
Audit Reporting
```

---

# ☁️ Cloud & DevSecOps Integration

This framework can integrate with:

| Technology | Usage |
|---|---|
| Jenkins | CI/CD |
| GitHub Actions | Automation |
| Terraform | Infrastructure Provisioning |
| Ansible | Configuration Management |
| Docker | Containerized Execution |
| Kubernetes | Cluster Hardening |
| AWS Systems Manager | Fleet Management |

---

# 🚀 Future Enhancements

- OpenSCAP Integration
- CIS Compliance Scoring
- HTML Dashboard
- Kubernetes Hardening
- Docker Security Benchmarking
- Agent-Based Architecture
- REST API Management
- Centralized Secrets Manager
- AI-Based Risk Scoring

---

# ▶️ Execution

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Framework

```bash
python harden.py
```

---

# ⚠️ Important Warning

Always test hardening changes in:
- Development
- QA
- Staging

before production rollout.

Incorrect hardening may:
- Break SSH access
- Block applications
- Interrupt services
- Cause system instability

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Linux Security Automation Framework  
Built for Enterprise DevSecOps & Production Security Operations