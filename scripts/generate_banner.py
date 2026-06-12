import json
import os
from datetime import date
from PIL import Image, ImageDraw, ImageFont

CURRENT_POST = "state/current_post.json"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "banners"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(CURRENT_POST, "r", encoding="utf-8") as f:
post = json.load(f)

category = post["category"].lower()
commands = post["commands"]

template_file = os.path.join(
TEMPLATE_DIR,
f"{category}.png"
)

if not os.path.exists(template_file):
raise Exception(f"Template not found: {template_file}")

img = Image.open(template_file).convert("RGBA")
draw = ImageDraw.Draw(img)

try:
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 34)
except:
font = ImageFont.load_default()

positions = [
(320, 420),
(320, 620),
(320, 820),
(320, 1020),
(320, 1220)
]

for i, cmd in enumerate(commands[:5]):
x, y = positions[i]
draw.text(
(x, y),
cmd["title"],
fill="white",
font=font
)

today = date.today().strftime("%Y-%m-%d")

output_file = os.path.join(
OUTPUT_DIR,
f"{today}.png"
)

img.save(output_file)

print(f"Banner generated: {output_file}")
