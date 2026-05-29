import spacy

nlp = spacy.load("en_core_web_sm")

#  Supported apps
APPS = [
    "chrome",
    "browser",
    "notepad",
    "editor",
    "calculator",
    "calc",
    "explorer",
    "files",
    "vscode",
    "code",
    "paint",
    "spotify",
    "telegram",
    "discord",
    "youtube"
]

def extract_entities(text: str) -> dict:

    text = text.lower()

    doc = nlp(text)

    entities = {}

    words = text.split()


    if "youtube" in text and "search" in text:

        entities["platform"] = "youtube"

        query = text

        query = query.replace("search", "")
        query = query.replace("on youtube", "")
        query = query.replace("youtube", "")

        entities["query"] = query.strip()

        return entities

    if "search" in text:

        entities["platform"] = "google"

        query = text.replace("search", "")

        entities["query"] = query.strip()

        return entities


    automation_keywords = [
        "open",
        "start",
        "launch",
        "play"
    ]

    for keyword in automation_keywords:

        if keyword in words:

            index = words.index(keyword)

            # 🔹 Next word becomes app name
            if index + 1 < len(words):

                app_name = words[index + 1]

                entities["app"] = app_name

                return entities


    for word in words:

        if word in APPS:

            entities["app"] = word

            return entities


    entities["query"] = text

    return entities


# TEST
if __name__ == "__main__":

    print(extract_entities("open discord"))

    print(extract_entities("search BTS kpop on youtube"))

    print(extract_entities("open chrome"))

    print(extract_entities("launch spotify"))