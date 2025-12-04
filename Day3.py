from asyncio.log import logger
import logging

logging.basicConfig(level=logging.INFO)


class batteryBank:
    def __init__(self, bank: str):
        self.bank = bank

    def _get_highest_joltage(self) -> int:
        bank = self.bank
        highest_joltage = highest_digit_in(bank)
        return highest_joltage


def highest_digit_in(sequence: str) -> int:
    highest_digit = max([int(digit) for digit in sequence])
    logger.debug(highest_digit)
    return highest_digit


def main() -> None:
    input_file: str = "day3_input.txt"
    with open(input_file) as file:
        for line in file.readlines():
            bank = batteryBank(line.rstrip())
            logger.info("highest digit in bank: %i", bank._get_highest_joltage())

if __name__ == "__main__":
    main()
