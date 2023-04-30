from your_module_name import Calculator

class TestCalculator:
    def test_addition(self):
        num1 = 10
        num2 = 5
        calc = Calculator(num1, num2)
        assert calc.add() == num1 + num2

    def test_subtraction(self):
        num1 = 10
        num2 = 5
        calc = Calculator(num1, num2)
        assert calc.subtract() == num1 - num2

    def test_multiplication(self):
        num1 = 10
        num2 = 5
        calc = Calculator(num1, num2)
        assert calc.multiply() == num1 * num2

    def test_division(self):
        num1 = 10
        num2 = 5
        calc = Calculator(num1, num2)
        assert calc.divide() == num1 / num2
