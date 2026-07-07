# Network Automation with Ansible

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

Ansible-based hybrid infrastructure monitoring framework for enterprise and ISP environments.

The project automates health checks across network devices and cloud infrastructure by collecting operational metrics, evaluating configurable thresholds, and generating structured alerts with severity classification, operational impact, possible causes, and recommended remediation actions.

Designed with a modular role-based architecture, it supports demonstration mode for GitHub Actions and production mode for Cisco IOS devices, making it suitable for learning, testing, and real-world network automation.

---

## Key Features

- Automated health checks for Cisco routers and switches
- Hybrid infrastructure monitoring
- Multi-cloud observability (AWS, Azure, GCP, OCI, Private Cloud)
- Connectivity validation and health reporting
- Intelligent threshold-based alerting with severity classification
- Structured operational reporting with actionable remediation guidance
- Role-based Ansible architecture
- Extensible for enterprise and ISP environments
- Enterprise-style observability alerts
- Production-ready monitoring workflow

---

## Architecture
- Ansible Playbooks for orchestration
- Ansible Roles for reusable automation logic
- Cisco IOS modules for network data collection
- Structured YAML-based configuration

---

## Monitoring Workflow

The monitoring workflow follows a structured operational pipeline:

```text
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
Provide Operational Guidance
```

The workflow supports both demonstration mode using simulated metrics and production mode using live Cisco IOS devices.

## Alert Design Philosophy

Alerts are designed to provide actionable operational information rather than simply reporting threshold violations.

Each alert follows a consistent structure that helps network engineers quickly assess and respond to incidents.

| Stage | Purpose |
|--------|---------|
| **What happened?** | Identifies the monitored resource and the metric that exceeded its threshold. |
| **How severe is it?** | Classifies the alert as **Warning**, **Major**, or **Critical** using configurable thresholds. |
| **What is the impact?** | Explains the potential operational or business impact if the issue persists. |
| **What might have caused it?** | Lists common causes to assist with initial diagnosis. |
| **What should the operator do?** | Provides recommended investigation and remediation steps based on operational best practices. |

This approach helps reduce mean time to detect (MTTD) and supports faster incident response by providing actionable context with every alert.

## Supported Alerts

The monitoring role currently detects and classifies:

- CPU Utilization
- Memory Utilization
- Network Latency
- Network Device Health
- Connectivity Failures
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
network-automation-ansible/
│
├── .github/
│   └── workflows/
│       └── ansible-health-check.yml # GitHub Actions CI monitoring workflow
├── health_check.yml                 # Main orchestrator playbook (hybrid monitoring)
├── ansible.cfg                      # Ansible configuration
├── README.md                        # Project documentation
├── LICENSE                          # MIT License
├── .gitattributes                   # GitHub language detection
├── .gitignore                       # Ignore logs, secrets, vault files, temporary files
├── assets/
│   └── ansible-banner.png           # README banner
├── inventory/
│   └── hosts.ini                    # Infrastructure inventory (hosts & groups)
├── group_vars/
│   ├── all.yml                      # Global monitoring policy
│   ├── network.yml                  # Cisco IOS connection settings
│   ├── aws_cloud.yml                # AWS monitoring configuration
│   ├── azure_cloud.yml              # Azure monitoring configuration
│   ├── gcp_cloud.yml                # Google Cloud monitoring configuration
│   ├── oci_cloud.yml                # Oracle Cloud monitoring configuration
│   └── private_cloud.yml            # Private cloud monitoring configuration
├── roles/
│   └── health_checks/
│       ├── tasks/
│       │   ├── main.yml             # Hybrid monitoring and alerting logic
│       │   └── send_monitoring_alert.yml # Sends monitoring alerts
│       ├── defaults/
│       │   └── main.yml             # Default monitoring thresholds
│       ├── vars/
│       │   └── main.yml             # Role-specific variables
│       └── handlers/
│           └── main.yml             # Event-driven alert handlers
├── scripts/
│   └── send_mon_summary.py          # Sends monitoring execution summary
├── templates/                       # Future report and notification templates
└── logs/                            # Runtime execution logs
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
4. Display structured output for validation and monitoring  

---

## Sample Output

Router: R1-EDGE-01
OS Version: IOS-XE 17.x
Model: Cisco ISR 4451-X
Serial Number: FGL2345ABC

---

## Technologies Used
- Ansible
- YAML
- Cisco IOS Automation Modules
- Network Engineering (L2/L3)
- Infrastructure Automation

---

## Security

This project follows infrastructure automation security best practices by supporting **Ansible Vault** for protecting sensitive credentials.

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

- Integration with SIEM platforms for centralized security monitoring and alert correlation
- Export monitoring metrics to Prometheus with visualization in Grafana dashboards
- Multi-vendor support for Juniper, Arista, Fortinet, and Nokia network devices
- Slack, Microsoft Teams, and Email notification channels
- CI/CD pipeline integration for automated network validation and compliance checks
- SNMP and streaming telemetry support for real-time observability
- Historical metric storage and trend analysis
- Automated incident creation with ServiceNow and Jira
- AI-assisted anomaly detection and predictive alerting
- Interactive operational dashboards and reporting

---

## Author
**Joyce Mwangi**  
Network & Cloud Infrastructure Engineer  
GitHub: https://github.com/joycemwangi  
LinkedIn: https://linkedin.com/in/wanjajoyce


