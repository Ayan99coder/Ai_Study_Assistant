from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class NotesOutput(BaseModel):

    definition: str = Field(
        description="A clear and simple definition of the topic"
    )

    important_concepts: list[str] = Field(
        description="Important concepts related to the topic, explained briefly"
    )

    key_points: list[str] = Field(
        description="Important points that the student should remember"
    )

    examples: list[str] = Field(
        description="Simple practical examples that help understand the topic"
    )

    short_summary: str = Field(
        description="A short and easy-to-understand summary of the topic"
    )


notes_parser = PydanticOutputParser(
    pydantic_object=NotesOutput
)