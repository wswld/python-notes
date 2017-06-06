"""Simplest possible form of descriptor object"""

class Descriptor(object):

    def __init__(self, init=1):
        self.x = init

    def __get__(self, obj, obj_cls):
        return self.x

    def __set__(self, obj, value):
        print 'setting to {}'.format(value)
        self.x = value

class Test(object):
    # descriptors should be cls attr
    d = Descriptor()

t = Test()

print t.d
t.d = 15
print t.d
t.d = 34
print t.d
