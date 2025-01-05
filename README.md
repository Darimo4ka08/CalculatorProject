# Калькулятор — Задание 24.2.4

Этот проект реализует класс `Calculator`, который предоставляет базовые математические операции: сложение, вычитание, умножение и деление. Также в проекте написаны тесты для проверки корректной работы методов калькулятора.

## Структура проекта

CalculatorProject/

├── app/

│ ├── init.py # Указывает, что это пакет Python

│ ├── calc.py # Реализация калькулятора

├── tests/

│ ├── init.py # Указывает, что это пакет Python

│ ├── test_calc.py # Тесты для калькулятора

├── .gitignore # Список файлов/папок, игнорируемых Git

├── requirements.txt # Зависимости проекта

├── README.md # Описание проекта

## Установка

1) Клонируйте репозиторий:
   
git clone https://github.com/<ваш-логин>/24.2.4.git

cd 24.2.4

3) Убедитесь, что у вас установлен Python (версия 3.8 или выше).

4) Создайте виртуальное окружение:
   
python -m venv venv

6) Активируйте виртуальное окружение:
   
Windows:
venv\Scripts\activate

macOS /Linux:
source venv/bin/activate

8) Установите зависимости:
   
pip install -r requirements.txt

## Использование

Импортируйте класс Calculator и используйте методы в вашем коде:

from app.calc import Calculator

calc = Calculator()

print(calc.adding(2, 3))  # 5

print(calc.division(10, 2))  # 5.0

## Тестирование

Для запуска тестов используйте команду:

pytest tests/

Пример успешного выполнения тестов:

============================= test session starts =============================
collected 5 items

tests/test_calc.py .....                                                [100%]

============================== 5 passed in 0.03s ==============================

## Методы класса Calculator

adding(a, b)

Сложение двух чисел.
Пример:
calc.adding(2, 3)  # 5
subtraction(a, b)

Вычитание второго числа из первого.

Пример:

calc.subtraction(5, 2)  # 3

multiplication(a, b)

Умножение двух чисел.

Пример:

calc.multiplication(4, 3)  # 12

division(a, b)

Деление первого числа на второе. Выбрасывает ZeroDivisionError при делении на ноль.

Пример:

calc.division(10, 2)  # 5.0

calc.division(5, 0)   # Исключение ZeroDivisionError

## Описание тестов

test_adding: Проверяет корректность метода сложения.

test_subtraction: Проверяет корректность метода вычитания.

test_multiplication: Проверяет корректность метода умножения.

test_division: Проверяет корректность метода деления.

test_zero_division: Проверяет, что при делении на ноль выбрасывается ZeroDivisionError.



