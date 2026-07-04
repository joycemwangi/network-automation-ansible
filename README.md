# Network Automation with Ansible

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
├── health_check.yml              # Main playbook
├── roles/
│   └── health_checks/
│       ├── tasks/
│       │   └── main.yml
│       ├── defaults/
│       ├── vars/
│       └── handlers/
├── inventory (hosts.ini)
├── ansible.cfg
└── README.md
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

