from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_for_discover(text):
    prompt = """
    حسّن النص التالي ليكون مناسبًا للنشر في Google Discover مع الحفاظ الكامل على الأسلوب الصحفي المحايد.

    المطلوب:
    - إنشاء عنوان جذاب دون إثارة مبالغ فيها.
    - تحسين الفقرة الافتتاحية لتصبح أكثر وضوحًا وقوة.
    - الحفاظ على الحقائق دون أي تغيير أو إضافة.
    - استخدام لغة بسيطة وواضحة وسلسة.
    - عدم إدخال أي مبالغة أو صياغة عاطفية.

    النص الأصلي:
    {text}
    """.format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.65,
        top_p=0.90
    )

    return response.choices[0].message.content
