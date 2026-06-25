import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Paste YouTube URL")

if st.button("Generate Summary"):

    try:
        # Extract video ID
        if "youtu.be" in url:
            video_id = url.split("/")[-1].split("?")[0]
        else:
            video_id = parse_qs(
                urlparse(url).query
            ).get("v", [""])[0]

        if not video_id:
            st.error("Invalid YouTube URL")
            st.stop()

        # Get transcript
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        transcript_text = " ".join(
            [item.text for item in transcript]
        )

        # Show transcript (optional)
        with st.expander("View Transcript"):
            st.write(transcript_text)

        # Gemini Prompt
        prompt = f"""
        Summarize this YouTube video.

        Give:
        1. Overview
        2. Key Points
        3. Important Takeaways

        Transcript:
        {transcript_text}
        """

        # Generate summary
        response = model.generate_content(prompt)

        st.subheader("📄 Summary")
        st.write(response.text)

        # Download button
        st.download_button(
            label="⬇ Download Summary",
            data=response.text,
            file_name="youtube_summary.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {e}")