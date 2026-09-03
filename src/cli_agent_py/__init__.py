from .ai import generateResponse

async def main():
    conversation = []
    print("Agent is running...")
    while True:
        user_input = input("You: ")

        if user_input == "/exit":
            break

        user_conversation = {"role": "user", "content": user_input}
        conversation.append(user_conversation)

        await generateResponse(conversation)

        
