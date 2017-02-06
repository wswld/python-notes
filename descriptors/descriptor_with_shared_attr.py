class Descriptor(object):
    x = 0
    def __get__(cls, obj, owner):
        return cls.x
    def __set__(cls, obj, value):
        print('setting')
        cls.x = value

class Test(object):
    d = Descriptor()

t = Test()
t2 = Test()
print t.d
print t2.d
t.d = 1
print t.d
print t2.d
