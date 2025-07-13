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

messages.extend(
    [
        # Here is the assistant's response from the previous step
        # with the code. This gives it "memory" of the previous
        # interaction.
        {
            "role": "assistant", 
            "content": response
        },
   
        # Now, we can ask the assistant to update the function
        {
            "role": "user",
            "content": "Update the function to include documentation in `google style`."
        }
    ]
)
print(f"Second messages iteration:\n{messages}")

response = generate_responses(messages)
print(response)