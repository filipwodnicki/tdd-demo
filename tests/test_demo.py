"""test_demo.py
TDD Testing functions corresponding to demo.py
"""

from unittest import TestCase
import numpy as np
from demo import process_image


class TestProcessImage(TestCase):
    def test_grayscale(self):
        """Ensure input's third dimension becomes 1"""

        # Given
        input = [
            np.random.randint(256, size=(1, 1, 3)),
            np.random.randint(256, size=(10, 10, 3)),
            np.random.randint(256, size=(100, 100, 3)),
        ]

        # Do
        for image in input:
            actual_output = process_image(image)

            # Compare
            self.assertEqual(actual_output.ndim, 3)  # still want 3D input
            self.assertEqual(
                actual_output.shape[2], 1
            )  # but the 3rd dimension should be 1

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
