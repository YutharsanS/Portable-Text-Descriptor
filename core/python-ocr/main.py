import cv2
import numpy as np

from utils import *
from config import TEST_IMAGES_DIR
import pprint

def main():
    path = TEST_IMAGES_DIR / "lenna.png"
    image = cv2.imread(str(path))

    if image is not None:
        image = resize_image(image, max_width=512, max_height=512)
        pprint.pprint(get_image_info(image))
        cv2.imshow("image", image)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()