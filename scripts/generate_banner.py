from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

today = datetime.now().strftime("%Y-%m-%d")

caption_file = f"captions/{today}.txt"

with open(caption_file, "r", encoding="utf-8") as f:
    content = f.read()

title = "TECH TIPS"
command = ""
description = ""

for line in content.splitlines():

    if line.startswith("TITLE:"):
        title = line.replace("TITLE:", "").strip()

    elif line.startswith("COMMAND:"):
        command = line.replace("COMMAND:", "").strip()

    elif line.startswith("DESCRIPTION:"):
        description = line.replace("DESCRIPTION:", "").strip()

width = 1080
height = 1350

img = Image.new("RGB", (width, height), (5, 12, 28))
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        58
    )

    heading_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        36
    )

    cmd_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        30
    )

    footer_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        24
    )

except:
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    cmd_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()

# Header
draw.rectangle(
    [(0,0),(1080,140)],
    fill=(15,25,55)
)

draw.text(
    (40,35),
    "🐧 LINUX COMMANDS",
    fill=(0,255,180),
    font=title_font
)

draw.text(
    (40,95),
    "Daily Infrastructure & Cloud Learning",
    fill=(180,180,180),
    font=footer_font
)

# Main Card
draw.rounded_rectangle(
    [(40,190),(1040,540)],
    radius=25,
    outline=(0,255,180),
    width=3,
    fill=(0,10,30)
)

draw.text(
    (70,220),
    title,
    fill=(255,255,255),
    font=heading_font
)

draw.rounded_rectangle(
    [(70,300),(700,345)],
    radius=8,
    fill=(25,45,75)
)

draw.text(
    (85,305),
    command,
    fill=(255,215,0),
    font=cmd_font
)

draw.text(
    (70,390),
    description,
    fill=(200,200,200),
    font=cmd_font
)

# Benefits Section
draw.text(
    (40,620),
    "WHY THIS COMMAND?",
    fill=(0,255,180),
    font=heading_font
)

benefits = [
    "✔ Useful for troubleshooting",
    "✔ Saves administration time",
    "✔ Commonly used in production",
    "✔ Essential for Linux admins"
]

y = 690

for item in benefits:
    draw.text(
        (60,y),
        item,
        fill=(240,240,240),
        font=cmd_font
    )
    y += 65

# Skills Footer
draw.line(
    [(40,1120),(1040,1120)],
    fill=(0,255,180),
    width=2
)

draw.text(
    (40,1160),
    "Deepak A",
    fill=(255,255,255),
    font=heading_font
)

draw.text(
    (250,1165),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(180,180,180),
    font=footer_font
)

draw.text(
    (40,1230),
    "Linux • AWS • Azure • Windows Server • DevOps",
    fill=(120,120,120),
    font=footer_font
)

os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today}.png"

img.save(output_file)

print(f"Banner generated: {output_file}")
