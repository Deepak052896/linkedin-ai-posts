import json
import os
from datetime import date

CURRENT_POST = "state/current_post.json"
CAPTION_DIR = "captions"

os.makedirs(CAPTION_DIR, exist_ok=True)

with open(CURRENT_POST, "r", encoding="utf-8") as f:
post = json.load(f)

category = post.get("category", "").lower()
title = post.get("title", "Tech Tips")
commands = post.get("commands", [])

hashtags = {
"aws": "#aws #cloud #devops #amazonwebservices #cloudcomputing",
"azure": "#azure #microsoftazure #cloud #devops #cloudcomputing",
"linux": "#linux #sysadmin #opensource #devops #linuxadmin",
"windows": "#windowsserver #microsoft #sysadmin #itadmin #devops",
"security": "#cybersecurity #infosec #security #devsecops #cloudsecurity",
"networking": "#networking #networkengineer #ccna #infrastructure #it",
"devops": "#devops #automation #sre #cloud #infrastructure"
}

caption = f"🚀 {title}\n\n"

for index, cmd in enumerate(commands, start=1):
caption += f"✅ {cmd['title']}\n"
caption += f"   {cmd['description']}\n\n"

caption += "💡 Which tip do you use most often in your environment?\n\n"
caption += hashtags.get(category, "#technology #it #cloud")

today = date.today().strftime("%Y-%m-%d")

output_file = os.path.join(
CAPTION_DIR,
f"{today}.txt"
)

with open(output_file, "w", encoding="utf-8") as f:
f.write(caption)

print(f"Caption generated: {output_file}")
