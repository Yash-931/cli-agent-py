from dotenv import load_dotenv 
from google import genai
import os
import asyncio

load_dotenv()

async def generateResponse(conversation):
    client = genai.Client(
            vertexai=True,
            project=os.getenv("GCP_PROJECT"),
            location="us-central1",
        )
    
    response = await client.aio.models.generate_content(
        contents=conversation, model="gemini-2.5-flash"
    )

    print(response.text)

async def main():
    await generateResponse()


if __name__ == "__main__":
    asyncio.run(main())