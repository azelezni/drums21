from drums21.instruments import *

from music21 import duration
from music21.note import Unpitched


class DrumsNote(Unpitched):
    def __init__(self, *arguments, **keywords):
        if 'duration' not in keywords:
            keywords.update({'duration': duration.Duration(0.5)})
        super().__init__(*arguments, **keywords)
        self.stemDirection = 'up'


class Kick(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(AcousticBassDrumInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = AcousticBassDrumInstrument()
        self.displayStep = 'F'
        self.displayOctave = 4


class Snare(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(AcousticSnareInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = AcousticSnareInstrument()
        self.displayStep = 'C'
        self.displayOctave = 5


class HiHat(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(ClosedHiHatInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = ClosedHiHatInstrument()
        self.displayStep = 'G'
        self.displayOctave = 5
        self.notehead = 'x'


class OpenHiHat(DrumsNote):
    def __init__(self, *arguments, **keywords):
        # super().__init__(OpenHiHatInstrument().percMapPitch, *arguments, **keywords)
        super().__init__(displayName='G5', *arguments, **keywords)
        self.storedInstrument = OpenHiHatInstrument()
        self.displayPitch()
        self.displayStep = 'G'
        self.displayOctave = 5
        self.notehead = 'circle-x'


class PedalHiHat(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(PedalHiHatInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = PedalHiHatInstrument()
        self.displayStep = 'D'
        self.displayOctave = 4
        self.notehead = 'x'


class Crash(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(CrashCymbal1Instrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = CrashCymbal1Instrument()
        self.displayStep = 'A'
        self.displayOctave = 5
        self.notehead = 'x'


class Ride(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(RideCymbal1Instrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = RideCymbal1Instrument()
        self.displayStep = 'F'
        self.displayOctave = 5
        self.notehead = 'x'


class RideBell(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(RideBellInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = RideBellInstrument()
        self.displayStep = 'F'
        self.displayOctave = 5
        self.notehead = 'diamond'


class HighTom(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(HighTomInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = HighTomInstrument()
        self.displayStep = 'F'
        self.displayOctave = 5


class MiddleTom(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(LowMidTomInstrument().percMapPitch, *arguments, **keywords)  # 48
        self.storedInstrument = LowMidTomInstrument()
        self.displayStep = 'E'
        self.displayOctave = 5


class LowTom(DrumsNote):
    def __init__(self, *arguments, **keywords):
        super().__init__(LowFloorTomInstrument().percMapPitch, *arguments, **keywords)
        self.storedInstrument = LowFloorTomInstrument()
        self.displayStep = 'A'
        self.displayOctave = 4


ALL_NOTES = [
    DrumsNote,
    Kick,
    Snare,
    HiHat,
    OpenHiHat,
    PedalHiHat,
    Crash,
    Ride,
    RideBell,
    HighTom,
    MiddleTom,
    LowTom,
]
