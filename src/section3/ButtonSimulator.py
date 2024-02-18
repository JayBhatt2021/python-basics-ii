class ButtonSimulator:
    """A class representing a button simulator."""

    BUTTONS = [
        "Button #1",
        "Button #2",
        "Button #3",
        "Button #4",
        "Button #5",
        "Button #6",
    ]
    """A list of buttons."""

    def __init__(self) -> None:
        """Initialize the button simulator."""
        print("Button Simulator:")

    def simulate_button_press(self) -> None:
        """Simulate pressing buttons."""
        while True:
            try:
                self.display_buttons()
                number = self.get_button_input()
                print(f"\n{self.BUTTONS[number - 1]} was pressed!")
                if self.should_stop():
                    break
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")

    def display_buttons(self) -> None:
        """Display the available buttons."""
        for i, button in enumerate(self.BUTTONS, start=1):
            print(f"{i}) {button}")

    def get_button_input(self) -> int:
        """Get user input for button press.

        :return: The number of the button to be pressed.
        """
        while True:
            number = int(input("Press a button (1-6): "))
            if 1 <= number <= 6:
                break
            print("\nPlease enter a number in the range [1, 6].")
            self.display_buttons()

        return number

    @staticmethod
    def should_stop() -> bool:
        """Check if the user wants to stop pressing buttons.

        :return: True if the user wants to stop, False otherwise.
        """
        return input(
            '\nDo you want to stop pressing buttons ("yes" or "no")?: '
        ).lower() == "yes"


def main() -> None:
    """Run the button simulator program."""
    try:
        button_simulator = ButtonSimulator()
        button_simulator.simulate_button_press()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'An unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
