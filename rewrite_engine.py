from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_news_humanized(text):
    prompt = f"""
    أعد صياغة الخبر التالي بأسلوب صحفي عربي بشري 100%.
    الشروط:
    - جمل قصيرة وأخرى متوسطة
    - تدفق طبيعي كالكتابة البشرية
    - إعادة ترتيب الجمل بشكل منطقي بدون تغيير الحقائق
    - نبرة يومية عادية غير رسمية
    - منع أي علامات أسلوب ذكاء اصطناعي

    النص:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
        top_p=0.9
    )

    return response.choices[0].message["content"]
