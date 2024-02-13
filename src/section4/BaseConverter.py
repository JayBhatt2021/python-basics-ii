class BaseConverter:
    """A class representing a simple addition calculator."""

    DECIMALS_TO_DIGITS = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "P",
        26: "Q",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z",
    }
    """A list of buttons."""

    def __init__(self, input_num, base) -> None:
        """Initialize the simple addition calculator.

        :return: None
        """
        self.input_num_str = input_num
        self.base = base

    def __str__(self) -> str:
        """Return a string representation of the octagon.

        :return: A string representing the octagon.
        """
        return (
            f"{self.input_num_str} in base 10 is equivalent to "
            f"{self.convert(self.input_num_str)} in base {self.base}."
        )

    def convert(self, num_str: str) -> str:
        """Enter numbers into the calculator.

        :return: None
        """
        num = int(num_str)
        dividend, remainder = num // self.base, num % self.base

        if not dividend:
            return self.DECIMALS_TO_DIGITS[remainder]

        return f"{self.convert(str(dividend))}{self.DECIMALS_TO_DIGITS[remainder]}"


def main() -> None:
    """Run the simple addition calculator program.

    :return: None
    """
    inputted_nums = ["753", "753", "9068", "692", "97867564534231201"]
    inputted_bases = [8, 16, 20, 2, 36]

    for tup in zip(inputted_nums, inputted_bases):
        print(BaseConverter(tup[0], tup[1]))


if __name__ == "__main__":
    main()
