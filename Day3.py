from asyncio.log import logger
import logging

logging.basicConfig(level=logging.DEBUG)


class batteryBank:
    def __init__(self, bank: str):
        self.bank = bank

    def _get_highest_joltage(self) -> int:
        bank = self.bank
        logger.debug("bank: %s", bank)
        highest_digit = highest_digit_in(bank)
        if bank.index(str(highest_digit)) == len(bank)-1:
            logger.debug("highest digit (%i) in last place", highest_digit)
            second_highest_digit = highest_digit
            updated_bank = bank[:-1]
            logger.debug("updated bank: %s", updated_bank)
            first_highest_digit = highest_digit_in(updated_bank)
        else:
            first_highest_digit = highest_digit
            index = bank.index(str(highest_digit))
            logger.debug("highest digit (%i) in %i place", highest_digit, index)
            updated_bank = bank[index+1:]
            logger.debug("updated bank: %s", updated_bank)
            second_highest_digit = highest_digit_in(updated_bank)
            logger.debug("second highest digit (%i)", second_highest_digit)
        highest_joltage = int(str(first_highest_digit) + str(second_highest_digit))
        logger.debug("highest joltage: %i", highest_joltage)
        return highest_joltage


def highest_digit_in(sequence: str) -> int:
    highest_digit = max([int(digit) for digit in sequence])
    logger.debug(highest_digit)
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
