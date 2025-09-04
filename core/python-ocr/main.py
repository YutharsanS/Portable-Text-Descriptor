import cv2
import numpy as np

from utils import *
from config import TEST_IMAGES_DIR
import pprint

def main():
    path = TEST_IMAGES_DIR / "lenna.png"
    print(str(path))
    image = load_image(path)

    if image is not None:
        # image = resize_image(image, max_width=512, max_height=512)
        # pprint.pprint(get_image_info(image))
        cv2.imshow("image", convert_to_grayscale(image))
        cv2.waitKey()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()