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

# ========== FIXED FOR 1024x1536 TEMPLATE ==========
# Font sizes - smaller for this template
FONT_TITLE = 28
FONT_COMMAND = 24
FONT_DESC = 20

# X position
X_POS = 180

# Y positions - EXACT for each row
Y_ROWS = [
    430,    # Row 1
    570,    # Row 2
    710,    # Row 3
    850,    # Row 4
    990     # Row 5
]

# Gaps between text lines
Y_GAP_CMD = 32   # Title to Command
Y_GAP_DESC = 60  # Title to Description

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
    if len(title) > 28:
        title = title[:25] + "..."
    if len(command) > 32:
        command = command[:29] + "..."
    if len(description) > 45:
        description = description[:42] + "..."

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
