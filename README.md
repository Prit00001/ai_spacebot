🚀 AI SpaceBot 🤖

An intelligent question-answering chatbot that fetches answers from **NASA**, **MOSDAC**, **ESA**, and falls back to **Wikipedia** if no relevant results are found. Built using `FastAPI`, `TextBlob`, `BeautifulSoup`, and `requests`.

## ✨ Features

- Understands natural language questions like:
  - “Who was the first person on the Moon?”
  - “What is the Sun?”
  - “Why do black holes form?”
- Extracts keywords using NLP (`TextBlob`)
- Scrapes paragraphs from NASA, MOSDAC, ESA websites
- Falls back to Wikipedia for intelligent answers
- Built with Python, FastAPI, HTML/JS frontend


## 🛠️ Tech Stack

| Tech        | Description                         |
|-------------|-------------------------------------|
| Python      | Core programming language           |
| FastAPI     | Backend API framework               |
| BeautifulSoup | Web scraping library              |
| TextBlob    | NLP keyword extraction              |
| Wikipedia API | Fallback answer source           |
| HTML/JS     | Frontend interface (simple input)   |


## 📁 Project Structure

ai\_spacebot/
├── backend/
│   ├── api/
│   │   └── main.py              # FastAPI app
│   └── helpers/
│       └── (optional NLP utils)
├── index.html                   # Simple front-end UI
├── .gitignore
├── README.md
└── requirements.txt

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_spacebot.git
cd ai_spacebot
````

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 4. Run the server

```bash
uvicorn backend.api.main:app --reload
```

Visit: `http://127.0.0.1:8000/docs` for Swagger UI
Or `index.html` for your custom UI

---

## 🧠 Sample Questions

* `Who is Neil Armstrong?`
* `What is ISRO?`
* `Why do stars twinkle?`
* `Where is the James Webb Telescope?`

---

## 🌍 Sources Used

* [NASA.gov](https://www.nasa.gov)
* [MOSDAC.gov.in](https://www.mosdac.gov.in)
* [ESA.int](https://www.esa.int)
* [Wikipedia.org](https://www.wikipedia.org)

---

## 📦 To Do

* [ ] Deploy online using Render / Railway
* [ ] Add summarization support
* [ ] Improve search accuracy with fuzzy matching
* [ ] Add logging & query analytics
