from .ai import generateResponse
from google.genai import types
import asyncio

async def main():
    conversation: list[types.Content] = []
    print("Agent is running...")
    while True:
        user_input = input("You: ")

        if user_input == "/exit":
            print("Goodbye!")
            break

        user_message = types.Part(text=user_input)
        user_conversation = types.Content(
            role='user',
            parts=[user_message]
        )

        conversation.append(user_conversation)


        print("Agent: ", end="")
        await generateResponse(conversation)


def run():
    asyncio.run(main())
