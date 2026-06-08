import os
from datetime import datetime
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

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
5. Content must be useful for System Administrators, Cloud Engineers and DevOps Engineers.
6. No motivational content.
7. No Sunday content.

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

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

content = response.text

os.makedirs("captions", exist_ok=True)

with open(f"captions/{date_str}.txt", "w") as f:
    f.write(content)

print(f"Content generated for {topic}")
