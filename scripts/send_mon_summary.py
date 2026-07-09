#!/usr/bin/env python3

"""
Parse Ansible PLAY RECAP and send a monitoring summary to Discord.

Author: Joyce Mwangi
Project: Network Automation with Ansible
"""

import json
import os
import re
import urllib.request
import urllib.error

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK:
    raise SystemExit("DISCORD_WEBHOOK_URL environment variable not found.")

OUTPUT_FILE = "ansible-output.txt"

failed = []
unreachable = []
successful = []

critical_alerts = 0
major_alerts = 0
warning_alerts = 0

if not os.path.exists(OUTPUT_FILE):
    raise SystemExit(f"{OUTPUT_FILE} not found.")

with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    text = line.lower()

    if "severity" not in text:
        continue

    if "critical" in text:
        critical_alerts += 1
    elif "major" in text:
        major_alerts += 1
    elif "warning" in text:
        warning_alerts += 1

play_recap = False

for line in lines:

    if "PLAY RECAP" in line:
        play_recap = True
        continue

    if not play_recap:
        continue

    m = re.match(
        r"^(\S+)\s+:.*ok=(\d+).*changed=(\d+).*unreachable=(\d+).*failed=(\d+)",
        line.strip()
    )

    if not m:
        continue

    host = m.group(1)
    unreachable_count = int(m.group(4))
    failed_count = int(m.group(5))

for line in lines:
    text = line.upper()

    if "CRITICAL -" in text:
        critical_alerts += 1
    elif "MAJOR -" in text:
        major_alerts += 1
    elif "WARNING -" in text:
        warning_alerts += 1

total = len(failed) + len(unreachable) + len(successful)

total_alerts = critical_alerts + major_alerts + warning_alerts

repo = os.getenv("GITHUB_REPOSITORY", "Local Run")
workflow = os.getenv("GITHUB_WORKFLOW", "Ansible Health Monitoring")
run_id = os.getenv("GITHUB_RUN_ID")

if run_id:
    workflow_url = f"https://github.com/{repo}/actions/runs/{run_id}"
else:
    workflow_url = "Local Execution"

message = f"""🚨 **INFRASTRUCTURE MONITORING REPORT**

**Repository**
{repo}

**Workflow**
{workflow}

----------------------------------------

**Total Hosts:** {total}
✅ Healthy: {len(successful)}
❌ Failed: {len(failed)}
⚠️ Unreachable: {len(unreachable)}

----------------------------------------

📊 **Alert Severity Summary**

🚨 Total Alerts: {total_alerts}

🔴 Critical: {critical_alerts}
🟠 Major: {major_alerts}
🟡 Warning: {warning_alerts}

"""

if failed:
    message += "**❌ Failed Hosts**\n"
    for host in failed:
        message += f"• {host}\n"
    message += "\n"

if unreachable:
    message += "**⚠️ Unreachable Hosts**\n"
    for host in unreachable:
        message += f"• {host}\n"
    message += "\n"

message += f"""----------------------------------------

🔗 Workflow Run
{workflow_url}
"""

payload = {
    "username": "Ansible Health Monitor",
    "content": message
}

req = urllib.request.Request(
    WEBHOOK,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "User-Agent": "AnsibleHealthMonitor/1.0"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        print(f"Discord notification sent ({response.status})")

except urllib.error.HTTPError as e:
    print("Discord HTTP Error:", e.code)
    print(e.read().decode())
    raise
