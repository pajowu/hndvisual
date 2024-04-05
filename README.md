# HND Visual Python Client

A simple python client for visual earpicks of the hnd brand.

## Installation

Install the dependencies using [poetry](https://python-poetry.org/):

```shell
poetry install
```

If you want to use the example scripts, you can install their additional dependencies with

```shell
poetry install -E examples
```

## Usage

See [`examples`](examples/):

- `live_udp.py`: Show the live images from an earpick via udp
- `dump_udp_to_file.py`: Connect to an earpick via udp and store the messages to files
- `live_file.py`: Read the files produced by `dump_udp_to_file.py` and show them live
