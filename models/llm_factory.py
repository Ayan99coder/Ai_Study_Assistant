from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()
GeminiModel = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
local_model = HuggingFacePipeline.from_model_id(
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",

)
model = ChatHuggingFace(llm=local_model)
