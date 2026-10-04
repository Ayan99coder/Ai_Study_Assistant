from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
class QuizQuestion(BaseModel):
    question: str = Field(
        description="The multiple-choice question"
    )

    options: list[str] = Field(
        description="Exactly 4 options"
    )

    correct_answer: str = Field(
        description="The correct answer"
    )


class QuizOutput(BaseModel):
    questions: list[QuizQuestion] = Field(
        description="Exactly 5 multiple-choice questions"
    )

    answers: list[str] = Field(
        description="Answers to all 5 questions in the same order"
    )


quiz_parser = PydanticOutputParser(
    pydantic_object=QuizOutput
)