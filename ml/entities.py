import spacy

nlp = spacy.load("en_core_web_sm")

# simple app list (can expand later)
APPS = [
    "chrome", "browser",
    "notepad", "editor",
    "calculator", "calc",
    "explorer", "files"
]
def extract_entities(text: str) -> dict:
    doc = nlp(text)

    entities = {}

    # check for app names manually
    for word in text.split():
        if word in APPS:
            entities["app"] = word

    # fallback
    if "app" not in entities:
        entities["query"] = text

    return entities