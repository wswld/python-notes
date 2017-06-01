# Singleton through a metaclass. Requires Python 3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


l1 = Logger()
print(l1)
l2 = Logger()
print(l2)
l3 = Logger()
print(l3)