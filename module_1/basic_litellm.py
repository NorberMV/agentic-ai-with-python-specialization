from typing import List, Dict

from litellm import completion
from dotenv import load_dotenv


load_dotenv(override=True)


def generate_responses(messages: List[Dict]) -> str:
    """Call LLM to generate responses."""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024,
    )
    return response.choices[0].message.content


messages = [
    {
        "role": "system", 
        "content": "You are an expert software engineer that prefers functional programming."
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values of a dictionary."
    }
]

response = generate_responses(messages)
print(response)
 