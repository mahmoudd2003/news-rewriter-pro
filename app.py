import streamlit as st
from rewrite_engine import rewrite_news_humanized
from discover_optimizer import optimize_for_discover
from ai_detector import ai_score
from wordpress_publisher import publish_to_wordpress

st.set_page_config(page_title="News Rewriter Pro – GPT-4.1", layout="wide")

st.title("📰 News Rewriter Pro – GPT-4.1")
st.caption("إعادة صياغة بشرية + تحسين Discover + كشف AI + نشر ووردبريس")

news = st.text_area("ضع الخبر هنا:", height=250)

if st.button("إعادة الصياغة"):
    if not news.strip():
        st.error("⚠️ الرجاء وضع نص الخبر أولاً.")
        st.stop()

    with st.spinner("🔄 جاري إعادة الصياغة البشرية..."):
        rewritten = rewrite_news_humanized(news)

    st.subheader("✍️ النص بعد إعادة الصياغة")
    st.write(rewritten)

    with st.spinner("⚡ تحسين Google Discover..."):
        discover_text = optimize_for_discover(rewritten)

    st.subheader("📱 النص المحسّن لـ Google Discover")
    st.write(discover_text)

    with st.spinner("🧠 تحليل الذكاء الاصطناعي..."):
        score = ai_score(discover_text)

    st.subheader("🔍 درجة الذكاء الاصطناعي (0 = بشري)")
    st.write(score)

    st.success("✨ الاستخراج جاهز!")

    if st.button("نشر إلى WordPress"):
        title = discover_text.split("\n")[0][:60]

        result = publish_to_wordpress(title, discover_text)
        st.subheader("📤 نتيجة النشر:")
        st.json(result)
