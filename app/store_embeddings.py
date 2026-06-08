from app.database import conn, cursor
from app.embeddings import create_embedding

cursor.execute(
    """
    SELECT id, content
    FROM document_chunks
    """
)

rows = cursor.fetchall()

for row in rows:

    document_id = row[0]
    content = row[1]

    embedding = create_embedding(content)

    cursor.execute(
        """
        UPDATE document_chunks
        SET embedding = %s
        WHERE id = %s
        """,
        (str(embedding), document_id)
    )

conn.commit()

print("Embeddings Stored Successfully!")