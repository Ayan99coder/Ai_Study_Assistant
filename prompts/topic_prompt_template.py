from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(template="Explain this {topic} in",input_variables=['topic'])