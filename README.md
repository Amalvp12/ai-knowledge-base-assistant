# AI Knowledge Base Assistant

## Overview

AI Knowledge Base Assistant is a Retrieval-Augmented Generation (RAG) application built using FastAPI, PostgreSQL, and Google Gemini.

The system stores company knowledge documents, generates embeddings, retrieves the most relevant document using similarity search, and uses Gemini to generate accurate answers.

---

## Features

* FastAPI REST API
* Google Gemini Integration
* PostgreSQL Database
* Embedding Generation
* Similarity Search
* Retrieval-Augmented Generation (RAG)
* Question Answering System

---

## Technologies Used

* Python
* FastAPI
* PostgreSQL
* Google Gemini API
* NumPy
* Psycopg2

---

## Architecture

Documents
↓
Embeddings
↓
PostgreSQL
↓
Similarity Search
↓
Retrieved Context
↓
Gemini
↓
Answer

---

## Project Structure

app/

* main.py
* database.py
* embeddings.py
* retriever.py
* gemini_service.py
* load_documents.py
* store_embeddings.py

documents/

* company_overview.txt
* employee_handbook.txt
* faq.txt
* it_policy.txt

---

## Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key

DB_HOST=localhost
DB_NAME=ai_knowledge_base
DB_USER=postgres
DB_PASSWORD=your_password

---

## Installation

pip install -r requirements.txt

---

## Run Application

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

---

## Example Questions

* What are the working hours?
* What are the employee benefits?
* What is the password policy?
* How can I apply for leave?

---

## Future Improvements

* Document Chunking
* pgvector Integration
* PDF Upload Support
* Cloud Deployment
* Authentication
