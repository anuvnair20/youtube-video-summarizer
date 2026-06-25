# YouTube Video Summarizer

## Team Members

* Your Name
* Friend Name

## Project Overview

The YouTube Video Summarizer is a Generative AI application that automatically generates summaries of YouTube videos.

The user provides a YouTube video URL, the application extracts the video's transcript, and Google's Gemini AI model generates a concise summary with key points and takeaways.

## Features

* Accepts YouTube video URLs
* Extracts video transcripts automatically
* Generates AI-powered summaries
* Displays key points and takeaways
* Simple and user-friendly interface

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* YouTube Transcript API
* Python Dotenv

## Project Workflow

1. User enters a YouTube URL.
2. The application extracts the video ID.
3. The transcript is fetched using YouTube Transcript API.
4. The transcript is sent to Gemini AI.
5. Gemini generates a summary.
6. The summary is displayed to the user.

## Installation

### Install Dependencies

pip install -r requirements.txt

### Create .env File

GEMINI_API_KEY=YOUR_API_KEY

### Run Application

streamlit run app.py

## Future Enhancements

* Multi-language support
* PDF export of summaries
* Different summary styles
* Video analytics dashboard

## Conclusion

This project demonstrates the use of Generative AI for content summarization. It combines transcript extraction and Google's Gemini model to provide quick and accurate video summaries.
