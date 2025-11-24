from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_score(text):
    prompt = """
    قيم النص التالي من حيث احتمالية أنه مكتوب بالذكاء الاصطناعي.
    أعد فقط رقمًا بين 0 و 100:
    - 0 يعني كتابة بشرية بالكامل
    - 100 يعني ذكاء اصطناعي بالكامل

    النص:
    {text}
    """.format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.9
    )

    return response.choices[0].message.content
