from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def style_instruction(style):
    if style == "Reuters Style":
        return "اكتب بأسلوب رويترز: جمل قصيرة، لغة محايدة، افتتاحية مباشرة تذكر الحدث أولًا."
    if style == "BBC Style":
        return "اكتب بأسلوب BBC: لغة واضحة، تفاصيل تحليلية خفيفة، توازن بين الخبر والسياق."
    if style == "Al Jazeera Style":
        return "اكتب بأسلوب الجزيرة: سلاسة لغوية، جمل مترابطة، خلفية سياسية قصيرة."
    if style == "Al Arabiya Style":
        return "اكتب بأسلوب العربية: لغة مباشرة، خبر ثم تفاصيل، وضوح شديد."
    if style == "Sky News Arabia Style":
        return "اكتب بأسلوب سكاي نيوز عربية: جمل قصيرة، لغة احترافية، وضوح بدون مبالغة."
    if style == "Analytical Style":
        return "اكتب بأسلوب تحليلي: ربط الأحداث بخلفياتها، شرح دقيق دون رأي."
    if style == "Breaking News Style":
        return "اكتب بأسلوب خبر عاجل: لغة مباشرة، جمل قصيرة جدًا، معلومات أساسية فقط."
    return "اكتب بأسلوب بشري كامل."


def camouflage_instruction(level):
    if level == "Low":
        return "استخدم أسلوبًا بشريًا بسيطًا مع تماسك لغوي."
    if level == "Medium":
        return "استخدم تنويعًا طبيعيًا في طول الجمل وبعض اللمسات البشرية."
    if level == "Strong":
        return """
اجعل الأسلوب بشريًا بالكامل مع كسر واضح للنمط، وعدم انتظام تام في طول الجمل،
واستخدام بعض العبارات التوضيحية البشرية، وتجنب أي صياغة اصطناعية متناسقة.
"""
    return ""


def rewrite_news_humanized(text, style="Human Mode 100%", camouflage="Medium", force_human=False):

    if force_human or style == "Human Mode 100%":
        style_text = "اكتب بأسلوب بشري 100% كما لو أن محررًا عربيًا كتبه دون أي نظام آلي."
    else:
        style_text = style_instruction(style)

    camouflage_text = camouflage_instruction(camouflage)

    prompt = f"""
أعد صياغة الخبر التالي بأسلوب بشري كامل.

التعليمات:
- {style_text}
- {camouflage_text}

تفاصيل إضافية لأسلوب بشري 100%:
1. استخدم جُملاً قصيرة جدًا ثم جُملاً طويلة، ثم جملة عادية.
2. أضف لمسات بشرية خفيفة مثل: "وفق معلومات أولية"، "لم يصدر تعليق فوري"، "على ما يبدو".
3. تجنب أي جملة لها نمط ذكاء اصطناعي.
4. لا تستخدم الجُمل المنمّقة أو الإنشائية.
5. لا تضف أي معلومة غير موجودة.

النص الأصلي:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.78,
        top_p=0.92
    )

    return response.choices[0].message.content
