import cv2
import numpy as np
import logging

from typing import Optional, Tuple
# from ..utils.image_utils import convert_to_grayscale, resize_image

logger = logging.getLogger(__name__)

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Main preporcessing pipeline
    """

    logger.info("Starting image preprocessing")


    return np.array([])

def reduce_noise(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Apply noise reduction filters"""

    denoised = cv2.bilateralFilter(image, 3, 30, 50)

    return image, denoised