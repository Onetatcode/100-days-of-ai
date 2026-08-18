"""
Day 01 — First Tool-Calling Agent (raw API, no framework)

The point of today is to see the full agent loop with nothing hidden:
  1. We tell the model what tools exist (as a JSON schema).
  2. The model decides: answer directly, or call a tool.
  3. If it calls a tool, WE run the actual code and send the result back.
  4. The model uses that result to form its final answer.

Run:
    python agent.py
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

MODEL = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.3-70b-instruct")


# --- Step 1: Define your tools as real Python functions ---------------

def calculator(expression: str) -> str:
    """Safely evaluate a basic arithmetic expression."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "Error: expression contains disallowed characters."
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"


def word_count(text: str) -> str:
    """Count the number of words in a piece of text."""
    return str(len(text.split()))


# --- Step 2: Describe your tools to the model (JSON schema) -----------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression, e.g. '4821 * 17'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A math expression using + - * / ( )",
                    }
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "word_count",
            "description": "Count the number of words in a piece of text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to count words in.",
                    }
                },
                "required": ["text"],
            },
        },
    },
]

# Map tool name -> actual Python function to call
AVAILABLE_TOOLS = {
    "calculator": calculator,
    "word_count": word_count,
}


def run_agent(user_message: str):
    messages = [{"role": "user", "content": user_message}]

    # First call: let the model see the tools and decide what to do
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
    )

    msg = response.choices[0].message
    messages.append(msg)

    # Step 3: if the model asked to call a tool, run it for real
    if msg.tool_calls:
        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"[agent] calling tool: {name}({args})")

            if name in AVAILABLE_TOOLS:
                result = AVAILABLE_TOOLS[name](**args)
            else:
                result = f"Error: unknown tool {name}"

            # Step 4: send the tool result back so the model can finish
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )

        final = client.chat.completions.create(model=MODEL, messages=messages)
        return final.choices[0].message.content

    # No tool needed — model answered directly
    return msg.content


if __name__ == "__main__":
    print("Day 01 agent — type a question (or 'quit')\n")
    while True:
        q = input("you> ").strip()
        if q.lower() in ("quit", "exit"):
            break
        answer = run_agent(q)
        print(f"agent> {answer}\n")
