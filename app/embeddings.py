import google.generativeai as genai

def create_embedding(text):
    response = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text
    )

    return response["embedding"]