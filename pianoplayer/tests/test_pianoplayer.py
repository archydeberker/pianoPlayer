import pickle
import matplotlib.pyplot as plt
from pianoplayer.player import play_chords
from pianoplayer.constants import KEYMAP, PIANO


def test_load_of_keymap():
    key_map = pickle.load(open(KEYMAP, 'rb'))
    assert isinstance(key_map, dict)


def test_load_of_piano_image():
    img = plt.imread(PIANO)

    assert len(img.shape) == 3


def test_run_chords_returns_an_image_list():
    input = ['A0', 'B0', 'C0']
    piano_image = plt.imread(PIANO)
    output = play_chords(input,
                         pickle.load(open(KEYMAP, 'rb')),
                         piano_image)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape


def test_single_chord_handling():
    input = ['A0', 'B0', 'C0']
    piano_image = plt.imread(PIANO)
    output = play_chords(input,
                         pickle.load(open(KEYMAP, 'rb')),
                         piano_image)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape


def test_multiple_chord_handling():

    input = [['A0', 'B0', 'C0'], ['A0', 'B0', 'C0']]
    piano_image = plt.imread(PIANO)
    output = play_chords(input,
                         pickle.load(open(KEYMAP, 'rb')),
                         piano_image)

    assert len(output) is 2
