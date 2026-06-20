from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
from datetime import datetime

# ========== CONFIGURATION ==========
TEMPLATE_PATH = "templates/ChatGPT Image Jun 9, 2026, 03_24_24 PM.png"
OUTPUT_DIR = "banners"
DATA_DIR = "data"

def load_commands(category):
    """Load commands from data file"""
    file_path = os.path.join(DATA_DIR, f"{category}.txt")
    if not os.path.exists(file_path):
        print(f"❌ Data file not found: {file_path}")
        return []
    
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
    
    commands = []
    for line in lines[:5]:
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 2:
                commands.append((parts[0], parts[1]))
    return commands

def get_today_category():
    """Auto select category based on day"""
    categories = ["linux", "aws", "windows", "networking", "security", "devops"]
    day_index = datetime.now().weekday()
    return categories[day_index % len(categories)]

def get_text_positions(img_width, img_height):
    """
    Returns exact positions based on image size
    Adjust these based on your template
    """
    return {
        # Command positions (X, Y)
        "cmd1": (320, 385),
        "cmd2": (320, 470),
        "cmd3": (320, 555),
        "cmd4": (320, 640),
        "cmd5": (320, 725),
        
        # Description positions (X, Y)
        "desc1": (320, 415),
        "desc2": (320, 500),
        "desc3": (320, 585),
        "desc4": (320, 670),
        "desc5": (320, 755),
        
        # Title position (if you want to change)
        "title": (300, 150),
        "subtitle": (300, 200),
    }

def generate_banner():
    """Generate banner using template"""
    
    category = get_today_category()
    print(f"📅 Generating {category.upper()} banner...")
    
    # Check template exists
    if not os.path.exists(TEMPLATE_PATH):
        print(f"❌ Template not found: {TEMPLATE_PATH}")
        print("   Please add your template PNG file to templates/ folder")
        return None
    
    # Load commands
    commands = load_commands(category)
    if not commands:
        print(f"❌ No commands for {category}")
        return None
    
    # Load template
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)
    
    # Get image dimensions
    width, height = img.size
    print(f"📐 Image size: {width} x {height}")
    
    # Load fonts
    try:
        # Command font - bold
        font_cmd = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        # Description font - regular
        font_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        # Fallback if not available
    except:
        font_cmd = ImageFont.load_default()
        font_desc = ImageFont.load_default()
    
    # Get positions
    pos = get_text_positions(width, height)
    
    # Colors
    COLOR_CMD = (0, 255, 0)        # Green
    COLOR_DESC = (180, 180, 180)   # Light Gray
    
    # Draw each command
    cmd_keys = ["cmd1", "cmd2", "cmd3", "cmd4", "cmd5"]
    desc_keys = ["desc1", "desc2", "desc3", "desc4", "desc5"]
    
    for i, (cmd, desc) in enumerate(commands):
        if i >= 5:
            break
        
        # Draw command (left side)
        draw.text(pos[cmd_keys[i]], cmd, fill=COLOR_CMD, font=font_cmd)
        
        # Draw description (below command)
        draw.text(pos[desc_keys[i]], f"- {desc}", fill=COLOR_DESC, font=font_desc)
        
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
