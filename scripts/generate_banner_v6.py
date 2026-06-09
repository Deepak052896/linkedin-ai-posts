from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import os

today = datetime.now()
weekday = today.weekday()

TOPICS = {
    0: ("LINUX COMMANDS", "data/linux.txt", (0, 255, 150)),
    1: ("AWS TIPS", "data/aws.txt", (255, 180, 0)),
    2: ("WINDOWS SERVER", "data/windows.txt", (0, 180, 255)),
    3: ("NETWORKING TIPS", "data/networking.txt", (180, 0, 255)),
    4: ("SECURITY TIPS", "data/security.txt", (255, 80, 80)),
    5: ("DEVOPS TIPS", "data/devops.txt", (255, 215, 0)),
}

title, file_path, accent = TOPICS.get(
    weekday,
    ("DEVOPS TIPS", "data/devops.txt", (255, 215, 0))
)

# Read tips
with open(file_path, "r", encoding="utf-8") as f:
    tips = [x.strip() for x in f.readlines() if x.strip()]

selected = random.sample(tips, min(5, len(tips)))

# Canvas
WIDTH = 1080
HEIGHT = 1350

img = Image.new("RGB", (WIDTH, HEIGHT), (5, 10, 25))
draw = ImageDraw.Draw(img)

# Fonts
try:
    big_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 72)
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 34)
    heading_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    command_font = ImageFont.truetype("DejaVuSans.ttf", 22)
    small_font = ImageFont.truetype("DejaVuSans.ttf", 18)
except:
    big_font = ImageFont.load_default()
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Header
draw.rectangle((0, 0, WIDTH, 220), fill=(10, 20, 45))

draw.text(
    (40, 20),
    title,
    fill=accent,
    font=big_font
)

draw.text(
    (40, 120),
    "Daily Infrastructure & Cloud Learning",
    fill=(220, 220, 220),
    font=title_font
)

draw.line((0, 200, WIDTH, 200), fill=accent, width=2)

# Center Title
draw.text(
    (220, 230),
    "TOP 5 COMMANDS",
    fill=(255, 255, 255),
    font=big_font
)

draw.text(
    (240, 320),
    "EVERY SYSADMIN SHOULD KNOW",
    fill=accent,
    font=title_font
)

# Cards
card_y = 400

for idx, tip in enumerate(selected[:5], start=1):

    parts = tip.split("|")

    heading = parts[0] if len(parts) > 0 else ""
    command = parts[1] if len(parts) > 1 else ""
    desc = parts[2] if len(parts) > 2 else ""

    draw.rounded_rectangle(
        (35, card_y, 1045, card_y + 120),
        radius=18,
        outline=accent,
        width=2,
        fill=(8, 15, 35)
    )

    # Number box
    draw.rounded_rectangle(
        (45, card_y + 10, 125, card_y + 110),
        radius=12,
        fill=(25, 45, 75)
    )

    draw.text(
        (62, card_y + 35),
        f"{idx:02}",
        fill="white",
        font=title_font
    )

    draw.text(
        (160, card_y + 12),
        heading[:40],
        fill="white",
        font=heading_font
    )

    draw.rounded_rectangle(
        (160, card_y + 45, 650, card_y + 82),
        radius=8,
        fill=(35, 50, 80)
    )

    draw.text(
        (175, card_y + 52),
        command[:40],
        fill=(255, 220, 0),
        font=command_font
    )

    draw.text(
        (700, card_y + 45),
        desc[:35],
        fill=(220, 220, 220),
        font=small_font
    )

    card_y += 140

# Benefits
draw.rounded_rectangle(
    (35, 1110, 1045, 1210),
    radius=18,
    outline=accent,
    width=2
)

benefits = [
    "TROUBLESHOOTING",
    "MONITORING",
    "PERFORMANCE",
    "PRODUCTION READY"
]

x = 55

for item in benefits:
    draw.text(
        (x, 1148),
        item,
        fill=accent,
        font=heading_font
    )
    x += 245

# Footer
draw.line((35, 1260, 1045, 1260), fill=accent, width=2)

draw.text(
    (50, 1280),
    "Deepak A",
    fill="white",
    font=title_font
)

draw.text(
    (260, 1288),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(200, 200, 200),
    font=command_font
)

# Save
os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today.strftime('%Y-%m-%d')}.png"

img.save(output_file)

print(f"Banner generated: {output_file}")
