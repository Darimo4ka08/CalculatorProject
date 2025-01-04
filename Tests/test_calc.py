import pytest
from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    # Позитивный тест на сложение
    def test_adding(self):
        assert self.calc.adding(2, 3) == 5

    # Позитивный тест на вычитание
    def test_subtraction(self):
        assert self.calc.subtraction(5, 3) == 2

    # Позитивный тест на умножение
    def test_multiplication(self):
        assert self.calc.multiplication(4, 3) == 12

    # Позитивный тест на деление
    def test_division(self):
        assert self.calc.division(10, 2) == 5.0

    # Позитивный тест на деление на ноль
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(5, 0)
