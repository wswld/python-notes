# Simplest possible variant


class Singleton(object):
    __instance = None

    def __init__(self, a):
        self.a = a

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

s1 = Singleton(a=1)
print s1.a
s2 = Singleton(a=2)
print s2.a
print s1.a