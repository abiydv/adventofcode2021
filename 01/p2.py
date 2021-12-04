# usage: p2.py [-h] [-f [FILE]] [--debug]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -f [FILE], --file [FILE]
#                         specify the input file
#   --debug               show debug output

from helper import parse_arguments, init_logger
from p1 import compare_elements


def main():
    input = parse_arguments()
    logger = init_logger(input.debug)

    logger.debug(f"File to work with - {input.file}")
    with open(input.file, "r") as f:
        readings = [int(r.strip()) for r in f]

    reading_sum = [
        sum(readings[i : i + 3])
        for i in range(len(readings))
        if len(readings[i : i + 3]) == 3
    ]

    count = compare_elements(reading_sum, logger)
    logger.info(f"Sums larger than previous sum - {count}")


if __name__ == "__main__":
    main()
