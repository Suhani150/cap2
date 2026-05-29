from ml.input_pipeline import process_input
from ml.intent import classify_intent

def full_pipeline(text: str):

    commands = [cmd.strip() for cmd in text.split("and")]

    results = []

    for cmd in commands:

        processed = process_input(cmd)

        intent = classify_intent(processed["clean_text"])

        results.append({
            "clean_text": processed["clean_text"],
            "entities": processed["entities"],
            "intent": intent
        })

    return results


# TEST
if __name__ == "__main__":

    print(full_pipeline("search BTS kpop on youtube"))