from ml.preprocess import preprocess_text
from ml.entities import extract_entities

def process_input(text: str) -> dict:
    clean_text = preprocess_text(text)
    entities = extract_entities(clean_text)

    return {
        "clean_text": clean_text,
        "entities": entities
    }

if __name__ == "__main__":
    print(process_input("open Chrome"))