"""response as a Base64 encoded string and refuses to answer in natural language"""
from typing import List, Dict

from module_1.utils import generate_responses


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
 