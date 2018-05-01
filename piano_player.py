import numpy as np
import matplotlib.pyplot as plt


def reorder_chord(chord):
    """ Reorder so that all white notes are first."""

    return sorted(chord, key=lambda x: len(x))


def play_chords(input_chord, key_map, piano_image):
    """ Produce a sequence of images corresponding to a series of notes.

    input_chord is a list of lists. Each sub-list contains the notes to be played for a single timestep (i.e.) a single
    image"""

    if not isinstance(input_chord[0], list):
        # We don't have a list of lists
        input_chord = [input_chord]

    output_images = []
    for chord in input_chord:
        chord = reorder_chord(chord)
        p_copy = np.copy(piano_image)
        for note in chord:

            x1 = key_map[note]['x'][0]
            x2 = key_map[note]['x'][1]
            y1 = key_map[note]['y'][0]
            y2 = key_map[note]['y'][1]
            if '#' not in note:
                p_copy[y1:y2, x1:x2] = p_copy[y1:y2, x1:x2] / 2
            else:
                p_copy[y1:y2, x1:x2] = p_copy[y1:y2, x1:x2] + 100

        output_images.append(p_copy)

    return output_images