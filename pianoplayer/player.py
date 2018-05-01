import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

import argparse
import pickle


from pianoplayer.constants import KEYMAP, PIANO


def get_keymap():
    return pickle.load(open(KEYMAP, 'rb'))


def get_piano_image():
    p = plt.imread(PIANO)
    return p[:,:,0]


def reorder_chord(chord):
    """ Reorder so that all white notes are first."""

    return sorted(chord, key=lambda x: len(x))


class PianoPlayer:

    def __init__(self, keymap=get_keymap(), piano_image=get_piano_image()):

        self.key_map = keymap
        self.piano_image = piano_image

    def play_chords(self, input_sequence):
        """ Produce a sequence of images corresponding to a series of notes.

        input_chord is a list of lists. Each sub-list contains the notes to be played for a single timestep (i.e.) a single
        image"""

        if not isinstance(input_sequence[0], list):
            # We don't have a list of lists
            input_sequence = [input_sequence]

        output_images = []
        for chord in input_sequence:
            chord = reorder_chord(chord)
            p_copy = np.copy(self.piano_image)
            for note in chord:

                x1 = self.key_map[note]['x'][0]
                x2 = self.key_map[note]['x'][1]
                y1 = self.key_map[note]['y'][0]
                y2 = self.key_map[note]['y'][1]
                if '#' not in note:
                    p_copy[y1:y2, x1:x2] = p_copy[y1:y2, x1:x2] / 2
                else:
                    p_copy[y1:y2, x1:x2] = p_copy[y1:y2, x1:x2] + 100

            output_images.append(p_copy)

        return output_images

    def generate_gif(self, input_chord, output_file, framerate):
        """

        Parameters
        ----------
        input_chord: iterable
        output_file: str
        framerate: int

        Returns
        -------

        """
        img_matrices = self.play_chords(input_chord)

        fig = plt.figure(figsize=(20, 10))

        artists = [[plt.imshow(i, animated=True, cmap='gray')] for i in img_matrices]

        ani = ArtistAnimation(fig, artists, interval=framerate, blit=True)
        ani.save(output_file, writer='imagemagick')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Produce an animated GIF of a series of piano notes')
    parser.add_argument('input_file', help='file from which sequence to be read. each line constitutes a new frame',
                        type=str)
    parser.add_argument('-o', '--output_file', help='the name of the file you would like to write to', default='piano.gif')
    parser.add_argument('-f', '--framerate', help='frame rate in milliseconds', default=1000, type=int)

    args = parser.parse_args()

    with open(args.input_file) as f:
        raw_input_sequence = f.readlines()

    # Convert this to a list of list
    input_sequence = []
    for l in raw_input_sequence:
        input_sequence.append(l.split())

    piano_player = PianoPlayer()
    piano_player.generate_gif(input_sequence,
                              output_file=args.output_file,
                              framerate=args.framerate)


