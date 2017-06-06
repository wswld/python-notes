""" Simplest possible decorator example """
def decorator(f):
    def inner(*args, **kwargs):
        return f(*args, **kwargs)*3
    return inner

@decorator
def func(a):
    return a

print func(5)
print func('string')
print func(('key', 'value'))
