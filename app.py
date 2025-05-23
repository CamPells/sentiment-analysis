from analysis import compute_sentiment, compute_filler_ratio, transcribe_audio
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Transcript Analyzer",
    page_icon="📝",
    layout="wide"
)
st.title("Transcript Analyzer")
# sidebar page switcher
page = st.sidebar.selectbox("Choose a view", ["Transcript", "Audio Recording"])


# transcript view
if page == "Transcript":
    lines = []

    # load the transcript file
    with open("transcript.txt", "r") as f:
        for line in f:
            cleaned = line.strip()
            if cleaned:  
                lines.append(cleaned)

   
    # prepare data for display
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
    # create a DataFrame, display it, and calculate averages
    df = pd.DataFrame(data)
    st.subheader("Transcript Analysis Table")
    st.dataframe(df, use_container_width=True)

    if not df.empty:
        avg_score = df["Confidence"].mean()
        avg_filler = df["Filler Ratio"].mean()
        st.subheader("Overall Averages")
        st.metric("Average Sentiment Score", f"{avg_score:.2f}")
        st.metric("Average Filler Ratio", f"{avg_filler:.2f}%")


# audio view
elif page == "Audio Recording":
    st.subheader("Record and Analyze Speech")

    # record audio
    audio_value = st.audio_input("Record a voice message")
    if audio_value:
        st.audio(audio_value, format="audio/wav")

        # save the audio to a file
        with open("recording.wav", "wb") as f:
            f.write(audio_value.getvalue())

        # transcribe the audio
        with st.spinner("Transcribing audio..."):
            text = transcribe_audio("recording.wav")

        st.subheader("Transcribed Text")
        st.write(text)

        # analyze the transcribed text
        sentiment, score = compute_sentiment(text)
        filler_ratio = compute_filler_ratio(text)

        st.subheader("Analysis")
        st.text(f"Sentiment: {sentiment} ({score:.2f})")
        st.text(f"Filler Ratio: {round(filler_ratio * 100, 2)}")


