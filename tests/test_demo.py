"""test_demo.py
Testing functions written for TDD of demo.py
"""

from unittest import TestCase
import numpy as np
from demo import _convert_to_grayscale, _normalize


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
        """Ensure image gets averaged and converted from uint-8 to single float"""

        # Given
        image = np.array(
            [[[209, 215], [188, 134]], [[225, 65], [3, 74]], [[193, 136], [241, 245]]],
            dtype="B",
        )

        # Do
        actual_output = _convert_to_grayscale(image)

        # Compare
        expected_output = np.array([[209.0, 138.66666667], [144.0, 151.0]], dtype="f")
        print(actual_output)
        self.assertIsNone(np.testing.assert_equal(actual_output, expected_output))
        self.assertTrue(actual_output.dtype, np.dtype("f"))  # Ensure output is float

    def test_normalize(self):
        """Ensure values are correctly normalized from int8 [0, 255] to single float [0.0, 1.0]"""

        # Given
        input_image = np.array([[209.0, 138.66666667], [144.0, 151.0]], dtype="f")

        # Do
        actual_output = _normalize(input_image)

        # Compare
        expected_output = np.array(
            [[0.81960785, 0.5437909], [0.5647059, 0.5921569]], dtype="f"
        )
        self.assertIsNone(np.testing.assert_equal(actual_output, expected_output))
