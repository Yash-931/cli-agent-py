from pydantic import BaseModel
from typing import Literal, Callable


class ParamSpec(BaseModel):
    type: Literal["string", "number", "boolean"]
    description: str


class ToolDeclaration(BaseModel):
    name: str
    description: str
    required: list[str]
    parameters: dict[str, ParamSpec]


class ToolSpec(BaseModel):
    declaration: ToolDeclaration
    execute: Callable[..., float]


def execute_calculator(a: float, b: float, op: str):
    if op == "add":
        return a + b

    elif op == "subtract":
        return a - b

    elif op == "multiply":
        return a * b

    else:
        if b == 0:
            raise ValueError("Divsion by zero not possible")

        else:
            return a / b


calculator = ToolSpec(
    declaration=ToolDeclaration(
        name="calculator",
        description="Calculate a basic mathematical expression. Supports addition, multiplication, division, subtraction of two numbers. Can use this tool multiple times breaking a complex mathematical expression and solving it in parts",
        parameters={
            "a": ParamSpec(type="number", description="The first number"),
            "b": ParamSpec(type="number", description="The second number"),
            "op": ParamSpec(
                type="string", description="The operation needed to be performed"
            ),
        },
        required=["a", "b", "op"],
    ),
    execute=execute_calculator,
)
