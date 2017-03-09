from random import choice
from abc import abstractmethod


class SampleBank(object):

    def __init__(self, genre, type_):
        self.genre = genre
        self.type = type_


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


class TrackProject(object):
    """Abstract factory class"""

    @abstractmethod
    def get_beats_bank(self): raise NotImplementedError()

    @abstractmethod
    def get_bass_bank(self): raise NotImplementedError()


class TechnoTrackProject(TrackProject):

    genre = 'techno'

    def get_beats_bank(self): return TechnoBeatsBank()

    def get_bass_bank(self): return TechnoBassBank()


class HipHopTrackProject(TrackProject):

    genre = 'hip-hop'

    def get_beats_bank(self): return HipHopBeatsBank()

    def get_bass_bank(self): return HipHopBassBank()


if __name__ == "__main__":
    for x in range(5):
        project = choice([TechnoTrackProject, HipHopTrackProject])()
        print 'User #{} wants to make some {}'.format(x+1, project.genre)
        print "He gets a fresh new {}".format(project.__class__.__name__)
        print "That contains {} for his beats and {} for bass".format(
            project.get_beats_bank().__class__.__name__,
            project.get_bass_bank().__class__.__name__
        )
        print '-'*80 if x < 4 else '- FIN -'
