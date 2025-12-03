from asyncio.log import logger
import logging

logging.basicConfig(level=logging.DEBUG)


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


def main() -> None:
    input_file: str = "day2_input.txt"
    product_ID_intervals: list[str] = []
    with open(input_file) as file:
        for line in file.readlines():
            # rewrite with extend
            product_ID_intervals = line.split(sep=",")
    logger.info(product_ID_intervals)

    for interval_str in product_ID_intervals:
        logger.debug("interval %s", interval_str)
        interval = product_ID_interval(interval_str)
        first_ID = interval._get_first_ID()
        last_ID = interval._get_last_ID()

        logger.debug("first ID %i, last ID %i", first_ID, last_ID)


if __name__ == "__main__":
    main()
