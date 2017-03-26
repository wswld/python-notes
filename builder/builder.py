# loosely based on https://en.wikipedia.org/wiki/Builder_pattern
from abc import abstractmethod
# TODO: Get rid of color and add seats. Make two builders TruckBulder and BusBuilder with 16/2 and 8/40 ratios


class Car(object):

    def __init__(self):
        self.wheels = None
        self.color = None

    def __repr__(self):
        return '<Car obj. w/ {0.wheels} wheels and color {0.color}>'.format(self)


class Builder(object):
    """Abstract Builder class"""

    product_class = None

    def __init__(self):
        self.product = self.product_class()

    @abstractmethod
    def set_wheels(self, number):
        raise NotImplementedError()

    @abstractmethod
    def set_color(self, color):
        raise NotImplementedError()

    @property
    def result(self):
        return self.product


class CarBuilder(Builder):

    product_class = Car

    def set_wheels(self, number):
        self.product.wheels = number

    def set_color(self, color):
        self.product.color = color


class CarBuilderDirector(object):
    """This is a nod to GOF, I'm not sure we really need this part in Python
    We could as well add a construct method to abstract builder? Couldn't we?
    """

    builder = CarBuilder

    def construct(self):
        builder = self.builder()
        builder.set_wheels(4)
        builder.set_color('green')
        return builder.result

director = CarBuilderDirector()
car = director.construct()
print(car)
