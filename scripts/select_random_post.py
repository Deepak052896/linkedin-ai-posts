import os
import json
import random

GENERATED_DIR = "generated"
STATE_FILE = "state/used_posts.json"
CURRENT_POST_FILE = "state/current_post.json"

# Create state folder if not exists
os.makedirs("state", exist_ok=True)

# Load used posts
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        used_data = json.load(f)
else:
    used_data = {"used": []}

used_posts = set(used_data.get("used", []))

# Find all JSON files
all_posts = []

for root, dirs, files in os.walk(GENERATED_DIR):
    for file in files:
        if file.endswith(".json"):
            full_path = os.path.join(root, file)
            all_posts.append(full_path)

# Remove already used posts
available_posts = [
    post for post in all_posts
    if post not in used_posts
]

# If all posts used, reset automatically
if not available_posts:
    print("All posts have been used.")
    print("Resetting used_posts.json...")

    used_posts = set()
    available_posts = all_posts

# Select random post
selected_file = random.choice(available_posts)

# Read selected JSON
with open(selected_file, "r", encoding="utf-8") as f:
    selected_post = json.load(f)

# Save current selected post
with open(CURRENT_POST_FILE, "w", encoding="utf-8") as f:
    json.dump(selected_post, f, indent=4)

# Update used posts
used_posts.add(selected_file)

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(
        {
            "used": sorted(list(used_posts))
        },
        f,
        indent=4
    )

print(f"Selected: {selected_file}")
print(f"Category: {selected_post.get('category')}")
print(f"Title: {selected_post.get('title')}")
