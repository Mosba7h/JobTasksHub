
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")