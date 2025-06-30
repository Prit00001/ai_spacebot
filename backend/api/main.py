# backend/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import wikipedia
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

# Extract important words (nouns)
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return keywords

# Detect type of question
def detect_question_type(question: str):
    q = question.lower()
    if q.startswith("who"):
        return "person"
    elif q.startswith("what"):
        return "definition"
    elif q.startswith("when"):
        return "date"
    elif q.startswith("where"):
        return "location"
    elif q.startswith("why"):
        return "reason"
    elif q.startswith("how"):
        return "explanation"
    else:
        return "general"

@app.post("/ask")
def ask_question(query: Query):
    user_question = query.question
    keywords = extract_keywords(user_question)
    question_type = detect_question_type(user_question)

    urls = [
        "https://www.nasa.gov",
        "https://www.mosdac.gov.in",
        "https://www.esa.int"
    ]

    collected_text = []

    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, "html.parser")
            paragraphs = soup.find_all("p")
            for p in paragraphs:
                text = p.get_text().strip().lower()
                if any(kw in text for kw in keywords):
                    if question_type == "person" and (" is " in text or " was " in text):
                        collected_text.append(text)
                    elif question_type == "definition" and (" is " in text):
                        collected_text.append(text)
                    elif question_type == "date" and any(w in text for w in [" in ", " on ", " since ", "year"]):
                        collected_text.append(text)
                    else:
                        collected_text.append(text)
                if len(collected_text) >= 2:
                    break
        except Exception:
            continue

    if collected_text:
        return {"answer": collected_text[0]}
    else:
        # Wikipedia fallback
        try:
            titles = wikipedia.search(user_question)
            chosen_title = next((t for t in titles if user_question.lower() in t.lower()), titles[0] if titles else None)

            if chosen_title:
                summary = wikipedia.summary(chosen_title, sentences=3)

                if question_type == "person":
                    doc = nlp(summary)
                    people = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
                    if people:
                        return {"answer": f"{people[0]} - {summary}"}

                return {"answer": f"(Wikipedia) {summary}"}

            return {"answer": "Sorry, I couldn't find anything relevant on Wikipedia."}

        except Exception as e:
            return {"answer": f"Error while searching Wikipedia: {e}"}

@app.get("/hello")
def hello():
    return {"message": "API is working!"}
