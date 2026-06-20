import json
import os
from datetime import date
from PIL import Image, ImageDraw, ImageFont

CURRENT_POST = "state/current_post.json"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "banners"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load selected post
with open(CURRENT_POST, "r", encoding="utf-8") as f:
    post = json.load(f)

category = post["category"].lower()
commands = post["commands"]

# Template file
template_file = os.path.join(
    TEMPLATE_DIR,
    f"{category}.png"
)

if not os.path.exists(template_file):
    raise FileNotFoundError(
        f"Template not found: {template_file}"
    )

# Open image
img = Image.open(template_file).convert("RGBA")
draw = ImageDraw.Draw(img)

# Fonts
try:
    title_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        20
    )

    command_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        24
    )

except Exception:
    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()

# Dynamic positioning
base_y = 430
row_gap = 150

for i, cmd in enumerate(commands[:5]):

    x = 340
    y = base_y + (i * row_gap)

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()

    if len(title) > 30:
        title = title[:30] + "..."

    if len(command) > 28:
        command = command[:28] + "..."

    # Title
    draw.text(
        (x, y),
        title,
        font=title_font,
        fill=(255, 255, 255)
    )

    # Command
    draw.text(
        (x, y + 28),
        command,
        font=command_font,
        fill=(0, 255, 255)
    )

# Save banner
today = date.today().strftime("%Y-%m-%d")

output_file = os.path.join(
    OUTPUT_DIR,
    f"{today}.png"
)

img.save(output_file)

print(f"Banner generated: {output_file}")
print(f"Category: {category}")
print(f"Title: {post['title']}")
