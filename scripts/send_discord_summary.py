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

if not os.path.exists(OUTPUT_FILE):
    raise SystemExit(f"{OUTPUT_FILE} not found.")

with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

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

    if failed_count > 0:
        failed.append(host)
    elif unreachable_count > 0:
        unreachable.append(host)
    else:
        successful.append(host)

total = len(failed) + len(unreachable) + len(successful)

# -------------------------------------------------
# TEMPORARY DEBUG PAYLOAD
# -------------------------------------------------

message = f"""
🚨 Infrastructure Monitoring Report

Total Hosts : {total}
Healthy     : {len(successful)}
Failed      : {len(failed)}
Unreachable : {len(unreachable)}

Repository:
{os.getenv('GITHUB_REPOSITORY', 'Local Run')}

Workflow:
{os.getenv('GITHUB_WORKFLOW', 'Ansible Health Monitoring')}
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
    print("====================================")
    print("DISCORD HTTP ERROR")
    print("====================================")
    print("Status :", e.code)
    print("Reason :", e.reason)

    try:
        print(e.read().decode())
    except Exception:
        pass

    raise
