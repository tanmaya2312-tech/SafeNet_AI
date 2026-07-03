import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read the API key
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")