def is_palindrome(string: str) -> bool:
    """Count the number of vowels in a given string.

    :param string: The input string.
    :return: The count of vowels in the string.
    """
    if not string:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


def main() -> None:
    """Run the program to count vowels in a string entered by the user.

    :return: None
    """
    try:
        input_str = input("Enter a string: ")
        print(
            f'\n"{input_str}" is'
            f'{" " if is_palindrome(input_str.lower()) else " not "}a '
            f'palindrome.'
        )
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'An unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
