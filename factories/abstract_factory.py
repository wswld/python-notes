"""This example is based on examples in https://en.wikipedia.org/wiki/Abstract_factory_pattern"""

from random import choice
from abc import abstractmethod


class Button(object):
    """Abstract product"""

    @abstractmethod
    def paint(self):
        raise NotImplementedError()


class WinButton(Button):
    """Concrete product #1"""

    def paint(self):
        print "Render a button in a Windows style"


class OSXButton(Button):
    """Concrete product #2"""

    def paint(self):
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
    # Possibly there could be an Application obj unaware of OS that makes a call to the paint() method
    current_os = choice(['osx', 'win', 'linux'])
    factory = None
    if current_os == 'win':
        factory = WinFactory()
    elif current_os == 'osx':
        factory = OSXFactory()
    else:
        raise NotImplementedError('OS {} is not supported'.format(current_os))

    button = factory.create_button()
    button.paint()