from typing import Union, List

from drums21.instruments import ALL_INSTRUMENTS
from music21.stream import Score, Part, Measure
from music21.clef import PercussionClef
from music21.key import KeySignature
from music21.tempo import MetronomeMark
from music21.meter import TimeSignature
from music21.metadata import Metadata
from music21.percussion import PercussionChord
from music21.note import Unpitched


class DrumScore(Score):
    def __init__(self, tempo: int = 80, time_signature: str = '4/4'):
        super().__init__()
        self.insert(Metadata())
        self.clef = PercussionClef()
        self.clef.line = 2
        self.key_signature = KeySignature(sharps=0)
        self.time_signature = TimeSignature(time_signature)
        self.tempo = MetronomeMark(number=tempo)
        self.drum_part = Part([self.clef, self.key_signature, self.time_signature, self.tempo])
        self.drum_part.partName = "Drumset"
        self.drum_part.partAbbreviation = "D. Set"

        for drum_instrument in ALL_INSTRUMENTS:
            self.drum_part.insert(drum_instrument())

        self.append(self.drum_part)

    def show(self, fmt=None, app=None, **keywords):
        self.drum_part.show()

    def add_note(self, notes: Union[Unpitched, List[Unpitched]]):
        should_append = False
        current_measure: Measure = self.drum_part.getElementsByClass('Measure').last()

        try:
            note_length = sum([note.quarterLength for note in current_measure.notes])
            if note_length >= self.time_signature.numerator:
                raise AttributeError
        except AttributeError:
            current_measure = Measure()
            should_append = True

        if type(notes) == list:
            chord = PercussionChord(notes)
        elif notes.isRest:
            chord = notes
        else:
            chord = PercussionChord([notes])

        current_measure.append(chord)

        if should_append:
            self.drum_part.append(current_measure)
