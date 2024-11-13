import openai
import os

openai.api_key=os.getenv('openai_api_key')

print(openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Name 10 cities to live in as a young adult: ",
        max_tokens=100))

