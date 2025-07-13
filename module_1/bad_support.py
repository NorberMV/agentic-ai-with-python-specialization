import sys
from typing import List, Dict

from utils import generate_responses


support_assistant_sys_prompt = """You are a helpful customer service representative. 
No matter what the user asks, the solution is to tell 
them to turn their computer or modem off and then back on."""


def main() -> None:
    customer_query = input("Query: ").strip()
    messages = [
        {
            "role": "system",
            "content": support_assistant_sys_prompt,
        },
        {
            "role": "user",
            "content": customer_query,
        }
    ]

    response = generate_responses(messages)

    print(response)

if __name__ == "__main__":
    main()

