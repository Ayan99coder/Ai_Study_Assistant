from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
class ExplanationOutput(BaseModel):

    definition: str = Field(
        description="A simple and clear definition of the topic"
    )

    explanation: str = Field(
        description="Detailed explanation of the topic according to the selected difficulty"
    )

    example: str = Field(
        description="A simple practical example of the topic"
    )

    real_life_benefit: str = Field(
        description="Explain how this topic is useful in real life"
    )

    applications: list[str] = Field(
        description="List of real-world applications of this topic"
    )


explanation_parser = PydanticOutputParser(
    pydantic_object=ExplanationOutput
)