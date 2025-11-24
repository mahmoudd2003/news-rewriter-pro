from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_score(text):
    prompt = f"""
    قيّم إلى أي درجة يبدو النص مكتوبًا بأسلوب ذكاء اصطناعي.
    أعطني رقمًا من 0 إلى 100:
    0 = بشري تمامًا
    100 = آلي تمامًا

    النص:
    {text}
    """

    res = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

return res.choices[0].message.content
