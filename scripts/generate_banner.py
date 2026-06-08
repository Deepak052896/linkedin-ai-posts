from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

today = datetime.now().strftime("%Y-%m-%d")

caption_file = f"captions/{today}.txt"

with open(caption_file, "r", encoding="utf-8") as f:
    content = f.read()

# Default values
title = "TECH TIP OF THE DAY"
command = ""

# Read caption file
lines = content.splitlines()

for i, line in enumerate(lines):

    if line.strip() == "TITLE:" and i + 1 < len(lines):
        title = lines[i + 1].strip()

    if line.strip() == "COMMAND:" and i + 1 < len(lines):
        command = lines[i + 1].strip()

# Banner Size
width = 1200
height = 627

# Dark Background
img = Image.new("RGB", (width, height), (15, 23, 42))

draw = ImageDraw.Draw(img)

# Fonts
try:
    header_font = ImageFont.truetype("DejaVuSans.ttf", 28)
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    cmd_font = ImageFont.truetype("DejaVuSans.ttf", 42)
    footer_font = ImageFont.truetype("DejaVuSans.ttf", 28)
except:
    header_font = ImageFont.load_default()
    title_font = ImageFont.load_default()
    cmd_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()

# Header
draw.text(
    (60, 80),
    "TECH TIP OF THE DAY",
    fill=(0, 255, 180),
    font=header_font
)

# Title
draw.text(
    (60, 180),
    title,
    fill=(255, 255, 255),
    font=title_font
)

# Command Box
box_x1 = 60
box_y1 = 310
box_x2 = 900
box_y2 = 390

draw.rectangle(
    [box_x1, box_y1, box_x2, box_y2],
    outline=(0, 255, 180),
    width=2
)

draw.text(
    (80, 330),
    command,
    fill=(255, 215, 0),
    font=cmd_font
)

# Footer
draw.text(
    (60, 540),
    "Deepak A",
    fill=(255, 255, 255),
    font=footer_font
)

draw.text(
    (60, 580),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(180, 180, 180),
    font=footer_font
)

# Save Banner
os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today}.png"

img.save(output_file)

print(f"Banner generated successfully: {output_file}")
