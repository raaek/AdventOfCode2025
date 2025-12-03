from asyncio.log import logger
import logging
import numpy as np
import math

logging.basicConfig(level=logging.INFO)

# translate the original rotaions (e.g. L30) into numbers with plus and minus (e.g. -30)
def translate(original_rotations: list[str]) -> list[int]:
    logger.debug(original_rotations)
    rotations = [
        -int(elem.replace("L", "")) if "L" in elem else int(elem.replace("R", ""))
        for elem in original_rotations
    ]
    return rotations


# calculate the new dial setting from the old one and the rotation
def calculate_new_dial_setting(current_dial_setting: int, rotation: int) -> int:
    new_dial_setting = (current_dial_setting + rotation) % 100
    logger.debug(new_dial_setting)
    return new_dial_setting


def main() -> None:
    number_of_times_0_has_been_reached: int = 0  # will be the password
    initial_dial_setting: int = 50
    current_dial_setting = initial_dial_setting

    # name of the input file with the rotation instructions
    input_file: str = "day1_input.txt"
    original_rotations: list[str] = []
    # read in the settings from the file
    with open(input_file) as file:
        for line in file.readlines():
            original_rotations.append(line.rstrip())

    rotations = translate(original_rotations)

    logger.info("the dial starts by pointing at %i", current_dial_setting)
    for rotation in rotations:
        sum = current_dial_setting + rotation
        logger.info("the dial is rotated %i to point at %i", rotation, sum % 100)
        if sum >= 100:
            number_of_times_0_has_been_reached = (
                number_of_times_0_has_been_reached + math.floor(sum / 100)
            )
            logger.info(
                "during this rotation, it points at 0 %i times", math.floor(sum / 100)
            )
        if sum <= 0:
            number_of_times_0_has_been_reached = (
                number_of_times_0_has_been_reached + 1 + math.floor(np.abs(sum) / 100)
            )
            logger.info(
                "during this rotation, it points at 0 %i times",
                1 + math.floor(np.abs(sum) / 100)
            )
            if current_dial_setting == 0:
                number_of_times_0_has_been_reached = (
                    number_of_times_0_has_been_reached - 1
                )

        current_dial_setting = calculate_new_dial_setting(
            current_dial_setting, rotation
        )

    logger.info("password:\n%s", number_of_times_0_has_been_reached)


if __name__ == "__main__":
    main()