from datetime import datetime
import os
import random

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

weekday = today.weekday()

files = {
    0: "data/linux.txt",
    1: "data/aws.txt",
    2: "data/windows.txt",
    3: "data/networking.txt",
    4: "data/security.txt",
    5: "data/devops.txt"
}

source_file = files.get(weekday, "data/devops.txt")

with open(source_file, "r", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]

tip = random.choice(lines)

parts = tip.split("|")

title = parts[0]
command = parts[1]
description = parts[2]

content = f"""
TITLE:
{title}

COMMAND:
{command}

DESCRIPTION:
{description}

#Linux #AWS #Cloud #DevOps #SystemAdministrator
"""

os.makedirs("captions", exist_ok=True)

with open(f"captions/{date_str}.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Content generated successfully")
