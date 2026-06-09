from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import os

today = datetime.now()
weekday = today.weekday()

# Category Config

topic_files = {
0: ("LINUX COMMANDS", "data/linux.txt", (0, 255, 180)),
1: ("AWS TIPS", "data/aws.txt", (255, 165, 0)),
2: ("WINDOWS SERVER", "data/windows.txt", (0, 170, 255)),
3: ("NETWORKING TIPS", "data/networking.txt", (180, 0, 255)),
4: ("SECURITY TIPS", "data/security.txt", (255, 80, 80)),
5: ("DEVOPS TIPS", "data/devops.txt", (255, 215, 0)),
}

title, file_path, accent = topic_files.get(
weekday,
("DEVOPS TIPS", "data/devops.txt", (255, 215, 0))
)

# Read Tips

with open(file_path, "r", encoding="utf-8") as f:
tips = [x.strip() for x in f.readlines() if x.strip()]

selected = random.sample(tips, min(5, len(tips)))

# LinkedIn Portrait Size

WIDTH = 1080
HEIGHT = 1350

# Background

img = Image.new("RGB", (WIDTH, HEIGHT), (10, 15, 25))
draw = ImageDraw.Draw(img)

# Fonts

try:
title_font = ImageFont.truetype(
"DejaVuSans-Bold.ttf",
48
)

```
heading_font = ImageFont.truetype(
    "DejaVuSans-Bold.ttf",
    28
)

command_font = ImageFont.truetype(
    "DejaVuSans.ttf",
    24
)

desc_font = ImageFont.truetype(
    "DejaVuSans.ttf",
    20
)

footer_font = ImageFont.truetype(
    "DejaVuSans.ttf",
    22
)
```

except:
title_font = ImageFont.load_default()
heading_font = ImageFont.load_default()
command_font = ImageFont.load_default()
desc_font = ImageFont.load_default()
footer_font = ImageFont.load_default()

# Header Background

draw.rectangle(
[(0, 0), (WIDTH, 190)],
fill=(18, 25, 40)
)

draw.text(
(40, 20),
f"TOP 5 {title}",
fill=accent,
font=heading_font
)

draw.text(
(40, 60),
"EVERY SYSADMIN SHOULD KNOW",
fill=(255, 255, 255),
font=title_font
)

draw.text(
(40, 130),
"Daily Infrastructure & Cloud Learning",
fill=(180, 180, 180),
font=footer_font
)

# Cards

y = 220

for idx, tip in enumerate(selected, start=1):

```
parts = tip.split("|")

heading = parts[0] if len(parts) > 0 else ""
command = parts[1] if len(parts) > 1 else ""
description = parts[2] if len(parts) > 2 else ""

card_height = 155

# Card
draw.rounded_rectangle(
    [(40, y), (1040, y + card_height)],
    radius=18,
    fill=(18, 25, 40),
    outline=accent,
    width=2
)

# Number Box
draw.rounded_rectangle(
    [(55, y + 15), (140, y + 140)],
    radius=12,
    fill=(30, 50, 80)
)

draw.text(
    (78, y + 50),
    f"{idx:02}",
    fill=(255, 255, 255),
    font=heading_font
)

# Heading
draw.text(
    (170, y + 15),
    heading[:45],
    fill=(255, 255, 255),
    font=heading_font
)

# Command Box
draw.rounded_rectangle(
    [(170, y + 55), (700, y + 100)],
    radius=8,
    fill=(35, 45, 70)
)

draw.text(
    (185, y + 65),
    command[:50],
    fill=(255, 215, 0),
    font=command_font
)

draw.text(
    (170, y + 115),
    description[:80],
    fill=(180, 180, 180),
    font=desc_font
)

y += 175
```

# Benefits Section

draw.line(
[(40, 1120), (1040, 1120)],
fill=accent,
width=2
)

benefits = [
"✓ Troubleshooting",
"✓ Monitoring",
"✓ Performance",
"✓ Production Ready"
]

x = 50

for item in benefits:
draw.text(
(x, 1145),
item,
fill=accent,
font=footer_font
)
x += 245

# Footer

draw.line(
[(40, 1220), (1040, 1220)],
fill=accent,
width=2
)

draw.text(
(50, 1250),
"Deepak A",
fill=(255, 255, 255),
font=heading_font
)

draw.text(
(50, 1285),
"IT Infrastructure Specialist | Cloud Engineer",
fill=(180, 180, 180),
font=footer_font
)

# Save Banner

os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today.strftime('%Y-%m-%d')}.png"

img.save(output_file)

print(f"Banner generated successfully: {output_file}")
