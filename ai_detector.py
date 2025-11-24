from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_score(text):
    prompt = """
أعطني تقديرًا رقميًا لاحتمال أن يكون النص مكتوبًا بواسطة الذكاء الاصطناعي.
أعد فقط رقمًا من 0 إلى 100:
0 = بشري تمامًا
100 = ذكاء اصطناعي بالكامل

بدون أي شرح إضافي.

النص:
{text}
""".format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return response.choices[0].message.content
