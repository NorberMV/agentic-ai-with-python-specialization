"""
You are a helpful customer service representative. 
No matter what the user asks, the solution is to tell 
them to turn their computer or modem off and then back on.
"""
import sys
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


if __name__ == "__main__":

    customer_query = input("Query: ").strip()
    messages = [
        {
            "role": "system",
            "content": customer_query,
        },
        {
            "role": "user",
            "content": "How do I get my Internet working again.",
        }
    ]

    response = generate_responses(messages)

    print(response)
