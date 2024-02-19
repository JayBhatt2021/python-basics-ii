class BaseConverter:
    """A class representing a base converter."""

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
    """A dictionary that maps decimal values to digits."""

    def __init__(self, input_num: int, base: int) -> None:
        """Initialize the base converter.

        :param input_num: The number to convert.
        :param base: The base to convert to.
        """
        self.input_num = input_num
        self.base = base

    def __str__(self) -> str:
        """Return a string representation of the conversion.

        :return: A string representing the conversion result.
        """
        return (
            f"{self.input_num} in base 10 is equivalent to "
            f"{self.convert(str(self.input_num))} in base {self.base}."
        )

    def convert(self, num_str: str) -> str:
        """Convert the input number to the specified base recursively.

        :param num_str: The number to convert.
        :return: The converted number as a string.
        """
        num = int(num_str)
        quotient, remainder = divmod(num, self.base)

        # Returns the remainder-digit value if the quotient is 0
        if not quotient:
            return self.DECIMALS_TO_DIGITS[remainder]

        # Recursively calls the convert method with the quotient and appends the
        # remainder-digit value
        return self.convert(str(quotient)) + self.DECIMALS_TO_DIGITS[remainder]


def main() -> None:
    """Run the base converter program."""
    try:
        input_num = int(input("Enter an integer: "))

        while True:
            base = int(input("Enter the base to convert to: "))
            if 2 <= base <= 36:
                print()
                break
            print("\nThe base must be between 2 and 36, inclusive.")

        print(BaseConverter(input_num, base))
    except ValueError:
        print("\nPlease enter a valid integer! Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
