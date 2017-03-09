""" The simplest approach to factories in Python - static method"""
from random import choice
from abc import abstractmethod


class Animal(object):
    """Generic Animal class"""

    @abstractmethod
    def sound(self):
        """What sound does the animal produce?"""
        raise NotImplementedError()

    @staticmethod
    def factory(type):
        if type == "Dog": return Dog()
        if type == "Sheep": return Sheep()
        if type == "Duck": return Duck()
        raise TypeError("Unsupported type")


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Woof!"


class Sheep(Animal):
    """Sheep class"""

    def sound(self):
        return "Baaa!"


class Duck(Animal):
    """Duck class"""

    def sound(self):
        return "Quack!"

choices = [t.__name__ for t in Animal.__subclasses__()]
for i in range(10):
    a = Animal.factory(choice(choices))
    print a.sound()