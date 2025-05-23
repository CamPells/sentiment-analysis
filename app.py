from analysis import compute_sentiment, compute_filler_ratio




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
    print(f"Speaker: {speaker.strip()}")
    print(f"Text: {text.strip()}")
    print(f"Sentiment: {sentiment}")
    print(f"Score: {score}")
    print(f"Filler Ratio: {filler_count}")
