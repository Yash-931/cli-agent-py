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
    args_model: type[BaseModel]
    execute: Callable[..., float]
