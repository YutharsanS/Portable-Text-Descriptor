import numpy as np
import pytest
import cv2
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__).parent.parent))

from utils import convert_to_grayscale

def classic_rgb_test_image(size: int =512) -> np.ndarray:
    """
    Creates a scalable RGB test image with a white background and:
    - A red square in the top-left
    - A green circle in the center
    - A blue triangle in the bottom-right

    Args:
        size (int): The width and height of the image (default: 512)

    Returns:
        numpy.ndarray: RGB test image of specified size
    """
    # Create a white background (255, 255, 255)
    image = np.ones((size, size, 3), dtype=np.uint8) * 255

    # Calculate proportional sizes based on image dimensions
    square_size = size // 16  # ~32px for 512x512
    circle_radius = size // 20  # ~25px for 512x512
    triangle_size = size // 10  # ~51px for 512x512

    # 1. Add a red square (top-left)
    start_x, start_y = size // 16, size // 16  # ~32px from edge
    end_x, end_y = start_x + square_size, start_y + square_size

    image[start_y:end_y, start_x:end_x, 0] = 255  # Red channel
    image[start_y:end_y, start_x:end_x, 1] = 0    # Green channel
    image[start_y:end_y, start_x:end_x, 2] = 0    # Blue channel

    # 2. Add a green circle (center)
    center_y, center_x = size // 2, size // 2  # Center of image
    y, x = np.ogrid[:size, :size]
    circle_mask = (x - center_x)**2 + (y - center_y)**2 <= circle_radius**2

    image[circle_mask, 0] = 0    # Red channel
    image[circle_mask, 1] = 255  # Green channel
    image[circle_mask, 2] = 0    # Blue channel

    # 3. Add a blue triangle (bottom-right)
    start_triangle_x = size - size // 8  # ~448px for 512x512
    start_triangle_y = size - size // 8  # ~448px for 512x512

    for i in range(triangle_size):
        for j in range(i):
            y = start_triangle_y - i
            x = start_triangle_x - j
            if 0 <= y < size and 0 <= x < size:
                image[y, x, 0] = 0    # Red channel
                image[y, x, 1] = 0    # Green channel
                image[y, x, 2] = 255  # Blue channel

    return image

@pytest.fixture
def classic_rgb_test_image_512() -> np.ndarray:
    """Test sample image 512 x 512 """
    return classic_rgb_test_image(size=512)


if __name__ == "__main__":
    cv2.imshow("image", classic_rgb_test_image())
    cv2.waitKey()