from pydantic import BaseModel
from typing import Literal
from .models import ToolDeclaration, ToolSpec, ParamSpec


class CalculatorArgs(BaseModel):
    a: float
    b: float
    op: Literal["add", "subtract", "divide", "multiply"]


def execute_calculator(a: float, b: float, op: str):
    if op == "add":
        return a + b

    elif op == "subtract":
        return a - b

    elif op == "multiply":
        return a * b

    elif op == "divide":
        if b == 0:
            raise ValueError("Divsion by zero not possible")

        else:
            return a / b
    else:
        raise TypeError("Incorrect operator passsed")


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
    args_model=CalculatorArgs,
)
