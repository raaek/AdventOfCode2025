from asyncio.log import logger
import logging

logging.basicConfig(level=logging.DEBUG)


class batteryBank:
    num_batteries_needed: int = 12 # 2 for part 1

    def __init__(self, bank: str):
        self.bank = bank

    def _get_highest_joltage(self) -> int:
        bank = self.bank
        num_batteries_needed = self.num_batteries_needed
        highest_joltage: list = [None] * num_batteries_needed
        index: int = 0
        logger.debug("bank: %s", bank)
        for i in range(1, num_batteries_needed+1):
            updated_bank = bank[index:len(bank)-num_batteries_needed+i]
            logger.debug("updated bank %s", updated_bank)
            highest_digit = highest_digit_in(updated_bank)
            highest_joltage[i-1] = highest_digit
            logger.debug("joltage list so far %s", highest_joltage)
            index = index + 1 + updated_bank.index(str(highest_digit))
        num_highest_joltage = int("".join(str(x) for x in highest_joltage))
        logger.debug("highest joltage: %i", num_highest_joltage)
        return num_highest_joltage


def highest_digit_in(sequence: str) -> int:
    highest_digit = max([int(digit) for digit in sequence])
    return highest_digit


def main() -> None:
    input_file: str = "day3_input.txt"
    total_output_joltage: int = 0
    with open(input_file) as file:
        for line in file.readlines():
            bank = batteryBank(line.rstrip())
            highest_joltage = bank._get_highest_joltage()
            # logger.info("highest joltage in bank: %i", highest_joltage)
            total_output_joltage = total_output_joltage + highest_joltage

    logger.info("total output joltage %i", total_output_joltage)


if __name__ == "__main__":
    main()
