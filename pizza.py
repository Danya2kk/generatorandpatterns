"""
3. Паттерн «Строитель»
• Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon.
• Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
• Создайте класс PizzaDirector, который принимает экземпляр
PizzaBuilder и содержит метод make_pizza, который
использует PizzaBuilder для создания Pizza.
"""


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def __str__(self):
        return f"Пицца: {self.size}, {self.cheese}, {self.pepperoni}, {self.mushrooms}, {self.onions}, {self.bacon}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions):
        self.pizza.onions = onions
        return self

    def set_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

    def get_pizza(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, director):
        self.director = director

    def make_pizza(self):
        return self.director.get_pizza()


builder = PizzaBuilder()
director = PizzaDirector(builder)
director.director.set_size('35 см').set_cheese('Моцарелла').set_pepperoni('Пепперони 100г').set_mushrooms('Какието грибы').set_onions("Какието онионсы").set_bacon('Вкусный бекон')
pizza = director.make_pizza()
print(pizza)