import numpy as np
import matplotlib.pyplot as plt
import argparse
import pickle
from pianoplayer.constants import KEYMAP, PIANO

def get_keymap():
    return pickle.load(open(KEYMAP, 'rb'))

def get_piano_image():
    return plt.imread(PIANO)

def reorder_chord(chord):
    """ Reorder so that all white notes are first."""

    return sorted(chord, key=lambda x: len(x))

def play_chords(input_sequence, key_map, piano_image):
    """ Produce a sequence of images corresponding to a series of notes.

    input_chord is a list of lists. Each sub-list contains the notes to be played for a single timestep (i.e.) a single
    image"""

    if not isinstance(input_sequence[0], list):
        # We don't have a list of lists
        input_sequence = [input_sequence]

    output_images = []
    for chord in input_sequence:
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

def generate_gif(input_chord, output_file, framerate, key_map='assets/key_map.pkl', piano_image='assets/piano.jpg'):

    img_matrices = play_chords(input_chord, )



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Produce an animated GIF of a series of piano notes')
    parser.add_argument('input_sequence', help='the sequence of notes you would like to play, as a list of lists')
    parser.add_argument('output_file', help='the name of the file you would like to write to', default='piano.gif')
    parser.add_argument('framerate', help='frame rate in milliseconds', default=1000)

    args = parser.parse_args()

    gif = generate_gif(args.input_sequence,
                       args.output_file,
                       args.framerate)



