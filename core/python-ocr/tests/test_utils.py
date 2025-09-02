"""Test script for utils"""

import sys
import pytest
import numpy as np
import tempfile
import cv2

from pathlib import Path
from confest import classic_rgb_test_image_512

from utils import image_utils
import os

sys.path.append(str(Path(__file__).parent))


class TestUtils:
    """Test suite for core image processing utilities"""

    def test_save_and_load_image(self):
        # Create a dummy RGB image
        img = np.zeros((10, 10, 3), dtype=np.uint8)
        img[..., 0] = 255  # Red channel
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            path = tmp.name
        try:
            assert image_utils.save_image(img, path)
            loaded = image_utils.load_images(path)
            assert loaded is not None
            assert loaded.shape == img.shape
            # Check pixel values
            assert np.array_equal(loaded, img)
        finally:
            os.remove(path)

    def test_resize_image(self):
        img = np.zeros((100, 200, 3), dtype=np.uint8)
        resized = image_utils.resize_image(img, max_width=50, max_height=50)
        assert resized.shape[0] <= 50 and resized.shape[1] <= 50
        # Aspect ratio maintained
        assert abs((resized.shape[1]/resized.shape[0]) - (200/100)) < 0.01

    def test_get_image_info(self):
        img = np.arange(100, dtype=np.uint8).reshape((10, 10))
        info = image_utils.get_image_info(img)
        assert info['shape'] == (10, 10)
        assert info['dtype'] == img.dtype
        assert info['min_value'] == img.min()
        assert info['max_value'] == img.max()
        assert info['mean_value'] == img.mean()

    def test_convert_to_grayscale(self, classic_rgb_test_image_512:np.ndarray):
        """Test RGB to grayscale conversion"""
        output = image_utils.convert_to_grayscale(classic_rgb_test_image_512)
        # Test image stats
        assert output.ndim == 2, "Must be a 2D array"
        assert output.shape[:2] == classic_rgb_test_image_512.shape[:2], "Image dimenstions must match"
        assert output.dtype == np.uint8, "Should maintain unit8 data type"

        red_region = output[400:410, 430:440]
        green_region = output[240:270, 240:270]

        # Test specific region
        assert red_region.max() < 100
        assert green_region.min() > 100