import json

from utils import generate_responses


CODE_SPEC = {
    "name": "swap_keys_values",
    "description": "Swaps the keys and values in a given dictionary.",
    "params": {
        "d": "A dictionary with unique values."
    },
}


def main() -> None:

    messages = [
        {
            "role": "system",
            "content": "You are an expert software engineer that writes clean code. You always document your functions.",
        },
        {
            "role": "user",
            "content": f"Please implement:\n{json.dumps(CODE_SPEC)}.",
        }
    ]

    response = generate_responses(messages)

    print(response)

if __name__ == "__main__":
    main()
