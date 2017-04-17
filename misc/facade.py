""" Based on https://en.wikipedia.org/wiki/Facade_pattern"""

# A bunch o classes with complicated logic

class Subsystem(object):

    def complex_method_one(self):
        print("Running {}.complex_method_one".format(self.__class__.__name__))

    def complex_method_two(self):
        print("Running {}.complex_method_two".format(self.__class__.__name__))


class SubsystemA(Subsystem):
    pass

class SubsystemB(Subsystem):
    pass

class SubsystemC(Subsystem):
    pass


# Facade providing the API to all the complex logic above

class Facade:

    def __init__(self):
        self.subsystemA = SubsystemA()
        self.subsystemB = SubsystemB()
        self.subsystemC = SubsystemC()

    def run(self):
        """Here we do some complex stuff with all the classes above
        We can have several of such methods of course.
        """
        self.subsystemA.complex_method_one()
        self.subsystemB.complex_method_two()
        self.subsystemC.complex_method_one()
        self.subsystemA.complex_method_two()
        self.subsystemB.complex_method_one()
        self.subsystemC.complex_method_two()
        print("Done some complex stuff and probably returning the results.")


f = Facade()
f.run()