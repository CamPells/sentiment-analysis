from analysis import compute_sentiment, compute_filler_ratio
import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Transcript Analyzer",
    page_icon="📝",
    layout="wide"
)
st.title("Transcript Analyzer")

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
    

data = []
for line in lines:
    speaker, text = line.split(":", 1)
    sentiment, score = compute_sentiment(text)
    filler_ratio = compute_filler_ratio(text)
    data.append({
        "Speaker": speaker.strip(),
        "Text": text.strip(),
        "Sentiment": sentiment,
        "Confidence": round(score, 2),
        "Filler Ratio": round(filler_ratio * 100, 2) 
    })

df = pd.DataFrame(data)
st.subheader("Transcript Analysis Table")
st.dataframe(df, use_container_width=True)

if not df.empty:
    avg_score = df["Confidence"].mean()
    avg_filler = df["Filler Ratio"].mean()
    st.subheader("Overall Averages")
    st.metric("Average Sentiment Score", f"{avg_score:.2f}")
    st.metric("Average Filler Ratio", f"{avg_filler:.2f}%")


