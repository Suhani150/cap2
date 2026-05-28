from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def classify_intent_bert(text: str):

    result = classifier(text)

    label = result[0]["label"]

    # Simple mapping
    if any(word in text.lower() for word in ["open", "start", "close", "play"]):
        return "automation"

    return "query"


# TEST
if __name__ == "__main__":

    print(classify_intent_bert("open chrome"))
    print(classify_intent_bert("what is AI"))