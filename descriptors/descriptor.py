class Descriptor(object):

    def __init__(self, init=1):
        self.x = init

    def __get__(cls, obj, owner):
        return cls.x

    def __set__(cls, obj, value):
        print 'setting'
        cls.x = value

class Test(object):
    # descriptors should be cls attr
    d = Descriptor()

t = Test()

print t.d
t.d = 15
print t.d
t.d = 34
print t.d
