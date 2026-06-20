import json
import os
from datetime import date
from PIL import Image, ImageDraw, ImageFont

CURRENT_POST = "state/current_post.json"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "banners"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load post
with open(CURRENT_POST, "r", encoding="utf-8") as f:
    post = json.load(f)

category = post["category"].lower()
commands = post["commands"]

# Template
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
        "fonts/Poppins-Bold.ttf",
        70
    )

    command_font = ImageFont.truetype(
        "fonts/Poppins-Bold.ttf",
        70
    )

    description_font = ImageFont.truetype(
        "fonts/Poppins-Regular.ttf",
        70
    )

    print("FONTS LOADED SUCCESSFULLY")

except Exception as e:

    print("FONT ERROR:", e)

    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    description_font = ImageFont.load_default()

# Fixed Y positions
positions = [
    430,
    585,
    740,
    895,
    1050
]

for i, cmd in enumerate(commands[:5]):

    x = 370
    y = positions[i]

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()
    description = cmd.get("description", "").strip()

    # Trim text
    if len(title) > 28:
        title = title[:28] + "..."

    if len(command) > 35:
        command = command[:35] + "..."

    if len(description) > 45:
        description = description[:45] + "..."

    # TITLE
    draw.text(
        (x, y),
        title,
        font=title_font,
        fill=(255, 255, 255)
    )

    # COMMAND
    draw.text(
        (x, y + 90),
        command,
        font=command_font,
        fill=(0, 255, 255)
    )

    # DESCRIPTION
    draw.text(
        (x, y + 180),
        description,
        font=description_font,
        fill=(210, 210, 210)
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
