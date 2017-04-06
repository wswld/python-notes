""" Loosely based on https://github.com/bottlepy/bottle/blob/cafc15419cbb4a6cb748e6ecdccf92893bb25ce5/bottle.py#L270 """


# TODO: Add class variant to descriptors
class lazy_loading(object):
    """Our lazy loading descriptor"""
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, type_):
        if obj is None: return self
        # it looks the way it looks - we overwrite the original decorated function w/ simple attribute
        value = obj.__dict__[self.function.__name__] = self.function(obj)
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