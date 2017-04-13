""" This is my take at Prototype. I'm not exactly satisfied with stuff I've seen over the web:

1. Some of the solutions introduce a factory/cache into the mix (too complex for such basic idea)
2. Also there is a suggestion to use simply deepcopy/copy on an object omitting the OOP boilerplate

With my implementation I want to take somewhat middle ground. Let me know if there's something wrong with this design.
"""

from copy import deepcopy


class Prototype(object):

    def clone(self):
        return deepcopy(self)


class ConcretePrototype1(Prototype):

    def __init__(self):
        self.name = 'Bear'


class ConcretePrototype2(Prototype):
    def __init__(self):
        self.name = 'Bull'


c1 = ConcretePrototype1()
c2 = ConcretePrototype2()
c1c = c1.clone()
c2c = c2.clone()

print c1.name
print c2.name
print c1c.name
print c2c.name
