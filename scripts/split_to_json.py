import os
import json
import math

INPUT_FILE = "data/aws.txt"
OUTPUT_DIR = "generated/aws"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

records = []

for line in lines:
    parts = line.split("|")

    if len(parts) >= 3:
        records.append({
            "title": parts[0].strip(),
            "command": parts[1].strip(),
            "description": parts[2].strip()
        })

POST_SIZE = 5

total_posts = math.ceil(len(records) / POST_SIZE)

for index in range(total_posts):

    start = index * POST_SIZE
    end = start + POST_SIZE

    chunk = records[start:end]

    output = {
        "category": "aws",
        "post_number": index + 1,
        "title": f"AWS Tips #{index + 1}",
        "commands": chunk
    }

    output_file = os.path.join(
        OUTPUT_DIR,
        f"aws_post_{index + 1}.json"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

print(f"Generated {total_posts} JSON files")
