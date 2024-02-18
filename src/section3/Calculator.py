class Calculator:
    """A class representing a simple calculator."""

    OPERATORS = {"+", "-", "*", "/"}
    """A set of arithmetic operators."""

    def __init__(self) -> None:
        """Initialize the calculator."""
        self.expression_list = []

    def enter_numbers(self) -> None:
        """Enter numbers into the calculator."""
        while True:
            try:
                number = int(input("Enter a number (1-9): "))
                if 1 <= number <= 9:
                    self.expression_list.append(str(number))
                    if (input('\nStop entering numbers ("yes" or "no")?: ')
                            .lower() == "yes"):
                        print()
                        break
                    print()
                else:
                    print("\nPlease enter a number in the range [1, 9].")
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")

    def enter_operator(self) -> None:
        """Enter an operator into the calculator."""
        while True:
            operator = input('Enter an operator ("+", "-", "*", or "/"): ')
            if operator in self.OPERATORS:
                self.expression_list.append(operator)
                print()
                break
            else:
                print("\nPlease enter a valid operator.")

    def calculate_expression(self) -> None:
        """Calculate the expression entered into the calculator."""
        try:
            expression_str = "".join(self.expression_list)
            print(
                f'The result of the expression "{expression_str}" is '
                f'"{eval(expression_str):.2f}".'
            )
        except Exception as e:
            print(f'An error occurred: "{e}".')


def main() -> None:
    """Run the calculator program."""
    try:
        calculator = Calculator()
        calculator.enter_numbers()
        calculator.enter_operator()
        calculator.enter_numbers()
        calculator.calculate_expression()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
