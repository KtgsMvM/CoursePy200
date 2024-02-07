class Calculator:
    #class_attr =
    def __init__(self, calculator_add, calculator_mul):  # TODO написать статические методы

    # @classmethod
    # def calculator(cls, *args):
    # calculator.add = Calculator(cls)
    #     cls.first_digite()

    @staticmethod
    def add_method(self, a, b):
        self.a = a
        self.b = b
        return a + b

    @staticmethod
    def mul_method(self, a, b):
        return a * b

if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
