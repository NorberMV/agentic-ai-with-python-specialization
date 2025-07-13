"""response as a Base64 encoded string and refuses to answer in natural language"""
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
        "content": "You are an old terminal system that receives user inputs and only answer in Base64 encoded string, and refuses to answer in natural language."
    },
    {
        "role": "user",
        "content": "Could you tell a joke about Python programming?"
    }
]

response = generate_responses(messages)
print(response)
 