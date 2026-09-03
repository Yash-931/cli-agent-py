from .calculator import calculator, ToolSpec

tool_registry: dict[str, ToolSpec] = {
    "calculator": calculator
}
