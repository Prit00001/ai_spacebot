import re
import string
from textblob import TextBlob

def clean_input(text):
    # Remove punctuation and lowercase
    return text.translate(str.maketrans('', '', string.punctuation)).lower().strip()

def get_keywords(text):
    blob = TextBlob(text)
    nouns = [word for word, tag in blob.tags if tag.startswith('NN')]
    return nouns or text.split()[:3]  # fallback

def get_question_type(text):
    if text.lower().startswith("who"):
        return "person"
    elif text.lower().startswith("what"):
        return "definition"
    elif text.lower().startswith("how"):
        return "explanation"
    elif text.lower().startswith("when"):
        return "time"
    elif text.lower().startswith("where"):
        return "location"
    else:
        return "general"
