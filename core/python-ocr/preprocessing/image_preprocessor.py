import cv2
import numpy as np
import logging

from typing import Optional, Tuple
from config import BILATERAL_FILTER_D, BILATERAL_FILTER_SIGMA, MAX_IMAGE_HEIGHT, MAX_IMAGE_WIDTH
from utils.image_utils import *

logger = logging.getLogger(__name__)

def preprocess_image(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Main preporcessing pipeline
    """

    logger.info("Starting image preprocessing")

    resized = resize_image(image, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)

    grayscaled = convert_to_grayscale(resized)

    noised_reduced = reduce_noise(grayscaled)[-1]

    contrast_enhanced = enhance_contrast(noised_reduced)[-1]

    binary = binarize_image(contrast_enhanced)[-1]

    return image, binary

def reduce_noise(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Apply noise reduction filters"""

    denoised = cv2.bilateralFilter(image, BILATERAL_FILTER_D, BILATERAL_FILTER_SIGMA, BILATERAL_FILTER_SIGMA)

    return image, denoised

def enhance_contrast(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Enhance image contrast with CLAHE"""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(image)

    return image, enhanced

def binarize_image(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Convert to binary image using adaptive thresholding"""
    # Adaptive thresholding works better for varying lighting conditions
    binary = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    return image, binary
