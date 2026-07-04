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

</p>
---

## Overview
Ansible-based automation framework for performing automated health checks on routers and switches across enterprise and ISP network environments.

This project gathers operational data, parses device output, and helps proactively identify network issues before they impact service availability or stability.

---

## Key Features
- Automated network device health checks (routers & switches)
- Configuration-free operational data collection
- Structured parsing of device outputs
- Early detection of network anomalies
- Multi-vendor ready automation approach
- Role-based Ansible architecture

---

## Architecture
- Ansible Playbooks for orchestration
- Ansible Roles for reusable automation logic
- Cisco IOS modules for network data collection
- Structured YAML-based configuration

---

## Project Structure
```
network-automation-ansible/
│
├── health_check.yml           # Main orchestrator playbook (hybrid monitoring)
├── ansible.cfg                # Ansible configuration
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
├── .gitattributes             # GitHub language detection
│
├── inventory/
│   └── hosts.ini              # Network & multi-cloud inventory
├── group_vars/
│   └── all.yml                # Global monitoring variables
├── host_vars/
│   └── devices.yml            # Infrastructure metadata
│
├── roles/
│   └── health_checks/
│       ├── tasks/
│       │   └── main.yml       # Hybrid monitoring logic
│       ├── defaults/
│       │   └── main.yml       # Default role variables
│       ├── vars/
│       │   └── main.yml       # Role-specific variables
│       └── handlers/
│           └── main.yml       # Event-driven alert handlers
│
├── templates/                 # Reserved for future report templates
└── logs/                      # Runtime logs (.gitkeep, .gitignore)
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

## Use Cases
- Network health monitoring
- Pre-incident detection
- ISP and enterprise network automation
- Configuration validation workflows
- Operational visibility improvement

---

## Future Enhancements
- Integration with SIEM for alerts
- Export results to Prometheus / Grafana
- Multi-vendor support (Juniper, Arista, Fortinet)
- Slack / Email alerting system
- CI/CD pipeline integration for network automation

---

## Author
**Joyce Mwangi**  
Network & Cloud Infrastructure Engineer  
GitHub: https://github.com/joycemwangi  
LinkedIn: https://linkedin.com/in/wanjajoyce


