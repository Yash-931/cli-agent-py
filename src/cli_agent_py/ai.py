from dotenv import load_dotenv
from google import genai
import os
import asyncio
from .tools import tool_registry
from google.genai import types

load_dotenv()

for name, tool in tool_registry.items():
    tool_name = name
    tool_declaration = tool["declaration"]

    types.FunctionDeclaration(
        name=tool_declaration["name"],
        description=tool_declaration["description"],
        parameters_json_schema={
            "type": "object",
            "properties": tool_declaration["parameters"],
            "required": tool_declaration["required"],
        },
    )


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
