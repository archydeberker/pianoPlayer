import tempfile
import os
import pytest

from pianoplayer.player import PianoPlayer, get_keymap, get_piano_image

@pytest.fixture
def piano_player():
    return PianoPlayer()

def test_load_of_keymap():
    key_map = get_keymap()
    assert isinstance(key_map, dict)


def test_load_of_piano_image():
    img = get_piano_image()
    assert len(img.shape) == 2


def test_play_chords_returns_an_image_list(piano_player):
    input = ['A0', 'B0', 'C0']
    piano_image = get_piano_image()
    output = piano_player.play_chords(input)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape


def test_single_chord_handling(piano_player):
    input = ['A0', 'B0', 'C0']
    piano_image = get_piano_image()
    output = piano_player.play_chords(input)

    assert isinstance(output, list)
    assert output[0].shape == piano_image.shape


def test_multiple_chord_handling(piano_player):

    input = [['A0', 'B0', 'C0'], ['A0', 'B0', 'C0']]
    output = piano_player.play_chords(input)

    assert len(output) is 2


def test_gif_animation(piano_player):
    input = ['A0', 'B0', 'C0']

    with tempfile.NamedTemporaryFile() as f:
        piano_player.generate_gif(input,
                                  output_file=f.name,
                                  framerate=1000)

        assert os.path.getsize(f.name) > 0
