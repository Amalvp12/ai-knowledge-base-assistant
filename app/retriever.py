from app.database import cursor
import ast
import numpy as np
from app.embeddings import create_embedding


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_relevant_document(question):

    question_embedding = create_embedding(question)

    cursor.execute("""
        SELECT content, embedding
        FROM document_chunks
    """)

    documents = cursor.fetchall()

    best_score = -1
    best_document = ""

    for content, embedding in documents:

        document_embedding = ast.literal_eval(embedding)

        score = cosine_similarity(
            question_embedding,
            document_embedding
        )

        if score > best_score:
            best_score = score
            best_document = content

    return best_document