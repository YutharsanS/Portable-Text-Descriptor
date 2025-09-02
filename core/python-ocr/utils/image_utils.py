"""Utility functions for image processing"""

import cv2
import numpy as np
import logging

from pathlib import Path
from typing import Union, Optional

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) # module's name, specific to module

# Utils functions
def load_images(image_path: Union[str, Path]) -> Optional[np.ndarray]: # either None, or numpy array
    """
    Load image from file path as an RGB image
    """

    try:
        image_path = str(image_path)
        image = cv2.imread(image_path)

        if image is not None:
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        logger.warning(f"Imaged loaded as None: {image_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to load image {image_path}: {e}")
        return None

def save_image(image: np.ndarray, output_path: Union[str, Path]) -> bool:
    """
    Write image to a file path specified as BGR image
    """

    output_path = str(output_path)

    if len(image.shape) == 3 :
        image_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        image_bgr = image

    return cv2.imwrite(output_path, image_bgr)

def resize_image(image: np.ndarray, max_width: int = 1920, max_height: int = 1080) -> np.ndarray:
    """
    Resize the image while maintaining the aspect ratio
    """

    h, w = image.shape[:2]

    # Scaling factors
    scale_w = max_width / w
    scale_h = max_height / h

    scale = min(scale_w, scale_h, 1.0) # can't upscale, because we are using INTER_AREA which

    new_w = w * scale
    new_h = h * scale

    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert images to grayscale"""
    if image.ndim == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # eliminate double conversion exception
    return image

def get_image_info(image: np.ndarray) -> dict:
    """Get basic information about image"""

    return {
        'shape': image.shape,
        'dtype': image.dtype,
        'min_value': image.min(),
        'max_value': image.max(),
        'mean_value': image.mean()
    }
