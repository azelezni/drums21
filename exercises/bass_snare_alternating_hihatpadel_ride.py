import random

from drums21.score import DrumScore
from drums21.utils import notes_from_part_bit_list
from drums21.notes import *

page_1_snare = {
    Snare: [*[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 0, 0], *[1, 0, 0, 0]]
}

page_1_beats = {
    1: {
        Kick:  [*[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0]],
        **page_1_snare
    },
    2: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    3: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 0, 0], *[1, 0, 1, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    4: {
        Kick:  [*[1, 0, 1, 0], *[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    5: {
        Kick:  [*[1, 0, 1, 0], *[0, 0, 0, 0], *[1, 0, 1, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    6: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 1, 0], *[1, 0, 0, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    7: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 0, 0], *[1, 0, 0, 0], *[0, 0, 1, 0]],
        **page_1_snare
    },
    8: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 1, 0], *[1, 0, 0, 0], *[0, 0, 1, 0]],
        **page_1_snare
    },
    9: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 1, 0], *[1, 0, 1, 0], *[0, 0, 0, 0]],
        **page_1_snare
    },
    10: {
        Kick:  [*[1, 0, 0, 0], *[0, 0, 1, 0], *[1, 0, 1, 0], *[0, 0, 1, 0]],
        **page_1_snare
    },
}

beat_patterns = {
    'hhp_on_beat': {
        PedalHiHat: [*[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0]],
    },
    'hhp_off_beat': {
        PedalHiHat: [*[0, 0, 1, 0], *[0, 0, 1, 0], *[0, 0, 1, 0], *[0, 0, 1, 0]],
    },
    'ride_on_beat': {
        Ride: [*[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0], *[1, 0, 0, 0]],
    },
    'ride_off_beat': {
        Ride: [*[0, 0, 1, 0], *[0, 0, 1, 0], *[0, 0, 1, 0], *[0, 0, 1, 0]],
    },
    'ride_sixteenths': {
        Ride: [*[1, 0, 1, 1], *[1, 0, 1, 1], *[1, 0, 1, 1], *[1, 0, 1, 1]],
    },
}

score = DrumScore()

# for _ in range(24):
#     page_beat, beat = random.choice(list(page_1_beats.items()))
#     for _ in range(4):
#         pattern_name, pattern = random.choice(list(beat_patterns.items()))
#         tmp = dict(beat)
#         tmp.update(pattern)
#         notes = notes_from_part_bit_list(tmp)
#         score.add_notes(notes)

for beat in page_1_beats.values():
    notes = notes_from_part_bit_list(beat)
    score.add_notes(notes)
    for pattern in beat_patterns.values():
        tmp = dict(beat)
        tmp.update(pattern)
        notes = notes_from_part_bit_list(tmp)
        score.add_notes(notes)

score.show()
