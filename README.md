# Hybrid Infrastructure Health Monitoring with Ansible

<p align="center">
  <img src="assets/ansible-banner.png" alt="Network Automation with Ansible">
</p>

<p align="center">
  <strong>Automated Network Health Monitoring for Enterprise & ISP Infrastructure</strong>
</p>

<p align="center">

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Cisco IOS](https://img.shields.io/badge/Cisco-IOS-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=FF9900)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white)

</p>
---

## Overview

Ansible-based hybrid infrastructure monitoring framework that automates health checks across enterprise networks and multi-cloud environments.

The framework collects operational metrics, evaluates configurable thresholds, and generates structured alerts with severity classification, operational impact, possible causes, and recommended remediation actions.

---

## Key Features

- Hybrid infrastructure health monitoring
- Automated health checks for Cisco routers and switches
- Multi-cloud monitoring (AWS, Azure, GCP, OCI, Private Cloud)
- Connectivity validation and health reporting
- Threshold-based alerting with severity classification
- Actionable operational guidance and remediation recommendations
- Modular role-based Ansible architecture
- Enterprise-style observability alerts
- Production and demonstration monitoring modes
- Extensible framework for enterprise and ISP environments

---

## Core Components

- Ansible Playbooks for orchestration
- Ansible Roles for reusable automation logic
- Cisco IOS modules for network data collection
- Structured YAML-based configuration

---

## Monitoring Workflow

The monitoring workflow follows a structured operational pipeline:

```
Collect Metrics
      │
      ▼
Evaluate Thresholds
      │
      ▼
Determine Severity
      │
      ▼
Generate Alert
      │
      ▼
Publish Alert
      │
      ▼
Provide Operational Guidance
```

The workflow supports both demonstration mode using simulated metrics and production mode using live Cisco IOS devices.

## Alert Design Philosophy

Alerts are designed to provide actionable operational information rather than simply reporting threshold violations.

Each alert follows a consistent structure that helps network engineers quickly assess and respond to incidents.

| Stage | Purpose |
|--------|---------|
| **What happened?** | Identify the affected metric. |
| **How severe is it?** | Classify the alert severity. |
| **What is the impact?** | Describe the operational impact. |
| **What caused it?** | Highlight likely root causes. |
| **What should be done?** | Recommend investigation and remediation steps. |

This approach helps reduce Mean Time to Detect (MTTD) and supports faster incident response by providing actionable context with every alert.

## Supported Alerts

The monitoring role currently detects and classifies:

- Connectivity Failures
- Network Device Health
- CPU Utilization
- Memory Utilization
- Network Latency
- Monitoring Platform Failures

Each alert includes:

- Severity classification
- Configurable thresholds
- Amount exceeded
- Operational impact
- Possible causes
- Recommended remediation
- Timestamp
- Host information
- Monitoring mode

## Project Structure
```
hybrid-infrastructure-monitoring-ansible/
├── .github/
│   └── workflows/
│       └── ansible-health-check.yml      # GitHub Actions CI monitoring workflow
├── health_check.yml                      # Main orchestrator playbook (hybrid monitoring)
├── ansible.cfg                           # Ansible configuration
├── README.md                             # Project documentation
├── LICENSE                               # MIT License
├── .gitattributes                        # GitHub language detection
├── .gitignore                            # Ignore logs, secrets, vault files and temporary files
├── assets/
│   └── ansible-banner.png                # README banner
├── inventory/
│   └── hosts.ini                         # Infrastructure inventory (hosts & groups)
├── group_vars/
│   ├── all.yml                           # Global monitoring policy
│   ├── network.yml                       # Cisco IOS monitoring configuration
│   ├── aws_cloud.yml                     # AWS monitoring configuration
│   ├── azure_cloud.yml                   # Azure monitoring configuration
│   ├── gcp_cloud.yml                     # Google Cloud monitoring configuration
│   ├── oci_cloud.yml                     # Oracle Cloud monitoring configuration
│   └── private_cloud.yml                 # Private cloud monitoring configuration
├── roles/
│   └── health_checks/
│       ├── tasks/
│       │   ├── main.yml                  # Main hybrid monitoring workflow
│       │   ├── log_monitoring_alert.yml  # Generates monitoring alerts from detected events
│       │   └── send_monitoring_alert.yml # Publishes monitoring alerts
│       ├── defaults/
│       │   └── main.yml                  # Default monitoring thresholds
│       ├── vars/
│       │   └── main.yml                  # Role-specific variables
│       └── handlers/
│           └── main.yml                  # Event-driven handlers
├── scripts/
│   └── send_mon_summary.py               # Sends monitoring execution summary
├── templates/                            # Future notification and report templates
└── logs/
    ├── .gitkeep
    └── .gitignore
```

---

## Example Use Case

Automated health check workflow:

1. Connect to network devices via Ansible  
2. Collect operational state using IOS facts modules  
3. Extract key device information:
   - Hostname
   - OS version
   - Hardware model
   - Serial number  
4. Evaluate operational thresholds
5. Generate structured monitoring alerts
6. Publish alerts to the configured notification platform
---

## Sample Output

🚨 CRITICAL – HIGH CPU UTILIZATION

Host: R1-EDGE-01
CPU Usage: 95%
Threshold: 65%

Impact:
• Reduced control plane responsiveness

Possible Causes:
• High routing protocol activity

Recommended Action:
• Verify BGP/OSPF neighbor stability

---

## Technologies Used

- Ansible
- Python
- YAML
- Cisco IOS Automation
- GitHub Actions (CI/CD)
- Discord Webhooks
- Ansible Vault
- Infrastructure Monitoring
- Network Automation

---

## Security

This project follows infrastructure automation security best practices by supporting **Ansible Vault** for protecting sensitive credentials.
Sensitive credentials are encrypted using Ansible Vault and excluded from version control through .gitignore to support secure infrastructure automation.

### Protected Configuration
- Cisco device credentials
- Enable passwords
- API tokens
- Cloud authentication secrets

Sensitive variables can be encrypted using Ansible Vault before deployment:

```bash
ansible-vault encrypt group_vars/network.yml
```
---

## Use Cases
- Network health monitoring
- Pre-incident detection
- ISP and enterprise network automation
- Configuration validation workflows
- Operational visibility improvement

---

## Future Enhancements

- Slack, Microsoft Teams and Email notification channels
- Multi-vendor support (Juniper, Arista, Fortinet and Nokia)
- Prometheus and Grafana integration
- SNMP and streaming telemetry
- Historical metric storage and trend analysis
- ServiceNow and Jira integration
- SIEM integration
- AI-assisted anomaly detection
- Interactive operational dashboards
- Compliance and configuration validation pipelines
---

## Author
**Joyce Mwangi**  
Network & Cloud Infrastructure Engineer  
GitHub: https://github.com/joycemwangi  
LinkedIn: https://linkedin.com/in/wanjajoyce
