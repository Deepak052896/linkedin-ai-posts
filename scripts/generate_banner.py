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

# Template path
template_file = os.path.join(
    TEMPLATE_DIR,
    f"{category}.png"
)

if not os.path.exists(template_file):
    raise FileNotFoundError(
        f"Template not found: {template_file}"
    )

# Open template
img = Image.open(template_file).convert("RGBA")
draw = ImageDraw.Draw(img)

# Fonts
try:
    title_font = ImageFont.truetype(
        "fonts/Poppins-Bold.ttf",
        24
    )

    command_font = ImageFont.truetype(
        "fonts/Montserrat-Bold.ttf",
        24
    )

    description_font = ImageFont.truetype(
        "fonts/DejaVuSans-Bold.ttf",
        24
    )

except Exception:
    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    description_font = ImageFont.load_default()

# Fixed positions for all 5 boxes
positions = [
    430,   # Box 1
    585,   # Box 2
    740,   # Box 3
    895,   # Box 4
    1050   # Box 5
]

for i, cmd in enumerate(commands[:5]):

    x = 370
    y = positions[i]

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()
    description = cmd.get("description", "").strip()

    # Trim long text
    if len(title) > 26:
        title = title[:26] + "..."

    if len(command) > 32:
        command = command[:32] + "..."

    if len(description) > 42:
        description = description[:42] + "..."
        
    # White glow
    for dx in range(-1,0,1):
        for dy in range(-1,0,1):
            draw.text(
                (x + dx, y + dy),
                title,
                font=title_font,
                fill=(255, 255, 255, 80)
        )
    
    # Title
    draw.text(
        (x, y),
        title,
        font=title_font,
        fill=(255, 255, 255)
    )

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text(
                (x + dx, y + 34 + dy),
                command,
                font=command_font,
                fill=(0, 255, 255, 80)
        )
    
    # Command
    draw.text(
        (x, y + 34),
        command,
        font=command_font,
        fill=(0, 255, 255)
    )

    # Description
    draw.text(
        (x, y + 68),
        description,
        font=description_font,
        fill=(220, 220, 220)
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
