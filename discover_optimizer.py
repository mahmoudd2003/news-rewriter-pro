from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_for_discover(text):
    prompt = """
حسّن النص التالي ليكون مناسبًا للنشر في Google Discover دون المساس بالحقائق أو المصداقية.

التعليمات:
1. صياغة عنوان جذاب دون مبالغة.
2. تحسين الفقرة الافتتاحية لتكون أقوى وأسهل للفهم.
3. استخدام لغة سهلة وواضحة وموضوعية.
4. لا تضيف أي معلومات جديدة غير موجودة في النص الأصلي.
5. لا تستخدم صياغات إنشائية أو عاطفية.

النص الأصلي:
{text}
""".format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.60,
        top_p=0.90
    )

    return response.choices[0].message.content
