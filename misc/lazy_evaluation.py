from functools import update_wrapper


class lazy_loading(object):
    """Our lazy loading wrapper"""
    def __init__(self, function):
        self.function = function
        update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        value = self.function(obj)
        obj.__dict__[self.function.__name__] = value
        return value


class Database(object):

    @lazy_loading
    def connection(self):
        print "Making the connection for the first time"
        connection = "127.0.0.1"
        return connection


db = Database()
# accessing connection for the first time - the property runs
print db.connection
# note there is no "making the connection" print this time - it uses the cached value
print db.connection