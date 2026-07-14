import chromadb

# Create an in-memory Chroma database
client = chromadb.Client()


def create_vector_store(chunks, embeddings):
    """
    Store document chunks and their embeddings in ChromaDB.
    """

    collection = client.create_collection(
        name="documents"
    )

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return collection


def search_vector_store(collection, question):
    """
    Retrieve the most relevant document chunks.
    """

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    return results["documents"][0]