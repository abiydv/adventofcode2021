import argparse
import logging


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", help="specify the input file", default="test.txt", nargs="?"
    )
    parser.add_argument("--debug", action="store_true", help="show debug output")
    input = parser.parse_args()
    return input


def init_logger(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    logger = logging.getLogger()
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
