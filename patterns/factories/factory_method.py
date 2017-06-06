""" Simple factory method is through a static method of a class
Loosely based on: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html#simple-factory-method
"""
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
        if type == "dog": return Dog()
        if type == "sheep": return Sheep()
        if type == "pig": return Pig()
        raise TypeError("Unsupported type")


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Woof!"


class Sheep(Animal):
    """Sheep class"""

    def sound(self):
        return "Baaa!"


class Pig(Animal):
    """Pig class"""

    def sound(self):
        return "Oink!"

choices = [t.__name__.lower() for t in Animal.__subclasses__()]
for i in range(10):
    a = Animal.factory(choice(choices))
    print a.sound()