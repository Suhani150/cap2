from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Small knowledge base
text = """
Artificial Intelligence is the simulation of human intelligence by machines.

Machine Learning is a subset of Artificial Intelligence.

FastAPI is a Python framework used for building APIs.

Python is widely used in machine learning and automation.
"""

# Split text into chunks
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

docs = splitter.create_documents([text])

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in FAISS vector database
db = FAISS.from_documents(docs, embeddings)

# Search function
def search_query(query: str):

    results = db.similarity_search(query)

    return results[0].page_content


# TEST
if __name__ == "__main__":

    print(search_query("What is machine learning?"))