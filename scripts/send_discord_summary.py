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

if failed:
    color = 15158332      # Red
elif unreachable:
    color = 16776960      # Yellow
else:
    color = 3066993       # Green

description = []

if failed:
    description.append("## ❌ Failed")
    description.extend(f"• {h}" for h in failed)
    description.append("")

if unreachable:
    description.append("## ⚠️ Unreachable")
    description.extend(f"• {h}" for h in unreachable)
    description.append("")

if successful:
    description.append("## ✅ Healthy")
    description.extend(f"• {h}" for h in successful)

embed = {
    "title": "Infrastructure Monitoring Report",
    "description": "\n".join(description),
    "color": color,
    "fields": [
        {
            "name": "Total Hosts",
            "value": str(total),
            "inline": True
        },
        {
            "name": "Healthy",
            "value": str(len(successful)),
            "inline": True
        },
        {
            "name": "Failed",
            "value": str(len(failed)),
            "inline": True
        },
        {
            "name": "Unreachable",
            "value": str(len(unreachable)),
            "inline": True
        },
        {
            "name": "Repository",
            "value": os.getenv("GITHUB_REPOSITORY", "Local Run"),
            "inline": False
        },
        {
            "name": "Workflow",
            "value": os.getenv("GITHUB_WORKFLOW", "Ansible Health Check"),
            "inline": False
        }
    ]
}

payload = {
    "username": "Ansible Health Monitor",
    "embeds": [embed]
}

req = urllib.request.Request(
    WEBHOOK,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)

with urllib.request.urlopen(req) as response:
    print(f"Discord notification sent ({response.status})")
