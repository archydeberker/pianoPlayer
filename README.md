# pianoPlayer
Python code for visualizing music as a series of piano key presses

## Requirements

You'll need to install `imageMagick` in order to export gifs from matplotlib.

On a Mac, this is as simple as 

`brew install imagemagick`.

If you don't have `homebrew` installed, consider doing so!

The code is provided as a python package; you can install it remotely, or clone the repo and run

`pip install . ` inside the folder.

## Tests

To run the tests, simply run

`pytest` in the root folder.

## Examples

See [`pianoplayer/assets`](pianoplayer/assets) for an example of an input sequence file and the resulting GIF.
