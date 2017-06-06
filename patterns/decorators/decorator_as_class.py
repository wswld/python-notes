""" Kinda loosely based on:
http://stackoverflow.com/questions/10294014/python-decorator-best-practice-using-a-class-vs-a-function
"""


class foo(object):
    """No camel case. Living on the edge."""

    def __init__(self, function):
        print "Initiated decorator on {}".format(function.__name__)
        self.function = function

    def __call__(self):
        print "Calling {}".format(self.function.__name__)
        return self.function()*2


@foo
def bar():
    print "Now bar() is officially running."
    return 5

print bar()
