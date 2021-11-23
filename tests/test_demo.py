"""test_demo.py
TDD Testing functions corresponding to demo.py
"""

from unittest import TestCase
import numpy as np
from demo import process_image, _convert_to_grayscale


class TestProcessImage(TestCase):
    def test_grayscale_dimensions(self):
        """Ensure 3D output becomes 2D without changing other dimensions"""

        # Given
        input = [
            np.random.randint(256, size=(3, 1, 1), dtype="B"),
            np.random.randint(256, size=(3, 10, 10), dtype="B"),
            np.random.randint(256, size=(3, 100, 100), dtype="B"),
        ]

        # Do
        for image in input:
            actual_output = _convert_to_grayscale(image)

            # Compare
            self.assertEqual(actual_output.ndim, 2)  # Output should be 2D
            self.assertEqual(
                image.shape[1:], actual_output.shape
            )  # dimension and 1 and 2 should be unchanged

    def test_grayscale_functionality(self):
        self.fail

    def test_normalize(self):
        """Ensure values go from int [0, 255] to float [0, 1]"""

        # Given
        input = [
            np.random.randint(256, size=(4, 4, 3)),
            np.random.randint(256, size=(10, 10, 3)),
            np.random.randint(256, size=(100, 100, 3)),
            np.random.randint(256, size=(1000, 1000, 3)),
        ]

        # Do
        for image in input:
            actual_output = process_image(image)

            # Compare
            self.assertIsInstance(actual_output.flat, np.floating)
