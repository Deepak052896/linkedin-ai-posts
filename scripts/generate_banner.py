from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import os

today = datetime.now()
weekday = today.weekday()

# Day-wise categories
topic_files = {
    0: ("🐧 LINUX COMMANDS", "data/linux.txt"),
    1: ("☁️ AWS TIPS", "data/aws.txt"),
    2: ("🪟 WINDOWS SERVER", "data/windows.txt"),
    3: ("🌐 NETWORKING TIPS", "data/networking.txt"),
    4: ("🛡️ SECURITY TIPS", "data/security.txt"),
    5: ("⚙️ DEVOPS TIPS", "data/devops.txt"),
}

title, file_path = topic_files.get(
    weekday,
    ("⚙️ DEVOPS TIPS", "data/devops.txt")
)

# Read tips
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
        "DejaVuSans-Bold.ttf", 58
    )

    heading_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf", 32
    )

    command_font = ImageFont.truetype(
        "DejaVuSans.ttf", 28
    )

    desc_font = ImageFont.truetype(
        "DejaVuSans.ttf", 24
    )

    footer_font = ImageFont.truetype(
        "DejaVuSans.ttf", 24
    )

except:
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    desc_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()

# Header Background
draw.rectangle(
    [(0, 0), (WIDTH, 140)],
    fill=(20, 30, 50)
)

draw.text(
    (40, 35),
    title,
    fill=(0, 255, 180),
    font=title_font
)

# Subtitle
draw.text(
    (40, 105),
    "Daily Infrastructure & Cloud Learning",
    fill=(180, 180, 180),
    font=footer_font
)

# Tip Cards
y = 190

for idx, tip in enumerate(selected, start=1):

    parts = tip.split("|")

    heading = parts[0] if len(parts) > 0 else ""
    command = parts[1] if len(parts) > 1 else ""
    description = parts[2] if len(parts) > 2 else ""

    card_height = 180

    draw.rounded_rectangle(
        [(40, y), (1040, y + card_height)],
        radius=20,
        outline=(0, 255, 180),
        width=3
    )

    draw.text(
        (70, y + 20),
        f"{idx}. {heading}",
        fill=(255, 255, 255),
        font=heading_font
    )

    # Command Box
    draw.rounded_rectangle(
        [(70, y + 65), (700, y + 110)],
        radius=8,
        fill=(25, 40, 60)
    )

    draw.text(
        (85, y + 75),
        command,
        fill=(255, 215, 0),
        font=command_font
    )

    draw.text(
        (70, y + 125),
        description[:90],
        fill=(180, 180, 180),
        font=desc_font
    )

    y += 210

# Footer Line
draw.line(
    [(40, 1220), (1040, 1220)],
    fill=(0, 255, 180),
    width=2
)

# Branding
draw.text(
    (40, 1250),
    "Deepak A",
    fill=(255, 255, 255),
    font=heading_font
)

draw.text(
    (250, 1255),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(180, 180, 180),
    font=footer_font
)

# Save Banner
os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today.strftime('%Y-%m-%d')}.png"

img.save(output_file)

print(f"Banner generated successfully: {output_file}")
