# Not a singleton per se, but a very similar (albeit more pyhtonic) pattern.


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

b1 = Borg()
b2 = Borg()

b1.a = 5
print b1.a
print b2.a

b1.a = 10
print b1.a
print b2.a