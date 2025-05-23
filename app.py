from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

lines = []


with open("transcript.txt", "r") as f:
    for line in f:
        cleaned = line.strip()
        if cleaned:  
            lines.append(cleaned)


def compute_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

for line in lines:
    
    speaker, text = line.split(":", 1)
    sentiment, score = compute_sentiment(text)
    print(f"Speaker: {speaker.strip()}")
    print(f"Text: {text.strip()}")
    print(f"Sentiment: {sentiment}")
    print(f"Score: {score}")
