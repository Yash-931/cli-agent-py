from dotenv import load_dotenv
from google import genai
import os
from .tools import tool_registry
from .tools.calculator import ToolDeclaration
from google.genai import types
import asyncio

load_dotenv()

func_delarations = []

for name, tool in tool_registry.items():
    tool_declaration: ToolDeclaration = tool.declaration

    func = types.FunctionDeclaration(
        name=tool_declaration.name,
        description=tool_declaration.description,
        parameters_json_schema={
            'type': 'object',
            'properties': tool_declaration.parameters,
            'required': tool_declaration.required
        }
    )

    func_delarations.append(func)

tools = types.Tool(function_declarations=func_delarations)

async def generateResponse(conversation: list[types.Content]):
    client = genai.Client(
        vertexai=True,
        project=os.getenv("GCP_PROJECT"),
        location="us-central1",
    )

    response = await client.aio.models.generate_content(
        contents=conversation, model="gemini-2.5-flash", config=types.GenerateContentConfig(tools=[tools])
    )

    model_conversation = types.Content(
        role='model',
        parts=response.parts
    )
    
    conversation.append(model_conversation)
    print(response.text)


