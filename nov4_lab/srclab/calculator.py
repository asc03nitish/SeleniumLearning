class Calculator:

    def add(selfself, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # ✅ Match the test
        return a / b

    def power(self, a, b):
        return a ** b