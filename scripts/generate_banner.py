from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import os

today = datetime.now()

weekday = today.weekday()

topic_files = {
    0: ("LINUX COMMANDS", "data/linux.txt"),
    1: ("AWS TIPS", "data/aws.txt"),
    2: ("WINDOWS SERVER", "data/windows.txt"),
    3: ("NETWORKING TIPS", "data/networking.txt"),
    4: ("SECURITY TIPS", "data/security.txt"),
    5: ("DEVOPS TIPS", "data/devops.txt"),
}

title, file_path = topic_files.get(
    weekday,
    ("DEVOPS TIPS", "data/devops.txt")
)

with open(file_path, "r", encoding="utf-8") as f:
    tips = [x.strip() for x in f.readlines() if x.strip()]

selected = random.sample(tips, min(5, len(tips)))

width = 1200
height = 1200

img = Image.new("RGB", (width, height), (10, 15, 25))
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf", 70
    )
    tip_font = ImageFont.truetype(
        "DejaVuSans.ttf", 34
    )
    footer_font = ImageFont.truetype(
        "DejaVuSans.ttf", 28
    )
except:
    title_font = ImageFont.load_default()
    tip_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()

# Header
draw.rectangle(
    [(0, 0), (width, 140)],
    fill=(20, 30, 50)
)

draw.text(
    (50, 35),
    title,
    fill=(0, 255, 180),
    font=title_font
)

# Tips
y = 220

for idx, tip in enumerate(selected, start=1):

    parts = tip.split("|")

    heading = parts[0]

    desc = ""

    if len(parts) >= 3:
        desc = parts[2]

    draw.rounded_rectangle(
        [(50, y), (1150, y + 120)],
        radius=15,
        outline=(0, 255, 180),
        width=2
    )

    draw.text(
        (80, y + 15),
        f"{idx}. {heading}",
        fill=(255, 255, 255),
        font=tip_font
    )

    draw.text(
        (80, y + 60),
        desc[:90],
        fill=(180, 180, 180),
        font=footer_font
    )

    y += 150

# Footer
draw.line(
    [(50, 1080), (1150, 1080)],
    fill=(0, 255, 180),
    width=2
)

draw.text(
    (50, 1100),
    "Deepak A",
    fill=(255, 255, 255),
    font=footer_font
)

draw.text(
    (220, 1100),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(180, 180, 180),
    font=footer_font
)

os.makedirs("banners", exist_ok=True)

output = f"banners/{today.strftime('%Y-%m-%d')}.png"

img.save(output)

print("Banner generated:", output)
