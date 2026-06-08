import os
import time
from datetime import datetime
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY environment variable not found")

client = genai.Client(api_key=api_key)

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

weekday = today.weekday()

topics = {
    0: "Linux Command of the Day",
    1: "AWS Tip of the Day",
    2: "Windows Server Tip of the Day",
    3: "Networking Tip of the Day",
    4: "Security Best Practice",
    5: "DevOps Quick Tip"
}

topic = topics.get(weekday, "DevOps Quick Tip")

prompt = f"""
You are a Senior IT Infrastructure Specialist and Cloud Engineer.

Generate content for LinkedIn.

Today's category:
{topic}

Requirements:

1. Banner title (maximum 8 words)
2. Practical technical tip
3. LinkedIn post between 100-150 words
4. Include relevant hashtags
5. Content must be useful for:
   - System Administrators
   - Cloud Engineers
   - DevOps Engineers
6. No motivational content.
7. No Sunday content.
8. Give actionable technical advice.

Output format exactly:

BANNER:
<short title>

TIP:
<technical tip>

POST:
<linkedin post>

HASHTAGS:
<hashtags>
"""

response = None

for attempt in range(3):
    try:
        print(f"Attempt {attempt + 1}...")

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        break

    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")

        if attempt < 2:
            time.sleep(10)

if response is None:
    raise Exception("Failed to generate content after 3 attempts")

content = response.text

os.makedirs("captions", exist_ok=True)

with open(f"captions/{date_str}.txt", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Content generated successfully for {topic}")
print(f"Saved to captions/{date_str}.txt")
