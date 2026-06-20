from PIL import Image, ImageDraw
import os

# Open your template
img = Image.open("templates/ChatGPT Image Jun 9, 2026, 03_24_24 PM.png")
draw = ImageDraw.Draw(img)

width, height = img.size
print(f"Image: {width} x {height}")

# Draw grid to find positions
for y in range(0, height, 50):
    draw.line([(0, y), (width, y)], fill=(255, 0, 0), width=1)

for x in range(0, width, 50):
    draw.line([(x, 0), (x, height)], fill=(255, 0, 0), width=1)

# Mark key areas
draw.rectangle([(300, 380), (900, 410)], outline=(0, 255, 0), width=2)
draw.rectangle([(300, 465), (900, 495)], outline=(0, 255, 0), width=2)
draw.rectangle([(300, 550), (900, 580)], outline=(0, 255, 0), width=2)
draw.rectangle([(300, 635), (900, 665)], outline=(0, 255, 0), width=2)
draw.rectangle([(300, 720), (900, 750)], outline=(0, 255, 0), width=2)

img.save("grid_output.png")
print("✅ Grid saved as grid_output.png")
print("   Open it and note the positions where text should go")
