from typing import Dict, List, Any, Union

from drums21.notes import *

from music21.duration import Duration


def notes_from_part_bit_list(part_bits: Dict[Any, List[int]]) -> List[List[Any]]:
    output = []
    instruments = list(part_bits.keys())
    length = len(part_bits[instruments[0]])

    for instrument in instruments:
        assert len(part_bits[instrument]) == length

    for i in range(length):
        chord = []
        chord_duration = 0.25
        if i < length:
            for j in range(i + 1, length):
                if all([part_bits[instrument][j] == 0 for instrument in instruments]):
                    chord_duration += 0.25
                else:
                    break
        for instrument in instruments:
            if part_bits[instrument][i]:
                chord.append(instrument(duration=Duration(chord_duration)))
        if chord:
            output.append(chord)

    return output
