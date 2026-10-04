# AI Study Assistant

AI Study Assistant is a command-line learning tool that uses LangChain and
Google Gemini to create structured, personalized learning content from a
student's topic.

## Features

- Enter any study topic from the terminal.
- Select a difficulty level to adjust the response:
  - Beginner
  - Intermediate
  - Advanced
- Select a response language:
  - English
  - Roman Urdu
  - Simple English
- Choose one of three learning modes:
  - **Explain Topic** - Provides a definition, detailed explanation, practical
    example, real-life benefit, and applications.
  - **Generate Notes** - Creates a definition, important concepts, key points,
    examples, and a short summary.
  - **Generate Quiz** - Creates five multiple-choice questions with four
    options per question and the correct answers.
- Parse Gemini responses into predictable Pydantic models for structured output.
- Route each request to the matching LangChain workflow with a conditional
  runnable.

## Project structure

```text
Ai_Study_Assistant/
├── chains/                    # Explanation, notes, and quiz pipelines
├── models/                    # Gemini model configuration
├── parsers/                   # Pydantic structured-output schemas
├── prompts/                   # Prompt templates for each learning mode
├── runnables/                 # Conditional workflow routing
├── main.py                    # Command-line entry point
├── .env.example               # Example environment configuration
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

## How it works

1. `main.py` collects the topic, output type, difficulty, and language.
2. Prompt templates prepare the request for the selected learning mode.
3. `RunnableBranch` routes the request to the explanation, notes, or quiz
   chain.
4. Google Gemini generates the content.
5. A Pydantic output parser validates and structures the response.

## Contributing

1. Create a feature branch.
2. Make and test your changes.
3. Update this README when setup steps, features, or project structure change.
4. Commit and push the changes.
