from app.operation import Addition, Subtraction, Multiplication, Division


class Calculation:
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b

    def perform(self):
        operations = {
            "add": Addition,
            "subtract": Subtraction,
            "multiply": Multiplication,
            "divide": Division,
        }
        return operations[self.operation].execute(self.a, self.b)

    def __str__(self):
        symbols = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
        return f"{self.a} {symbols[self.operation]} {self.b} = {self.perform()}"


class CalculationFactory:
    valid_operations = ["add", "subtract", "multiply", "divide"]

    @classmethod
    def create(cls, operation, a, b):
        if operation not in cls.valid_operations:
            raise ValueError(f"Unknown operation: {operation}")
        return Calculation(operation, a, b)