import socket
from .decoder import Decoder

DEFAULT_IP = "192.168.1.1"
DEFAULT_PORT = 44506
OPEN_MESSAGE = b"\x20\x36"


class UdpClient:
    def __init__(self, ip: str = DEFAULT_IP, port: int = DEFAULT_PORT):
        self.ip = ip
        self.port = port
        self.decoder = Decoder()

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sendto(OPEN_MESSAGE, (self.ip, self.port))

    def __iter__(self):
        return self

    def __next__(self):
        frame = None
        while frame is None:
            data = self.sock.recv(1024 * 1024)
            if not data:  # Socket was closed
                raise StopIteration

            frame = self.decoder.handle_packet(data)
        return frame
