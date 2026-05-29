def classify_intent(text: str) -> str:

    text = text.lower()


    if (
        "search" in text
        or "youtube" in text
        or "google" in text
    ):

        return "web_search"


    automation_keywords = [
        "open",
        "start",
        "launch",
        "play",
        "show",
        "take",
        "lock"
    ]

    for word in automation_keywords:

        if word in text:

            return "automation"


    return "query"


# TEST
if __name__ == "__main__":

    print(classify_intent("search BTS kpop on youtube"))

    print(classify_intent("open chrome"))