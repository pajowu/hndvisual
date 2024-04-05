from collections import defaultdict
from typing import Optional
from PIL import Image, ImageFile
import io
import logging

logger = logging.getLogger()

ImageFile.LOAD_TRUNCATED_IMAGES = True

FRAME_LEN = 1304
HEADER_LEN = 4


class Decoder:
    def __init__(self):
        self._frames = defaultdict(bytes)

    def handle_packet(self, packet: bytes) -> Optional[Image.Image]:
        if len(packet) < 32:
            logger.debug(f"Packet to short, skipping ({len(packet)=})")
            return

        frame_num = packet[0]
        is_end_of_frame = packet[1]
        self._frames[frame_num] += packet[HEADER_LEN:]

        img = None
        if is_end_of_frame:
            done_frame = self._frames[frame_num]
            del self._frames[frame_num]
            try:
                img = Image.open(io.BytesIO(done_frame))
            except Exception as e:
                print(e)

            # nparr = np.fromstring(done_frame, np.uint8)
            # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            # print(img)

        return img
