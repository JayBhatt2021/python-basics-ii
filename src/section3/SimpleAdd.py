class SimpleAdd:
    """A class representing a simple addition calculator."""

    def __init__(self) -> None:
        """Initialize the simple addition calculator."""
        self.text_field_num = 1
        self.user_nums = []

    def enter_number(self) -> None:
        """Enter a number into the calculator."""
        while True:
            try:
                print(f"Text Field #{self.text_field_num}")
                number = float(input("Enter a number: "))

                self.user_nums.append(number)
                self.text_field_num += 1
                print()
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

    def calculate_sum(self) -> None:
        """Calculate the sum of the two entered numbers."""
        try:
            first_operand, second_operand = self.user_nums[0], self.user_nums[1]
            print(
                f"The sum of {first_operand:.2f} and {second_operand:.2f} is "
                f"{(first_operand + second_operand):.2f}."
            )
        except Exception as e:
            print(f'\nAn unexpected error occurred: "{e}".')


def main() -> None:
    """Run the simple addition calculator program."""
    try:
        simple_add = SimpleAdd()
        simple_add.enter_number()
        simple_add.enter_number()
        simple_add.calculate_sum()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
