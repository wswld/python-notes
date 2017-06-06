# Descriptors could be used as validators
import re


class DescriptorValidator(object):

    def __get__(self, obj, obj_cls):
        return self.x

    def __set__(self, obj, value):
        self.validate(value)
        self.x = value

    def validate(self, value):
        # raise some exception if not validated
        pass


class RegexValidator(DescriptorValidator):

    def __init__(self, regexp):
        self.regexp = regexp

    def validate(self, value):
        if not re.match(self.regexp, value):
            raise ValueError("{} doesn't match: {}".format(value, str(self.regexp)))
        else:
            print 'Validated {} w/ regexp {}'.format(value, str(self.regexp))


class Site(object):
    # This is not the perfect URL regexp out there, but it'll do
    url = RegexValidator(regexp='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    def __init__(self, name, url):
        self.name = name
        self.url = url

s1 = Site('first', 'http://first.com')
s2 = Site('second', 'https://second.co.uk')
s3 = Site('third', '###')