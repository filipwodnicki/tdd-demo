"""demo.py
Small demo file that shows corresponding tests.
"""
import numpy as np


def _convert_to_grayscale(image: np.array) -> np.array:
    """Converts 8-bit image array from RGB to grayscale by averaging RGB inputs"""
    assert image.dtype == np.dtype("uint8"), "array not 8-bit unsigned"
    assert len(image.shape) == 3, "image array needs to have three dimensions"
    assert image.shape[0] == 3, "image needs to be composed of three layers, RGB"

    return np.mean(image, axis=0)


def _normalize(image: np.array) -> np.array:
    """Normalizes integer array [0,255] to [0,1]"""

    pass


def process_image(image_array: np.array) -> np.array:
    """Converts image to grayscale and returns normalized 0 to 1

    # Input
    image_array (np.array) -> image that is 10 x 10 x 3 in 8-bit (0-255)

    # Output
    image_array (np.array) -> image that is 10 x 10 x 1 grayscale, normalized (0-1)
    """
    pass


if __name__ == "__main__":
    pass
