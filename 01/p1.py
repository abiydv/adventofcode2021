# usage: p1.py [-h] [-f [FILE]] [--debug]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -f [FILE], --file [FILE]
#                         specify the input file
#   --debug               show debug output

from helper import parse_arguments, init_logger


def compare_elements(arr, logger):
    logger.debug(f"Input in compare_elements - {arr}")

    count, previous = 0, 0
    for i, number in enumerate(arr):
        logger.debug(f"i - {i}")
        if i == 0:
            logger.debug(f"Ignore first element")
            previous = int(number)
            continue

        count = count + 1 if int(number) > previous else count

        logger.debug(f"This - {number}, Previous - {previous}, Count - {count}")
        previous = int(number)

    logger.debug(f"Return from compare_elements - {count}")
    return count


def main():
    input = parse_arguments()
    logger = init_logger(input.debug)

    logger.debug(f"File to work with - {input.file}")
    with open(input.file, "r") as f:
        readings = [int(r.strip()) for r in f]

    count = compare_elements(readings, logger)

    logger.info(f"Readings larger than previous readings - {count}")


if __name__ == "__main__":
    main()
