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

# ========== SCALE BASED ON IMAGE SIZE ==========
if width >= 3000:  # 4K
    FONT_TITLE = 70
    FONT_COMMAND = 60
    FONT_DESC = 50
    X_POS = 1100
    Y_START = 1200
    Y_STEP = 500  # Space between each command
    Y_GAP_CMD = 85
    Y_GAP_DESC = 170
    
elif width >= 2000:  # 2K
    FONT_TITLE = 48
    FONT_COMMAND = 40
    FONT_DESC = 32
    X_POS = 700
    Y_START = 800
    Y_STEP = 340
    Y_GAP_CMD = 60
    Y_GAP_DESC = 120
    
elif width >= 1500:  # HD
    FONT_TITLE = 36
    FONT_COMMAND = 30
    FONT_DESC = 24
    X_POS = 520
    Y_START = 620
    Y_STEP = 260
    Y_GAP_CMD = 48
    Y_GAP_DESC = 95
    
else:  # Standard
    FONT_TITLE = 26
    FONT_COMMAND = 22
    FONT_DESC = 18
    X_POS = 340
    Y_START = 400
    Y_STEP = 170
    Y_GAP_CMD = 35
    Y_GAP_DESC = 70

print(f"📝 Using: Y_START={Y_START}, Y_STEP={Y_STEP}")

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

# Draw each command with equal spacing
for i, cmd in enumerate(commands[:5]):
    # Calculate Y position with equal spacing
    y = Y_START + (i * Y_STEP)
    x = X_POS

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()
    description = cmd.get("description", "").strip()

    # Trim long text
    max_title = 30
    max_cmd = 38
    max_desc = 50
    
    if len(title) > max_title:
        title = title[:max_title-3] + "..."
    if len(command) > max_cmd:
        command = command[:max_cmd-3] + "..."
    if len(description) > max_desc:
        description = description[:max_desc-3] + "..."

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
print(f"📝 Title: {post['title']}")
