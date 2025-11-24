from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_score(text):
    prompt = """
    قيّم احتمال أن يكون النص التالي مكتوبًا بالذكاء الاصطناعي.
    أعد فقط رقمًا دقيقًا بين 0 و100:
    - 0 = بشري بالكامل
    - 100 = ذكاء اصطناعي بالكامل

    لا تشرح. فقط أعد الرقم.

    النص:
    {text}
    """.format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return response.choices[0].message.content
