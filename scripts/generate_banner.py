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
        26
    )

except Exception:
    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()

# Correct box positions
positions = [
    (320, 430),   # 01
    (320, 580),   # 02
    (320, 730),   # 03
    (320, 880),   # 04
    (320, 1030)   # 05
]

# Draw content
for i, cmd in enumerate(commands[:5]):

    x, y = positions[i]

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()

    # Trim long text
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
