"""This example is based on:
* http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html#abstract-factories
* https://en.wikipedia.org/wiki/Abstract_factory_pattern
"""

from random import choice
from abc import abstractmethod


class Button(object):
    """Abstract product"""

    @abstractmethod
    def draw(self):
        raise NotImplementedError()


class WinButton(Button):
    """Concrete product #1"""

    def draw(self):
        print "Render a button in a Windows style"


class OSXButton(Button):
    """Concrete product #2"""

    def draw(self):
        print "Render a button in an OSX style"


class GUIFactory(object):
    """Abstract factory"""

    @abstractmethod
    def create_button(self):
        raise NotImplementedError()


class WinFactory(GUIFactory):
    """Concrete factory #1"""

    def create_button(self):
        return WinButton()


class OSXFactory(GUIFactory):
    """Concrete factory #2"""

    def create_button(self):
        return OSXButton()


if __name__ == '__main__':
    # TODO(gva): Not sure about this part
    # Possibly there could be an App obj unaware of the OS that makes a call to the draw() method
    # Or am I getting into Java territory here?
    current_os = choice(['osx', 'win', 'linux'])
    factory = None
    if current_os == 'win':
        factory = WinFactory()
    elif current_os == 'osx':
        factory = OSXFactory()
    else:
        raise NotImplementedError('OS {} is not supported'.format(current_os))

    button = factory.create_button()
    button.draw()