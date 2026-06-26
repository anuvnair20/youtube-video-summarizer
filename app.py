import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI YouTube Video Summarizer",
    page_icon="🎥",
    layout="centered"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
/* Background */
.stApp{
    background: linear-gradient(to right,#ffe4ec,#fff5f8);
}

/* Title */
h1{
    font-family: 'Dancing Script', cursive;
    color:#d81b60;
    text-align:center;
    font-size:55px;
    font-weight:bold;
}
/* Subtitle */
.subtitle{
    text-align:center;
    color:#555;
    font-size:18px;
}

/* Text Input */
.stTextInput>div>div>input{
    border:2px solid #ff69b4;
    border-radius:12px;
    padding:10px;
}

/* Button */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#ff4b91,#ff1493);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#ff1493,#c2185b);
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#ffd6e8;
}

/* Success */
.stSuccess{
    border-radius:10px;
}

/* Info */
.stInfo{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD API
# ----------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:

    st.markdown(
    "<h1 style='font-family:Dancing Script,cursive;'>💖 About</h1>",
    unsafe_allow_html=True
)

    st.write("""
This application summarizes YouTube videos using **Google Gemini AI**.
""")

    st.markdown("---")

    st.markdown(
    "<h2 style='font-family:Dancing Script,cursive;'>✨ Features</h2>",
    unsafe_allow_html=True
)

    st.write("✔ AI Generated Summary")
    st.write("✔ Transcript Extraction")
    st.write("✔ Key Takeaways")
    st.write("✔ Download Summary")

    st.markdown("---")

    st.markdown(
    "<h2 style='font-family:Dancing Script,cursive;'>👨‍💻 Team Members</h2>",
    unsafe_allow_html=True
)

    st.success("Abhijith")
    st.success("Anu")
    st.success("Adarsh")

# ----------------------------
# MAIN PAGE
# ----------------------------

st.markdown("""
<h1 style="
font-family:'Dancing Script', cursive;
font-size:60px;
color:#d81b60;
text-align:center;
text-shadow:2px 2px 6px rgba(0,0,0,0.2);
margin-bottom:0;">
🎥 AI YouTube Video Summarizer
</h1>
""", unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Generate AI-powered summaries of YouTube videos using Google Gemini.</p>',
unsafe_allow_html=True
)

url = st.text_input(
    "🔗 Paste YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("✨ Generate Summary"):

    try:

        # Extract Video ID
        if "youtu.be" in url:
            video_id = url.split("/")[-1].split("?")[0]
        else:
            video_id = parse_qs(urlparse(url).query).get("v", [""])[0]

        if not video_id:
            st.error("❌ Invalid YouTube URL")
            st.stop()

        # Fetch Transcript
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        transcript_text = " ".join(
            [item.text for item in transcript]
        )

        # Show Transcript
        with st.expander("📜 View Transcript"):
            st.write(transcript_text)

        prompt = f"""
Summarize this YouTube video.

Give:

1. Overview

2. Key Points

3. Important Takeaways

Transcript:

{transcript_text}
"""

        with st.spinner("🤖 Gemini AI is generating the summary..."):

            response = model.generate_content(prompt)

        st.success("✅ Summary Generated Successfully!")

        st.subheader("📄 AI Summary")

        st.info(response.text)

        st.download_button(
            label="⬇ Download Summary",
            data=response.text,
            file_name="youtube_summary.txt",
            mime="text/plain"
        )

    except Exception as e:

        st.error(f"❌ Error: {e}")

# ----------------------------
# FOOTER
# ----------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>

<h2 style="font-family:'Dancing Script', cursive; color:#d81b60;">
❤️ Developed By 
</h2>

<h4>Abhijith • Anu • Adarsh</h4>

<p>Built using <b>Python</b>, <b>Streamlit</b>, <b>Google Gemini</b> and
<b>YouTube Transcript API</b>.</p>

</div>
""",
unsafe_allow_html=True
)
