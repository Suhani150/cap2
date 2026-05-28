from transformers import pipeline

# DistilBERT zero-shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

labels = ["automation", "query"]

def classify_intent(text: str) -> str:

    result = classifier(text, labels)

    return result["labels"][0]


# TEST
if __name__ == "__main__":

    print(classify_intent("open chrome"))
    print(classify_intent("what is artificial intelligence"))