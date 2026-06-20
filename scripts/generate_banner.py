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

# ========== SCALE POSITIONS BASED ON IMAGE SIZE ==========
if width >= 3000:  # 4K template
    FONT_TITLE = 80
    FONT_COMMAND = 72
    FONT_DESC = 60
    X_POS = 1200
    Y_POSITIONS = [1400, 1900, 2400, 2900, 3400]
    Y_GAP_TITLE = 0
    Y_GAP_COMMAND = 110
    Y_GAP_DESC = 210
elif width >= 2000:  # 2K template
    FONT_TITLE = 55
    FONT_COMMAND = 48
    FONT_DESC = 38
    X_POS = 750
    Y_POSITIONS = [900, 1220, 1540, 1860, 2180]
    Y_GAP_TITLE = 0
    Y_GAP_COMMAND = 75
    Y_GAP_DESC = 140
elif width >= 1500:  # HD template
    FONT_TITLE = 40
    FONT_COMMAND = 36
    FONT_DESC = 28
    X_POS = 550
    Y_POSITIONS = [700, 950, 1200, 1450, 1700]
    Y_GAP_TITLE = 0
    Y_GAP_COMMAND = 55
    Y_GAP_DESC = 105
else:  # Standard
    FONT_TITLE = 28
    FONT_COMMAND = 24
    FONT_DESC = 20
    X_POS = 350
    Y_POSITIONS = [430, 585, 740, 895, 1050]
    Y_GAP_TITLE = 0
    Y_GAP_COMMAND = 40
    Y_GAP_DESC = 80

print(f"📝 Using scaled values:")
print(f"   Font: T={FONT_TITLE}, C={FONT_COMMAND}, D={FONT_DESC}")
print(f"   X={X_POS}, Y positions={Y_POSITIONS[0]}...")

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
    x = X_POS
    y = Y_POSITIONS[i]

    title = cmd.get("title", "").strip()
    command = cmd.get("command", "").strip()
    description = cmd.get("description", "").strip()

    # Trim long text (adjust based on font size)
    if len(title) > 30:
        title = title[:28] + "..."
    if len(command) > 38:
        command = command[:36] + "..."
    if len(description) > 50:
        description = description[:48] + "..."

    # TITLE - White
    draw.text(
        (x, y + Y_GAP_TITLE),
        title,
        font=title_font,
        fill=(255, 255, 255)
    )

    # COMMAND - Cyan
    draw.text(
        (x, y + Y_GAP_COMMAND),
        command,
        font=command_font,
        fill=(0, 255, 255)
    )

    # DESCRIPTION - Light Gray
    draw.text(
        (x, y + Y_GAP_DESC),
        description,
        font=description_font,
        fill=(210, 210, 210)
    )

# Save banner
today = date.today().strftime("%Y-%m-%d")
output_file = os.path.join(OUTPUT_DIR, f"{today}.png")
img.save(output_file)

print(f"✅ Banner saved: {output_file}")
print(f"📂 Category: {category}")
print(f"📝 Title: {post['title']}")
