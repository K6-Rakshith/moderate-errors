# Complex calculator with moderate errors
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        # Error: No zero division check
        return a / b

def main():
    calc = Calculator()
    print("Add:", calc.add(10))  # Error: missing argument
    print("Subtract:", calc.subtract(10, 5))
    print("Multiply:", calc.multiply(10, "5"))  # Error: str instead of int
    print("Divide:", calc.divide(10, 0))  # Error: ZeroDivisionError

if __name__ == "__main__":
    main()
