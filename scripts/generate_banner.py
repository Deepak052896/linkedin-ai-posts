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

# Pick template based on category
template_file = os.path.join(
    TEMPLATE_DIR,
    f"{category}.png"
)

if not os.path.exists(template_file):
    raise Exception(
        f"Template not found: {template_file}"
    )

# Open template
img = Image.open(template_file).convert("RGBA")
draw = ImageDraw.Draw(img)

# Fonts
try:
    title_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        22
    )

    command_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        24
    )

    description_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        16
    )

except:
    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    description_font = ImageFont.load_default()

# Box positions
positions = [
    (320, 435),   # 01
    (320, 610),   # 02
    (320, 785),   # 03
    (320, 960),   # 04
    (320, 1135)   # 05
]

# Draw content
for i, cmd in enumerate(commands[:5]):

    x, y = positions[i]

    title = cmd.get("title", "")[:35]

    command = cmd.get("command", "")
    if len(command) > 40:
        command = command[:40] + "..."

    description = cmd.get("description", "")
    if len(description) > 45:
        description = description[:45] + "..."

    draw.text(
        (x, y),
        title,
        fill="white",
        font=title_font
    )

    draw.text(
        (x, y + 38),
        command,
        fill=(0, 255, 255),
        font=command_font
    )

    draw.text(
        (x, y + 72),
        description,
        fill=(180, 180, 180),
        font=description_font
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
