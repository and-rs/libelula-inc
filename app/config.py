import os

from dotenv import load_dotenv

is_dotenv_loaded = load_dotenv()
print(f"Is Dotenv loaded? {is_dotenv_loaded}")

# example
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables or .env file. Please ensure it's set."
    )
else:
    print(f"Loaded api key ending with {GEMINI_API_KEY[:5]}")
