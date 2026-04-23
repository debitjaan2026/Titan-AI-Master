import os
from openai import OpenAI

# গিটহাব সিক্রেট থেকে এপিআই কি নিয়ে আসা
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(topic):
    # এআই-কে নির্দেশ দেওয়া যেন সে ভাইরাল আর্টিকেল লেখে
    prompt = f"Write a catchy, viral-style short article about {topic}. Focus on why people should be interested in this today. Keep it engaging and professional."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI: {e}")
        return f"Today's top trending topic is {topic}. Stay tuned for more updates!"
