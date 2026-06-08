# AI Knowledge Base Assistant

## Overview
AI Knowledge Base Assistant is a Retrieval-Augmented Generation (RAG) application built using FastAPI, PostgreSQL, and Google Gemini.

## Features
- Document Storage
- Embedding Generation
- PostgreSQL Database
- Similarity Search
- RAG-based Question Answering

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- Gemini API
- NumPy
- Psycopg2

## Architecture

Documents
↓
Embeddings
↓
PostgreSQL
↓
Retrieval
↓
Gemini
↓
Answer

## Run Project

Create virtual environment:

pip install -r requirements.txt

Run:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs