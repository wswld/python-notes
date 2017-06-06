"""This decorator counts function executions."""
def decorator(f):
    def inner(*args, **kwargs):
        inner.count += 1
        print "exec #{}".format(inner.count)
        return f(*args, **kwargs)
    inner.count = 0
    return inner

@decorator
def func(x):
    print x

func(5)
func(2)
func(-3)
