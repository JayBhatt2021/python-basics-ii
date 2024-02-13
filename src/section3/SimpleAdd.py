class SimpleAdd:
    """A class representing a button simulator."""

    def __init__(self) -> None:
        """Initialize the button simulator.

        :return: None
        """
        self.text_field_num = 1
        self.user_nums = []

    def enter_number(self) -> None:
        """Enter numbers into the calculator.

        :return: None
        """
        while True:
            try:
                print(f"Text Field #{self.text_field_num}")
                number = float(input("Enter a number: "))

                self.user_nums.append(number)
                self.text_field_num += 1
                print()
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")

    def calculate_sum(self) -> None:
        """Calculate the expression entered into the calculator.

        :return: None
        """
        try:
            first_operand, second_operand = self.user_nums[0], self.user_nums[1]
            print(
                f'The sum of {first_operand} and {second_operand} is '
                f'{first_operand + second_operand}.'
            )
        except Exception as e:
            print(f'An unexpected error occurred: "{e}".')


def main() -> None:
    """Run the calculator program.

    :return: None
    """
    try:
        simple_add = SimpleAdd()
        simple_add.enter_number()
        simple_add.enter_number()
        simple_add.calculate_sum()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'An unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
