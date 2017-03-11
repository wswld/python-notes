"""The simplest abstract factory example as music DAW software pseudocode"""

from random import choice
from abc import abstractmethod


class SampleBank(object):

    def __init__(self, genre, type_):
        self.genre = genre
        self.type = type_

    def load(self):
        print "Loading {} {}.".format(self.genre, self.type)


class TechnoBeatsBank(SampleBank):

    def __init__(self):
        super(TechnoBeatsBank, self).__init__("techno", "beats")


class TechnoBassBank(SampleBank):
    def __init__(self):
        super(TechnoBassBank, self).__init__("techno", "bass")


class HipHopBeatsBank(SampleBank):
    def __init__(self):
        super(HipHopBeatsBank, self).__init__("hip-hop", "beats")


class HipHopBassBank(SampleBank):
    def __init__(self):
        super(HipHopBassBank, self).__init__("hip-hop", "bass")


class AbstractTrackProject(object):
    """Abstract factory class"""

    @abstractmethod
    def get_beats_bank(self): raise NotImplementedError()

    @abstractmethod
    def get_bass_bank(self): raise NotImplementedError()

    def create(self, name):
        if name == 'techno':
            return TechnoTrackProject()
        if name == 'hip-hop':
            return HipHopTrackProject()


class TechnoTrackProject(AbstractTrackProject):

    genre = 'techno'

    def get_beats_bank(self): return TechnoBeatsBank()

    def get_bass_bank(self): return TechnoBassBank()


class HipHopTrackProject(AbstractTrackProject):

    genre = 'hip-hop'

    def get_beats_bank(self): return HipHopBeatsBank()

    def get_bass_bank(self): return HipHopBassBank()


if __name__ == "__main__":
    for x in range(5):
        project = AbstractTrackProject().create(choice(['techno', 'hip-hop']))
        print 'User #{} wants to make some {}'.format(x+1, project.genre)
        project.get_beats_bank().load()
        project.get_bass_bank().load()
        print '-'*80 if x < 4 else '- FIN -'
