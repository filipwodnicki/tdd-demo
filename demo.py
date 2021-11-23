"""demo.py
Small demo file of processing an image that shows corresponding tests.
"""
import numpy as np


def _convert_to_grayscale(image: np.array) -> np.array:
    """Converts 8-bit image array from RGB to grayscale by averaging RGB inputs"""

    assert image.dtype == np.dtype("uint8"), "array not 8-bit unsigned"
    assert len(image.shape) == 3, "image array needs to have three dimensions"
    assert image.shape[0] == 3, "image needs to be composed of three layers, RGB"

    return np.mean(image, axis=0).astype("f", copy=False)


def _normalize(image: np.array) -> np.array:
    """Normalizes single float integer array from [0,255] to [0,1]"""
    assert image.dtype == np.dtype("single")

    return image / 255


def process_image(image_array: np.array) -> np.array:
    """Converts image to grayscale and returns normalized 0 to 1

    # Input
    image_array (np.array) -> image that is 10 x 10 x 3 in 8-bit [0-255]

    # Output
    image_array (np.array) -> image that is 10 x 10 x 1 grayscale, normalized [0-1]
    """
    grayscale_image = _convert_to_grayscale(image_array)
    normalized_grayscale_image = _normalize(grayscale_image)
    return normalized_grayscale_image


def main():
    print("This is a TDD demo...")
    print("All the fun happened while iteratively writing tests and code.")
    print("But here's the finished code scenario:\n")
    print("We start with a 4x4 RGB image")
    image = np.random.randint(256, size=(3, 4, 4), dtype="B")
    print(image)
    print("\nIt get's processed: converted to grayscale and normalized.")
    print("Here it is:")
    processed_image = process_image(image)
    print(processed_image)


if __name__ == "__main__":
    main()
