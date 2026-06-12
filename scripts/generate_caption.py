import json

with open("state/current_post.json", "r") as f:
post = json.load(f)

print(post)
