"""Configuration settings for OCR pipeline"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
CORE_DIR = PROJECT_ROOT / "core" / "python-ocr" # syntax is possible because of pathlib operator overloading
TEST_IMAGES_DIR = PROJECT_ROOT / "research" / "test-images"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Tessaract Settings

# Image Processing parameters
MAX_IMAGE_WIDTH = 512
MAX_IMAGE_HEIGHT = 512

BILATERAL_FILTER_D = 9
BILATERAL_FILTER_SIGMA = 50

# Performance settings

# Debugging


def create_directories():
    """Create necessary  directories if they don't exist"""
    directories = [TEST_IMAGES_DIR, OUTPUT_DIR]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    create_directories()
    print("Configuration loaded successfully")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Core directory: {CORE_DIR}")