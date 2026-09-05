from dotenv import load_dotenv
from google import genai
import os
from .tools import tool_registry
from .tools.calculator import ToolDeclaration
from google.genai import types
from typing import Optional

load_dotenv()

func_delarations = []

for name, tool in tool_registry.items():
    tool_declaration: ToolDeclaration = tool.declaration

    func = types.FunctionDeclaration(
        name=tool_declaration.name,
        description=tool_declaration.description,
        parameters_json_schema={
            "type": "object",
            "properties": tool_declaration.parameters,
            "required": tool_declaration.required,
        },
    )

    func_delarations.append(func)

tools = types.Tool(function_declarations=func_delarations)


async def generateResponse(conversation: list[types.Content]):
    n: int = 10
    client = genai.Client(
        vertexai=True,
        project=os.getenv("GCP_PROJECT"),
        location="us-central1",
    )

    while n > 0:
        response = await client.aio.models.generate_content(
            contents=conversation,
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(tools=[tools]),
        )

        model_conversation = types.Content(role="model", parts=response.parts)

        conversation.append(model_conversation)

        tool_calls: Optional[list[types.FunctionCall]] = response.function_calls
        if tool_calls is not None:
            for call in tool_calls:
                tool_name: Optional[str] = call.name
                tool_args = call.args
                result = None
                error = None
                if (
                    tool_name is not None
                    and tool_args is not None
                    and tool_name in tool_registry
                ):
                    try:
                        spec = tool_registry[tool_name]
                        validated_args = spec.args_model.model_validate(tool_args)
                        result = spec.execute(**validated_args.model_dump())

                    except Exception as e:
                        error = str(e)

                else:
                    error = (
                        "Unrecognized tool or arguments not present in tool registry"
                    )

                tool_response = types.Content(
                    role="user",
                    parts=[
                        types.Part(
                            function_response=types.FunctionResponse(
                                name=tool_name,
                                response={"output": result, "error": error},
                            )
                        )
                    ],
                )

                conversation.append(tool_response)

        else:
            print((response.text or "").strip())
            return

        n = n - 1

    print(
        "Sorry the max limit of tool calls reached. Please try again later with simpler instructions",
    )
