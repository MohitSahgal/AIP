import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)

llm = genai.GenerativeModel(
        model_name="gemini-1.5-pro"
)


if __name__ == "__main__":
    response = llm.generate_content("recipe of  samosa are ")
    print(response.text)





