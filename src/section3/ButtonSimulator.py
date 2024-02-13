class ButtonSimulator:
    """A class representing a simple calculator."""

    BUTTONS = [
        "Button #1",
        "Button #2",
        "Button #3",
        "Button #4",
        "Button #5",
        "Button #6",
    ]
    """A set of arithmetic operators."""

    def __init__(self) -> None:
        """Initialize the calculator.

        :return: None
        """
        print("Button Simulator:")

    def press_buttons(self) -> None:
        """Enter numbers into the calculator.

        :return: None
        """
        while True:
            try:
                for i in range(1, 7):
                    print(f"{i}) {self.BUTTONS[i - 1]}")
                number = int(input("Press a button (1-6): "))
                if 1 <= number <= 6:
                    print(f"\n{self.BUTTONS[number - 1]} was pressed!")
                else:
                    print("\nPlease enter a number in the range [1, 6].")
                    continue
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
            else:
                if (input("\nDo you want to stop pressing buttons (yes/no): ")
                        .lower() == "yes"):
                    break


def main() -> None:
    """Run the calculator program.

    :return: None
    """
    try:
        button = ButtonSimulator()
        button.press_buttons()
    except KeyboardInterrupt:
        print("\n\nProgram ended by user.")
    except Exception as e:
        print(f'An unexpected error occurred: "{e}"')


if __name__ == "__main__":
    main()
