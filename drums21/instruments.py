from music21.instrument import UnpitchedPercussion


class DrumInstrument(UnpitchedPercussion):
    def __init__(self):
        super().__init__()
        self.instrumentAbbreviation = None
        self.midiChannel = 10
        self.midiProgram = 1


class AcousticBassDrumInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 36
        self.instrumentName = 'Acoustic Bass Drum'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class AcousticSnareInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 38
        self.instrumentName = 'Acoustic Snare'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class ClosedHiHatInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 42
        self.instrumentName = 'Closed Hi-Hat'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class OpenHiHatInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 47
        self.instrumentName = 'Open Hi-Hat'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class PedalHiHatInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 44
        self.instrumentName = 'Pedal Hi-Hat'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class HighTomInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 50
        self.instrumentName = 'High Tom'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class LowMidTomInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 43
        self.instrumentName = 'Low-Mid Tom'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class LowFloorTomInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 41
        self.instrumentName = 'Low Floor Tom'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class CrashCymbal1Instrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 49
        self.instrumentName = 'Crash Cymbal 1'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class RideCymbal1Instrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 51
        self.instrumentName = 'Ride Cymbal 1'
        self.instrumentId = f'P1-I{self.percMapPitch}'


class RideBellInstrument(DrumInstrument):
    def __init__(self):
        super().__init__()
        self.percMapPitch = 53
        self.instrumentName = 'Ride Bell'
        self.instrumentId = f'P1-I{self.percMapPitch}'


ALL_INSTRUMENTS = [
    AcousticBassDrumInstrument,
    AcousticSnareInstrument,
    ClosedHiHatInstrument,
    PedalHiHatInstrument,
    LowFloorTomInstrument,
    OpenHiHatInstrument,
    LowMidTomInstrument,
    CrashCymbal1Instrument,
    HighTomInstrument,
    RideCymbal1Instrument,
    RideBellInstrument,
]
