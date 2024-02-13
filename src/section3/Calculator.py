class Calculator:
    """An abstract class representing a Vacation."""

    def __init__(self) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        self.operator_list = ["+", "-", "*", "/"]
        self.expression_list = []

    def enter_number(self) -> None:
        """Abstract method to calculate how much the vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        while True:
            number = int(input("Enter a number (1-9): "))
            if number < 1 or number > 9:
                print("\nPlease enter a number in the range [1, 9].")
                continue
            self.expression_list.append(str(number))

            stop_entering_numbers = input(
                "\nDo you want to stop entering numbers (enter 'yes' or 'no'): "
            )
            if stop_entering_numbers.lower() == "yes":
                print()
                break

    def enter_operator(self) -> None:
        """Abstract method to calculate how much the vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        while True:
            operator = input("Enter an operator (+, -, *, /): ")
            if operator not in self.operator_list:
                print("\nPlease enter a valid operator.")
                continue
            self.expression_list.append(operator)
            print()
            break

    def calculate_expression(self) -> None:
        """Abstract method to calculate how much the vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        expression_str = "".join(self.expression_list)

        operator_index = 1
        for i, char in enumerate(expression_str):
            if char in self.operator_list:
                operator_index = i
                break

        operator = expression_str[operator_index]
        operands = expression_str.split(operator)
        first_operand, second_operand = operands[0], operands[1]

        if operator == "+":
            print(
                f"The sum of {first_operand} and {second_operand} is "
                f"{int(first_operand) + int(second_operand)}."
            )
        elif operator == "-":
            print(
                f"The difference of {first_operand} and {second_operand} is "
                f"{int(first_operand) - int(second_operand)}."
            )
        elif operator == "*":
            print(
                f"The product of {first_operand} and {second_operand} is "
                f"{int(first_operand) * int(second_operand)}."
            )
        else:
            print(
                f"The dividend of {first_operand} and {second_operand} is "
                f"{int(first_operand) / int(second_operand):.2f}."
            )


def main() -> None:
    """Generate two types of vacations, prompt for input, and display details.

    :return: None
    """
    try:
        calculator = Calculator()
        calculator.enter_number()
        calculator.enter_operator()
        calculator.enter_number()
        calculator.calculate_expression()
    except ValueError:
        print("\nInput must be a valid integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram ended by user.")


if __name__ == "__main__":
    main()
