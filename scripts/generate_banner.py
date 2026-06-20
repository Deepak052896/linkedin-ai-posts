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
template_file = os.path.join(TEMPLATE_DIR, f"{category}.png")
if not os.path.exists(template_file):
    raise FileNotFoundError(f"Template not found: {template_file}")

# Open image
img = Image.open(template_file).convert("RGBA")
draw = ImageDraw.Draw(img)

# Get image size
width, height = img.size
print(f"📐 IMAGE SIZE: {width} x {height}")

# ========== EXACT POSITIONS FOR YOUR TEMPLATE ==========
# Based on your template design
# These values work for 2048x2048 or similar

# Font sizes
FONT_TITLE = 48
FONT_COMMAND = 42
FONT_DESC = 34

# X position (left margin)
X_POS = 700

# Y positions - EXACT values for each row
# Adjust these numbers based on your template
Y_ROWS = [
    750,    # Row 1
    1000,   # Row 2  
    1250,   # Row 3
    1500,   # Row 4
    1750    # Row 5
]

# Gap between title, command, description
Y_GAP_CMD = 45
Y_GAP_DESC = 90

print(f"📝 Using Y positions: {Y_ROWS}")

# Load fonts
try:
    title_font = ImageFont.truetype("fonts/Poppins-Bold.ttf", FONT_TITLE)
    command_font = ImageFont.truetype("fonts/Poppins-Bold.ttf", FONT_COMMAND)
    description_font = ImageFont.truetype("fonts/Poppins-Regular.ttf", FONT_DESC)
    print("✅ CUSTOM FONTS LOADED")
except Exception as e:
    print(f"⚠️ FONT ERROR: {e}")
    title_font = ImageFont.load_default()
    command_font = ImageFont.load_default()
    description_font = ImageFont.load_default()

# Draw each command
for i, cmd in enumerate(commands[:5]):
    y = Y_ROWS[i]
    x = X_POS

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()
    description = cmd.get("description", "").strip()

    # Trim long text
    if len(title) > 32:
        title = title[:29] + "..."
    if len(command) > 40:
        command = command[:37] + "..."
    if len(description) > 55:
        description = description[:52] + "..."

    # TITLE - White
    draw.text(
        (x, y),
        title,
        font=title_font,
        fill=(255, 255, 255)
    )

    # COMMAND - Cyan
    draw.text(
        (x, y + Y_GAP_CMD),
        command,
        font=command_font,
        fill=(0, 255, 255)
    )

    # DESCRIPTION - Light Gray
    draw.text(
        (x, y + Y_GAP_DESC),
        f"- {description}",
        font=description_font,
        fill=(200, 200, 200)
    )
    
    print(f"  ✓ Row {i+1}: Y={y}")

# Save banner
today = date.today().strftime("%Y-%m-%d")
output_file = os.path.join(OUTPUT_DIR, f"{today}.png")
img.save(output_file)

print(f"✅ Banner saved: {output_file}")
print(f"📂 Category: {category}")
