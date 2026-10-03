# AI Study Assistant

AI Study Assistant is a command-line learning tool that uses LangChain and
Google Gemini to explain study topics in a structured format.

## Features

- Choose a study topic from the terminal.
- Select a difficulty level:
  - Beginner
  - Intermediate
  - Advanced
- Select an output language:
  - English
  - Roman Urdu
  - Simple English
- Receive a structured response containing:
  - Definition
  - Detailed explanation
  - Practical example
  - Real-life benefit
  - Applications

## Project structure

```text
Ai_Study_Assistant/
├── chains/                  # LangChain pipelines
├── models/                  # LLM configuration
├── parsers/                 # Structured output schemas
├── prompts/                 # Prompt templates
├── main.py                  # Command-line entry point
├── .env.example             # Example environment configuration
└── README.md
```

## Requirements

- Python 3.10 or newer
- A Google Gemini API key

Install the required packages:

```bash
pip install langchain-core langchain-google-genai langchain-huggingface \
python-dotenv pydantic
```

## Configuration

Create a `.env` file in the project root and add your Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Never commit `.env` or any API key to GitHub. The repository ignores local
environment files by default.

## Run the application

From the project root, run:

```bash
python main.py
```

Then follow the prompts in the terminal.

## Current status

The explanation workflow is implemented with Gemini and structured Pydantic
output parsing. The command-line menu includes options for explanations,
quizzes, and notes; quiz and notes workflows are planned for a future update.

## Contributing

1. Create a feature branch.
2. Make and test your changes.
3. Update this README when setup steps, features, or project structure change.
4. Commit and push the changes.
