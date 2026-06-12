import os
import json
import math

DATA_DIR = "data"
OUTPUT_BASE_DIR = "generated"

POST_SIZE = 5

for file_name in os.listdir(DATA_DIR):

    if not file_name.endswith(".txt"):
        continue

    category = file_name.replace(".txt", "")

    input_file = os.path.join(DATA_DIR, file_name)
    output_dir = os.path.join(OUTPUT_BASE_DIR, category)

    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    records = []

    for line in lines:

        parts = line.split("|")

        if len(parts) < 3:
            continue

        records.append({
            "title": parts[0].strip(),
            "command": parts[1].strip(),
            "description": parts[2].strip()
        })

    total_posts = math.ceil(len(records) / POST_SIZE)

    for index in range(total_posts):

        start = index * POST_SIZE
        end = start + POST_SIZE

        chunk = records[start:end]

        output = {
            "category": category,
            "post_number": index + 1,
            "title": f"{category.upper()} Tips #{index + 1}",
            "commands": chunk
        }

        output_file = os.path.join(
            output_dir,
            f"{category}_post_{index + 1}.json"
        )

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

    print(
        f"{category}: Generated {total_posts} JSON files"
    )

print("All categories processed successfully!")
