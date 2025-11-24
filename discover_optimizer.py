from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_for_discover(text):
    prompt = f"""
    حسّن النص التالي ليكون مناسبًا لــ Google Discover:
    - مقدمة قصيرة جذابة
    - وضوح وسهولة القراءة
    - جمل قصيرة
    - إزالة الحشو
    - تحسين تسلسل المعلومات
    - دون إضافة معلومات جديدة

    النص:
    {text}
    """

    res = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

return res.choices[0].message.content
