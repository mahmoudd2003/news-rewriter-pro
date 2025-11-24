from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_news_humanized(text):
    prompt = """
أعد صياغة الخبر التالي بأسلوب صحفي عربي بشري احترافي، قريب من كتابة وكالات الأنباء مثل رويترز و«أسوشيتد برس».

القواعد:
1. لغة بشرية طبيعية.
2. جمل قصيرة ومتوسطة وطويلة معاً.
3. ترتيب الخبر: الفقرة الافتتاحية → التفاصيل → الخلفية.
4. موضوعية بلا مبالغة.
5. منع الجمل النمطية المعتادة في الذكاء الاصطناعي.
6. منع اختراع معلومات.
7. عدم التكرار.

النص الأصلي:
{text}
""".format(text=text)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.75,
        top_p=0.92
    )

    return response.choices[0].message.content
