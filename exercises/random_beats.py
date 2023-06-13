import random

from drums21.score import DrumScore
from drums21.utils import notes_from_part_bit_list
from drums21.notes import *

from music21 import *
from music21 import environment

environment.set('musicxmlPath', '~/Downloads/MuseScore-4.AppImage')

part = stream.Part()

base_pattern = {
    Kick:  [*[1, 0, 0, 0], *[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 0, 0]],
    Snare: [*[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 0, 0], *[0, 0, 0, 0]],
    HiHat: [*[1, 0, 1, 0], *[1, 0, 1, 0], *[1, 0, 1, 0], *[0, 0, 0, 0]]
}

note_choices = [
    Kick,
    Snare,
    HiHat,
    OpenHiHat,
    Crash,
    Ride,
    RideBell,
    HighTom,
    MiddleTom,
    LowTom,
]

score = DrumScore(tempo=60)

for _ in range(50):
    tmp = base_pattern.copy()

    for instrument, beat in tmp.items():
        tmp[instrument][-4::] = [0, 0, 0, 0]

    rand_beats = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    random.shuffle(rand_beats)

    for i in range(4):
        rand_note = random.choice(note_choices)
        rand_beat = [*[0, 0, 0, 0], *[0, 0, 0, 0], *[0, 0, 0, 0], *rand_beats[i]]
        if rand_note in tmp:
            for ib, beat in enumerate(tmp[rand_note]):
                if rand_beat[ib]:
                    tmp[rand_note][ib] = rand_beat[ib]
        else:
            tmp[rand_note] = rand_beat

    for instrument, beat in tmp.items():
        print(f'{instrument}: {beat}')
    print('-------------------------------------------')

    notes = notes_from_part_bit_list(tmp)
    score.add_notes(notes)

# score.drum_part.write('musicxml', 'out.xml')
score.show()
