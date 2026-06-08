import os
from datetime import datetime
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

today = datetime.now().strftime("%Y-%m-%d")

prompt = """
You are a Senior System Administrator.

Generate:
1. A technical LinkedIn post (150-200 words)
2. A short banner title (max 10 words)

Topic category:
Linux, AWS, Azure, Windows Server, Networking, Security, DevOps

Output format:

BANNER:
<banner text>

POST:
<linkedin post>
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

content = response.text

os.makedirs("captions", exist_ok=True)

with open(f"captions/{today}.txt", "w") as f:
    f.write(content)

print("Content generated successfully")
