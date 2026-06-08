from app.database import conn, cursor
files = [
    "documents/company_overview.txt",
    "documents/employee_handbook.txt",
    "documents/faq.txt",
    "documents/it_policy.txt"
]

for file_path in files:

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    cursor.execute(
        """
        INSERT INTO document_chunks (source_file, content)
        VALUES (%s, %s)
        """,
        (file_path, content)
    )

conn.commit()

print("Documents Loaded Successfully!")