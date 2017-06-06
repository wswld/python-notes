# Singleton through a decorator.


def singleton(class_):
  instances = {}

  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance


@singleton
class MyClass(object):
  pass

m1 = MyClass()
print(m1)
m2 = MyClass()
print(m2)
m3 = MyClass()
print(m3)