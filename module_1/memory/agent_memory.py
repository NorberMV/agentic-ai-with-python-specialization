"""Including previous responses to the messages list for continuity."""
from module_1.utils import generate_responses


messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming."
    },
    {
        "role": "user",
        "content": "Write a function to swap keys and values in a dictionary."
    }
]

response = generate_responses(messages)
print(response)
