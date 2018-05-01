import pickle
import matplotlib.pyplot as plt
from piano_player import play_chords


def test_load_of_keymap():
    key_map = pickle.load(open('key_map.pkl', 'rb'))
    assert isinstance(key_map, dict)

def test_load_of_piano_image():
    img = plt.imread('/Users/archydeberker/Downloads/piano.jpeg')

    assert len(img.shape) == 3

def test_run_chords_returns_an_image_list():
    input = ['A0', 'B0', 'C0']
    piano_image = plt.imread('/Users/archydeberker/Downloads/piano.jpeg')
    output = play_chords(input,
                         pickle.load(open('key_map.pkl', 'rb')),
                         piano_image)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape

def test_single_chord_handling():
    input = ['A0', 'B0', 'C0']
    piano_image = plt.imread('/Users/archydeberker/Downloads/piano.jpeg')
    output = play_chords(input,
                         pickle.load(open('key_map.pkl', 'rb')),
                         piano_image)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape

def test_multiple_chord_handling():

    input = [['A0', 'B0', 'C0'], ['A0', 'B0', 'C0']]
    piano_image = plt.imread('/Users/archydeberker/Downloads/piano.jpeg')
    output = play_chords(input,
                         pickle.load(open('key_map.pkl', 'rb')),
                         piano_image)

    assert len(output) is 2
