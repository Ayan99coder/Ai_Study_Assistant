from langchain_core.prompts import PromptTemplate
from parsers.explaination_parser import explanation_parser

explanation_prompt = PromptTemplate(
    template="""
Explain the following topic.

Topic: {topic}
Difficulty: {difficulty}
Language: {language}

Explain according to the selected difficulty and language.

{format_instructions}
""",
    input_variables=["topic", "difficulty", "language"],
    partial_variables={
        "format_instructions": explanation_parser.get_format_instructions()
    }
)


quiz_prompt = PromptTemplate(

    template="""
Generate a quiz about the following topic.

Topic: {topic}
Difficulty: {difficulty}
Language: {language}

Generate 5 multiple-choice questions.

Each question must have:
- question
- 4 options
- correct answer

{format_instructions}
""",
    input_variables=[
        "topic",
        "difficulty",
        "language"
    ],
    partial_variables={
        "format_instructions": 'parser.get_format_instructions()'
    }
)
notes_prompt = PromptTemplate(
    template="""
You are an expert teacher.

Generate study notes about the following topic.

Topic: {topic}
Difficulty: {difficulty}
Language: {language}

Create clear and easy-to-understand notes.
Include:
1. Definition
2. Important concepts
3. Key points
4. Examples
5. Short summary

{format_instructions}
""",
    input_variables=[
        "topic",
        "difficulty",
        "language"
    ],
    partial_variables={
        "format_instructions": "{format_instructions}"
    }
)
mcq_prompt = PromptTemplate(
    template="""
You are an expert teacher.

Generate 5 multiple-choice questions about the following topic.

Topic: {topic}
Difficulty: {difficulty}
Language: {language}

Each question must contain:
- A question
- Exactly 4 options
- One correct answer

Make the questions suitable for the selected difficulty.

{format_instructions}
""",
    input_variables=[
        "topic",
        "difficulty",
        "language"
    ],
    partial_variables={
        "format_instructions": "{format_instructions}"
    }
)