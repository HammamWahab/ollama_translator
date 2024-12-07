# LLM Pipeline for Language Translation

This project provides a Python script to translate texts and check if the translations are acceptable. It uses the **ollama** API for translations and employs **pydantic** for data validation.

## Features

- Load discharge instructions from a JSONL file.
- Translate text from English to German using a language model.
- Review translations for acceptability.
- Process multiple translations in parallel for speed.

## Requirements

- Python 3.8+
- Libraries: `datasets`, `pydantic`, `ollama`, `tqdm`
- Access to the **ollama** API (e.g., `llama3.1` model).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt 
   ``` 

2. On `main.py` change the data path, and load your desired data to translate 
3. Run `python3 main.py` 


## How It Works
- Load Dataset: Reads discharge instructions from the JSONL file.
- Translate: Generates German translations using the ollama API.
- Review: Checks if the translation is acceptable.
- Output: Combines the translation and review result.