from transformers import pipeline
import spacy
import whisper

sentiment_pipeline = pipeline("sentiment-analysis","distilbert/distilbert-base-uncased-finetuned-sst-2-english")
filler = {'um', 'uh', 'like', 'you know'}
nlp = spacy.load("en_core_web_sm")

def compute_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

def get_filler_count(doc):
    count = 0
    for token in doc:
        if token.text.lower() in filler:
            count += 1
    return count

def compute_filler_ratio(text):
    doc = nlp(text)
    words = []
    for token in doc:
        if token.is_alpha:
            words.append(token)

    filler_count = get_filler_count(doc)
    
    if words:
        return filler_count / len(words)
    else:
        return 0
    
def transcribe_audio(file):
    model = whisper.load_model("base")
    result = model.transcribe(file)
    return result['text']
