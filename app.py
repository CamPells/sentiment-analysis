from analysis import compute_sentiment, compute_filler_ratio
import streamlit as st


st.title("Transcript Sentiment & Filler Analyzer")

lines = []


with open("transcript.txt", "r") as f:
    for line in f:
        cleaned = line.strip()
        if cleaned:  
            lines.append(cleaned)


for line in lines:
    
    speaker, text = line.split(":", 1)
    sentiment, score = compute_sentiment(text)
    filler_count = compute_filler_ratio(text)
    st.subheader(speaker.strip())
    st.text(text.strip())
    st.markdown(f"Sentiment: {sentiment}")
    st.markdown(f"Score: {score}")
    st.markdown(f"Filler Ratio: {filler_count}")
