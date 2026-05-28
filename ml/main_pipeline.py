from ml.input_pipeline import process_input
from ml.distilbert_intent import classify_intent_bert

def full_pipeline(text: str):

    # Split multiple commands
    commands = [cmd.strip() for cmd in text.split("and")]

    results = []

    for cmd in commands:

        # Preprocessing + Entity Extraction
        processed = process_input(cmd)

        # DistilBERT Intent Classification
        intent = classify_intent_bert(processed["clean_text"])

        # Store final structured output
        results.append({
            "clean_text": processed["clean_text"],
            "entities": processed["entities"],
            "intent": intent
        })

    return results


# TEST
if __name__ == "__main__":

    print(full_pipeline("open chrome and open notepad"))