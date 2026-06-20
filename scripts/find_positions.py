from PIL import Image, ImageDraw
import os

# ========== FIND YOUR TEMPLATE ==========
template_paths = [
    "templates/linux.png",
    "templates/aws.png",
    "templates/windows.png",
    "templates/networking.png",
    "templates/security.png",
    "templates/devops.png",
]

template_path = None
for path in template_paths:
    if os.path.exists(path):
        template_path = path
        break

if not template_path:
    print("❌ No template found!")
    print("   Looking for: templates/linux.png")
    print("   Available files in templates/:")
    if os.path.exists("templates/"):
        print(os.listdir("templates/"))
    exit()

print(f"📁 Using template: {template_path}")

# Open template
img = Image.open(template_path)
draw = ImageDraw.Draw(img)

width, height = img.size
print(f"📐 Image size: {width} x {height}")
print("")
print("==========================================")
print("📊 GRID GENERATED")
print("==========================================")
print("")

# Draw horizontal guide lines every 50px with labels
for y in range(0, height, 50):
    draw.line([(0, y), (width, y)], fill=(255, 0, 0), width=1)
    draw.text((10, y), str(y), fill=(255, 255, 255))

# Draw vertical guide lines every 50px
for x in range(0, width, 50):
    draw.line([(x, 0), (x, height)], fill=(0, 255, 0), width=1)

# Mark command areas - adjust these numbers if needed
command_areas = [
    (650, 800, 1800, 880),     # Row 1
    (650, 1130, 1800, 1210),   # Row 2
    (650, 1460, 1800, 1540),   # Row 3
    (650, 1790, 1800, 1870),   # Row 4
    (650, 2120, 1800, 2200),   # Row 5
]

for i, (x1, y1, x2, y2) in enumerate(command_areas):
    draw.rectangle([(x1, y1), (x2, y2)], outline=(255, 255, 0), width=3)
    draw.text((x1 + 10, y1 - 20), f"ROW {i+1}", fill=(255, 255, 0))

# Save
output_path = "debug_grid.png"
img.save(output_path)

print("✅ Grid saved as: debug_grid.png")
print("")
print("==========================================")
print("📝 INSTRUCTIONS:")
print("==========================================")
print("")
print("1. Download debug_grid.png from artifacts")
print("2. Look for each ROW 1-5")
print("3. Note the Y position where text should go")
print("4. Update Y_ROWS in generate_banner_final.py")
print("")
print(f"   Current Y positions: [800, 1130, 1460, 1790, 2120]")
