import streamlit as st
from rewrite_engine import rewrite_news_humanized
from discover_optimizer import optimize_for_discover
from ai_detector import ai_score

st.set_page_config(page_title="News Rewriter Pro", layout="wide")

st.title("📰 News Rewriter Pro – الإصدار الاحترافي")

st.subheader("أعد صياغة الأخبار بأسلوب صحفي بشري، مع خيارات الأسلوب ومستوى التمويه")

# اختيار الأسلوب
style = st.selectbox(
    "اختر الأسلوب الصحفي:",
    [
        "Human Mode 100%",
        "Reuters Style",
        "BBC Style",
        "Al Jazeera Style",
        "Al Arabiya Style",
        "Sky News Arabia Style",
        "Analytical Style",
        "Breaking News Style"
    ]
)

# مستوى التمويه
camouflage = st.select_slider(
    "مستوى التمويه ضد أدوات كشف الذكاء الاصطناعي:",
    options=["Low", "Medium", "Strong"],
    value="Medium"
)

# زر التفعيل القوي
force_human = st.checkbox("🔒 تفعيل Human Mode 100% (يتجاوز جميع الإعدادات)")

text_input = st.text_area("أدخل النص الأصلي هنا:", height=300)

if st.button("إعادة الصياغة"):
    if not text_input.strip():
        st.warning("الرجاء إدخال نص.")
    else:
        with st.spinner("جارٍ إعادة الصياغة..."):
            result = rewrite_news_humanized(
                text_input,
                style=style,
                camouflage=camouflage,
                force_human=force_human
            )
        st.success("تمت إعادة الصياغة:")
        st.write(result)

if st.button("تحسين للنشر على Google Discover"):
    if not text_input.strip():
        st.warning("الرجاء إدخال نص.")
    else:
        with st.spinner("جارٍ التحسين..."):
            result = optimize_for_discover(text_input)
        st.success("النص المحسّن:")
        st.write(result)

if st.button("فحص احتمال الذكاء الاصطناعي"):
    if not text_input.strip():
        st.warning("الرجاء إدخال نص.")
    else:
        with st.spinner("جارٍ التقييم..."):
            score = ai_score(text_input)
        st.success("نتيجة التقييم:")
        st.write(f"احتمال أنه مكتوب بالذكاء الاصطناعي: {score}%")
