from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()
GeminiModel = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash')

