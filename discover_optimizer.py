from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_for_discover(text):
    prompt = """
    حسّن النص التالي ليكون مناسبًا للظهور في Google Discover.
    الشروط:
    - لغة سلسة وواضحة
    - جمل قصيرة
    - إثارة فضول القارئ بدون مبالغة
    - الحفاظ على الحقائق بدون تغيير
    - تحسين العنوان ليكون جذابًا

    النص:
    {text}
    """.format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        top_p=0.95
    )

    return response.choices[0].message.content
