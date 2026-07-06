# Movie Information Extraction

This project uses a local AI model with Ollama and Instructor to extract movie information from text.

## Features
- Extract movie title
- Extract movie review
- Uses Pydantic schema for structured output
- Runs locally with Ollama

## Files
- api.py : FastAPI endpoints
- schema.py : Pydantic schema
- main.py : Typer CLI application
- ai extraction.py : Movie extraction logic

## Requirements

- Python 3.11
- Ollama
- Instructor
- Pydantic
- FastAPI

## Installation

```bash
pip install instructor fastapi pydantic typer
```

## Run

```bash
python "ai extraction.py"
```

## Example Input

```text
Inception is a mind-bending sci-fi movie by Nolan. Very confusing but brilliant.
```

## Example Output

```text
title='Inception'
review='A mind-bending sci-fi movie by Nolan. Very confusing but brilliant.'
```

## Author

Malak# project.py
