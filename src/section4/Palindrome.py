def is_palindrome(string: str) -> bool:
    """Check if a string is a palindrome.

    :param string: The input string.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Returns True if the string is empty or has only one character
    if len(string) <= 1:
        return True

    # Checks if the first and last characters are not equal
    if string[0] != string[-1]:
        return False

    # Recursively checks if the substring excluding the first and last
    # characters is a palindrome
    return is_palindrome(string[1:-1])


def main() -> None:
    """Run the program to check if a string is a palindrome."""
    try:
        input_str = input("Enter a string: ")
        is_palindrome_str = "a palindrome" \
            if is_palindrome(input_str.lower()) else "not a palindrome"
        print(f'\n"{input_str}" is {is_palindrome_str}.')
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
