from dotenv import load_dotenv
import os


# OpenAI authentication
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-3.5-turbo"

CHUNK_SIZE_1 = 10_000
CHUNK_OVERLAP_1 = 200

CHUNK_SIZE_2 = 1000
CHUNK_OVERLAP_2 = 100

TEMPERATURE_QUES = 0.3
TEMPERATURE_ANS = 0.1

HOST = "0.0.0.0"
PORT = 8080
