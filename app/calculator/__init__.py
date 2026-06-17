from app.calculation import CalculationFactory


class Calculator:
    def __init__(self):
        self.history = []
        self.operations = ["add", "subtract", "multiply", "divide"]

    def get_number(self, prompt):
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print(f"  Invalid input '{value}'. Please enter a number.")

    def show_help(self):
        print("\nAvailable commands:")
        print("  add, subtract, multiply, divide - perform a calculation")
        print("  history - show past calculations")
        print("  help - show this message")
        print("  exit - quit the calculator\n")

    def show_history(self):
        if not self.history:
            print("  No calculations yet.\n")
            return
        print("\nCalculation history:")
        for item in self.history:
            print(f"  {item}")
        print("")

    def run(self):
        print("=" * 40)
        print("  Welcome to the Python Calculator!")
        print("  Type 'help' for commands or 'exit' to quit.")
        print("=" * 40)

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                self.show_help()
                continue

            if command == "history":
                self.show_history()
                continue

            if command not in self.operations:
                print(f"  Unknown command '{command}'. Type 'help' for options.")
                continue

            a = self.get_number("Enter first number: ")
            b = self.get_number("Enter second number: ")

            try:
                calculation = CalculationFactory.create(command, a, b)
                result = str(calculation)
                self.history.append(result)
                print(f"  Result: {result}\n")
            except ValueError as e:
                print(f"  Error: {e}\n")