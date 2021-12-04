# usage: p1.py [-h] [-f [FILE]] [--debug]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -f [FILE], --file [FILE]
#                         specify the input file
#   --debug               show debug output

from helper import parse_arguments, init_logger


def main():
    input = parse_arguments()
    logger = init_logger(input.debug)
    
    logger.debug(f"File to work with - {input.file}")
    with open(input.file, "r") as f:
        instructions = [str(r.strip()) for r in f]

    horizontal, depth = 0, 0
    for i in range(len(instructions)):
        logger.debug(f"{i} Instruction - {instructions[i]}")
        unit = int(instructions[i].split(" ")[1])
        
        if instructions[i].__contains__("forward"):
            horizontal = horizontal + unit
        elif instructions[i].__contains__("up"):
            depth = depth - unit
        elif instructions[i].__contains__("down"):
            depth = depth + unit
        else:
            logger.warn(f"Ignoring instruction, not one of [forward, up, down]")
        
        logger.debug(f"{i} Horizontal, Depth - {horizontal}, {depth}")

    product = horizontal*depth
    logger.info(f"Product of horizontal position and depth - {product}")


if __name__ == "__main__":
    main()
