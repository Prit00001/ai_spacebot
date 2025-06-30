# 🔁 Wikipedia fallback logic (improved to avoid irrelevant pages)
try:
    titles = wikipedia.search(user_question)
    chosen_title = None

    # Strip question words and find best title match
    for t in titles:
        if any(name in t.lower() for name in user_question.lower().split()):
            chosen_title = t
            break

    # Fallback to first if nothing matches well
    if not chosen_title and titles:
        chosen_title = titles[0]

    if chosen_title:
        page = wikipedia.page(chosen_title)
        return {"answer": f"(Wikipedia) {page.summary[:500]}"}
    else:
        return {"answer": "Sorry, couldn't find a good match on Wikipedia."}
except Exception:
    return {"answer": "Sorry, I couldn't find anything helpful online."}
