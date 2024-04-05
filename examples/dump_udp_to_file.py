import socket
import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.1")
    parser.add_argument("--port", type=int, default=44506)
    parser.add_argument("out_dir", type=Path)
    args = parser.parse_args()

    args.out_dir.mkdir(exist_ok=True)

    MESSAGE = b"\x20\x36"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (args.ip, args.port))

    i = 0
    while True:
        data = sock.recv(1024 * 1024)
        with open(args.out_dir / f"{i:04d}.raw", "wb") as f:
            f.write(data)
        i += 1
        print(i)
