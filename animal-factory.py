"""
4. Паттерн «Фабричный метод»
• Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
• Создайте классы Dog и Cat, которые наследуют от Animal и
реализуют метод speak.
• Создайте класс AnimalFactory, который использует паттерн
«Фабричный метод» для создания экземпляра Animal. Этот
класс должен иметь метод create_animal, который принимает
строку («dog» или «cat») и возвращает соответствующий
объект (Dog или Cat).
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f'Гав-гав-гав'


class Cat(Animal):
    def speak(self):
        return f'Мяу-мяу'


class AnimalFactory:
    def create_animal(self, animal):
        if animal == "dog":
            return Dog()
        elif animal == "cat":
            return Cat()
        else:
            raise ValueError("Неверый ввод")


factory = AnimalFactory()
animal1 = factory.create_animal('dog')
animal2 = factory.create_animal('cat')

print(animal1.speak())
print(animal2.speak())
