from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(chunks).tolist()
    return embeddings