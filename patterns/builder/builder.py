# loosely based on https://en.wikipedia.org/wiki/Builder_pattern
from abc import abstractmethod


class Car(object):

    def __init__(self):
        self.type = None
        self.wheels = None
        self.seats = None

    def __repr__(self):
        return '<Car {0.type} obj. w/ {0.wheels} wheels and color {0.seats}>'.format(self)


class Builder(object):
    """Abstract Builder class"""

    product_class = None

    def __init__(self):
        self.product = self.product_class()

    @abstractmethod
    def set_type(self, name):
        raise NotImplementedError()

    @abstractmethod
    def set_wheels(self, number):
        raise NotImplementedError()

    @abstractmethod
    def set_seats(self, seats):
        raise NotImplementedError()

    @property
    def result(self):
        return self.product


class CarBuilder(Builder):

    product_class = Car

    def set_type(self, name):
        self.product.type = name

    def set_wheels(self, number):
        self.product.wheels = number

    def set_seats(self, seats):
        self.product.seats = seats


class CarDirector(object):
    """This is a nod to GOF, I'm not sure we really need this part in Python
    We could as well add a construct method to abstract builder? Couldn't we?
    """

    builder = CarBuilder

    def construct(self):
        builder = self.builder()
        builder.set_type('car')
        builder.set_wheels(4)
        builder.set_seats(4)
        return builder.result


class BusDirector(object):

    builder = CarBuilder

    def construct(self):
        builder = self.builder()
        builder.set_type('bus')
        builder.set_wheels(8)
        builder.set_seats(40)
        return builder.result


class TruckDirector(object):

    builder = CarBuilder

    def construct(self):
        builder = self.builder()
        builder.set_type('truck')
        builder.set_wheels(16)
        builder.set_seats(2)
        return builder.result


director = CarDirector()
car = director.construct()
print(car)

director = BusDirector()
car = director.construct()
print(car)

director = TruckDirector()
car = director.construct()
print(car)
