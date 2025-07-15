"""
Building a Quasi-Agent
For practice, we are going to write a quasi-agent that can write Python functions based on user requirements. 
It isn’t quite a real agent, it can’t react and adapt, but it can do something useful for us.
The quasi-agent will ask the user what they want code for, write the code for the function, add documentation, 
and finally include test cases using the unittest framework. This exercise will help you understand how to 
maintain context across multiple prompts and manage the information flow between the user and the LLM. 
It will also help you understand the pain of trying to parse and handle the output of an LLM that is not always consistent.
"""
import os

from litellm import completion

from .utils import extract_xml


os.environ["HF_TOKEN"] = os.environ["HF_TOKEN"]


quasi_agent_sys_prompt = """You are a software engineer agent, expert in generate Python code. 
Your main goal is to chat with users to help them with their coding requirements.
<Task>
- Greet the user.
- Ask the user what function he wants to create.
- Analyze the user code requirements.
- Write a basic Python function based on the user’s description.
- Follow the format below to answer.
</Task>

<Format>
Use the following xml tags to format your answer:
<code> (Include this tag Only if the answer requires code generation)
```Python
# Here the generated Python code based on the user's descriptions.
```
</code>

<text>
Here the text part of the answer like a chat message, or analysis of the generated code.
</text>
</Format>
"""


def llm_call(messages: list[dict[str, str]]):
    # Call DeepSeek-R1 model through Together AI
    response = completion(
        model="huggingface/together/deepseek-ai/DeepSeek-V3",
        messages=messages,
    )
    return response.choices[0].message.content


messages = [
    {
        "content": quasi_agent_sys_prompt, 
        "role": "system"
    },
    {
        "role": "user",
        "content": None,
    },
]


if __name__ == "__main__":

    query = input("Query: ").strip()
    messages[1]["content"] = query
 
    response = llm_call(messages)
    first_utterance = extract_xml(response, 'text')

    print(first_utterance)

    follow_up = input("User: ")
    message = {
        "role": "user",
        "content": follow_up,
    }
    messages.append(message)
    # print(f"Final messages:\n{messages}")
    response = llm_call(messages)

    second_utterance_text = extract_xml(response, 'text')
    second_utterance_code = extract_xml(response, 'code')

    print(f"{second_utterance_text}\n{second_utterance_code}")

    follow_up = input("User: ")
    message = {
        "role": "user",
        "content": follow_up,
    }

    messages.append(message)
    response = llm_call(messages)

    third_utterance_text = extract_xml(response, 'text')
    third_utterance_code = extract_xml(response, 'code')

    print(f"{third_utterance_text}\n{third_utterance_code}")
