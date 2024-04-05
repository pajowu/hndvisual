from hndvisual.file import FileClient
from pathlib import Path
import cv2
import numpy as np

if __name__ == "__main__":
    client = FileClient(Path("out/"))

    cv2.namedWindow("preview")

    for image in client:
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow("preview", cv_image)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
