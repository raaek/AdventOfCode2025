from asyncio.log import logger
import logging

logging.basicConfig(level=logging.INFO)


class product_ID_interval:
    def __init__(self, interval: str):
        self.interval = interval
        left, _, right = interval.rpartition("-")
        self.first_ID = int(left)
        self.last_ID = int(right)

    def _get_first_ID(self) -> int:
        return self.first_ID

    def _get_last_ID(self) -> int:
        return self.last_ID

    def _find_invalid_IDS(self) -> int:
        invalid_IDs: list[int] = []
        first_ID = self.first_ID
        last_ID = self.last_ID
        for id in range(first_ID, last_ID + 1):
            length_ID = len(str(id))
            divisors: list[int] = []
            for j in range(1, int(length_ID / 2) + 1):
                if is_divisor(j, length_ID):
                    divisors.append(j)
            for k in divisors:
                id_str = str(id)
                id_temp = id_str.replace(id_str[:k], "")
                if id_temp == "":
                    invalid_IDs.append(id)
                    break

        return sum(invalid_IDs)


def is_divisor(divisor: int, dividend: int) -> bool:
    if (dividend / divisor) == (dividend // divisor):
        is_divisor = True
    else:
        is_divisor = False
    return is_divisor


def main() -> None:
    input_file: str = "day2_input.txt"
    product_ID_intervals: list[str] = []
    total_of_invalid_IDs: int = 0
    with open(input_file) as file:
        for line in file.readlines():
            product_ID_intervals.extend(line.split(sep=","))
    logger.info(product_ID_intervals)

    for interval_str in product_ID_intervals:
        logger.debug("interval %s", interval_str)
        interval = product_ID_interval(interval_str)
        first_ID = interval._get_first_ID()
        last_ID = interval._get_last_ID()

        logger.debug("first ID %i, last ID %i", first_ID, last_ID)

        invalid_IDs = interval._find_invalid_IDS()
        total_of_invalid_IDs = total_of_invalid_IDs + invalid_IDs

        logger.info("total sum of invalid IDs %i", total_of_invalid_IDs)


if __name__ == "__main__":
    main()