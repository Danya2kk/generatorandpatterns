"""
5. Паттерн «Стратегия»
• Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
• Создайте несколько классов, каждый реализует определенную
стратегию математической операции, например, Addition,
Subtraction, Multiplication, Division. Каждый класс должен
содержать метод execute, который принимает два числа и
выполняет соответствующую операцию.
TeachMeSkills.by
• Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate, который
выполняет операцию с помощью текущей стратегии
"""


class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strat):
        self.strategy = strat

    def calculate(self, a, b):
        return self.strategy.execute(a, b)


class Addition:
    def execute(self, x, y):
        return x+y


class Subtraction:
    def execute(self, x, y):
        return x - y


class Multiplication:
    def execute(self, x, y):
        return x * y


class Division:
    def execute(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            print("На 0 делить нельзя!")


calculator = Calculator(Addition())
print(calculator.calculate(5, 3))

calculator.set_strategy(Multiplication())
print(calculator.calculate(5, 3))
