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
        24
    )

    command_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        18
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
    (320, 430),
    (320, 630),
    (320, 830),
    (320, 1030),
    (320, 1230)
]

# Draw content
for i, cmd in enumerate(commands[:5]):

    x, y = positions[i]

    title = cmd.get("title", "")

    command = cmd.get("command", "")
    if len(command) > 35:
        command = command[:35] + "..."

    description = cmd.get("description", "")
    if len(description) > 50:
        description = description[:50] + "..."

    # Title
    draw.text(
        (x, y),
        title,
        fill="white",
        font=title_font
    )

    # Command
    draw.text(
        (x, y + 35),
        command,
        fill=(0, 255, 255),
        font=command_font
    )

    # Description
    draw.text(
        (x, y + 65),
        description,
        fill=(200, 200, 200),
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
