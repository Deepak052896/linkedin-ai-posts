from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# ========== FIXED: Point to correct folder ==========
TEMPLATE_DIR = "assets"      # Your templates are here
DATA_DIR = "data"
OUTPUT_DIR = "banners"

def load_tips(category):
    """Load commands from data file"""
    file_path = os.path.join(DATA_DIR, f"{category}.txt")
    if not os.path.exists(file_path):
        print(f"❌ Data missing: {file_path}")
        return []
    
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
    
    tips = []
    for line in lines[:5]:
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 2:
                tips.append((parts[0], parts[1]))
    return tips

def get_category():
    """Auto select based on day"""
    categories = ["linux", "aws", "windows", "networking", "security", "devops"]
    day_index = datetime.now().weekday()
    return categories[day_index % len(categories)]

def generate_banner():
    """Main banner generator"""
    
    category = get_category()
    print(f"📅 Generating {category} banner...")
    
    # Check template exists
    template_path = os.path.join(TEMPLATE_DIR, f"{category}.png")
    if not os.path.exists(template_path):
        print(f"❌ Template not found: {template_path}")
        print(f"📁 Available templates: {os.listdir(TEMPLATE_DIR) if os.path.exists(TEMPLATE_DIR) else 'Folder not found'}")
        return None
    
    # Load commands
    tips = load_tips(category)
    if not tips:
        print(f"❌ No commands for {category}")
        return None
    
    # Open template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Load font
    try:
        font_cmd = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except:
        font_cmd = ImageFont.load_default()
        font_desc = ImageFont.load_default()
    
    # ========== ADJUST THESE POSITIONS ==========
    cmd_x = 320      # Command X position
    desc_x = 320     # Description X position
    
    # Y positions for 5 commands
    cmd_y = [380, 470, 560, 650, 740]
    desc_y = [415, 505, 595, 685, 775]
    
    # Draw each command
    for i, (cmd, desc) in enumerate(tips):
        draw.text((cmd_x, cmd_y[i]), cmd, fill=(0, 255, 0), font=font_cmd)
        draw.text((desc_x, desc_y[i]), desc, fill=(200, 200, 200), font=font_desc)
        print(f"  ✓ {cmd}")
    
    # Save banner
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(OUTPUT_DIR, f"{date_str}.png")
    img.save(output_path)
    
    print(f"✅ Banner saved: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_banner()
