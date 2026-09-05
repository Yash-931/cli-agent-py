from .calculator import calculator
from .models import ToolSpec

tool_registry: dict[str, ToolSpec] = {"calculator": calculator}
