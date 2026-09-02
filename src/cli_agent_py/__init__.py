from google import genai
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def main():
    client = genai.Client(
        vertexai=True,
        project=os.getenv("GCP_PROJECT"),
        location="us-central1",
    )

    response = await client.aio.models.generate_content(
        contents=["Hi, gemini are you up?"], model="gemini-2.5-flash"
    )

    print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
