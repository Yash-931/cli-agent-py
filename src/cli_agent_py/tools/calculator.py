def execute_calculator(a, b, op):
    if op == "add":
        return a + b

    elif op == "subtract":
        return a - b

    elif op == "multiply":
        return a * b

    else:
        if b == 0:
            raise Exception("Divsion by zero not possible")

        else:
            return a / b


calculator = {
    "declaration": {
        "name": "Calculator",
        "description": "Calculate a basic mathematical expression. Supports addition, multiplication, division, subtraction of two numbers. Can use this tool multiple times breaking a complex mathematical expression and solving it in parts",
        "parameters": {
            "a": {
                "type": "Number",
                "description": "The first number",
            },
            "b": {"type": "Number", "description": "The second number"},
            "op": {"type": "String", "description": "The operation to be performed"},
        },
        "required": ["a", "b", "op"]
    },

    "execute": execute_calculator
}
