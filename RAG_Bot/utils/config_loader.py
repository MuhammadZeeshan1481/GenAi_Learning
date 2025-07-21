import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def get_hf_token() -> str:
    return os.getenv("HUGGINGFACEHUB_API_TOKEN")
