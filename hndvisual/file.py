from .decoder import Decoder
from pathlib import Path


class FileClient:
    def __init__(self, directory: Path):
        self.directory_iterator = iter(sorted(directory.iterdir()))
        self.decoder = Decoder()

    def __iter__(self):
        return self

    def __next__(self):
        for file in self.directory_iterator:
            with open(file, "rb") as f:
                frame = self.decoder.handle_packet(f.read())
            if frame is not None:
                return frame

        raise StopIteration
