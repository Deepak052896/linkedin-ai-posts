from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

today = datetime.now().strftime("%Y-%m-%d")

caption_file = f"captions/{today}.txt"

with open(caption_file, "r", encoding="utf-8") as f:
    content = f.read()

title = "TECH TIP OF THE DAY"
command = ""

for line in content.splitlines():
    if line.startswith("TITLE:"):
        title = line.replace("TITLE:", "").strip()

    if line.startswith("COMMAND:"):
        command = line.replace("COMMAND:", "").strip()

width = 1200
height = 627

img = Image.new("RGB", (width, height), (15, 23, 42))

draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    cmd_font = ImageFont.truetype("DejaVuSans.ttf", 42)
    footer_font = ImageFont.truetype("DejaVuSans.ttf", 28)
except:
    title_font = ImageFont.load_default()
    cmd_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()

draw.text(
    (60, 80),
    "TECH TIP OF THE DAY",
    fill=(0, 255, 180),
    font=footer_font
)

draw.text(
    (60, 180),
    title,
    fill=(255, 255, 255),
    font=title_font
)

draw.text(
    (60, 320),
    command,
    fill=(255, 215, 0),
    font=cmd_font
)

draw.text(
    (60, 560),
    "Deepak A",
    fill=(255, 255, 255),
    font=footer_font
)

draw.text(
    (60, 595),
    "IT Infrastructure Specialist | Cloud Engineer",
    fill=(180, 180, 180),
    font=footer_font
)

os.makedirs("banners", exist_ok=True)

output_file = f"banners/{today}.png"

img.save(output_file)

print(f"Banner generated: {output_file}")
