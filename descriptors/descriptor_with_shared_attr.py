class Descriptor(object):
    x = 0

    def __get__(self, obj, owner):
        return self.x
    def __set__(self, obj, value):
        print('setting')
        self.x = value

class Test(object):
    d = Descriptor()

t = Test()
t2 = Test()
print t.d
print t2.d
t.d = 1
print t.d
print t2.d
