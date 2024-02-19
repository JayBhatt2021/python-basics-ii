def count_vowels(string: str) -> int:
    """Count the number of vowels in a given string.

    :param string: The input string.
    :return: The count of vowels in the string.
    """
    # Returns 0 if the string is empty
    if not string:
        return 0

    # Recursively counts vowels in the substring starting from the second
    # character and adds 1 to the count if the first character is a vowel
    return count_vowels(string[1:]) + (1 if is_vowel(string[0]) else 0)


def is_vowel(char: str) -> bool:
    """Check if a character is a vowel.

    :param char: The character to check.
    :return: True if the character is a vowel, False otherwise.
    """
    return char in {'a', 'e', 'i', 'o', 'u'}


def main() -> None:
    """Run the program to count vowels in a string entered by the user."""
    try:
        input_str_lower = input("Enter a string: ").lower()
        print(
            f"\nThere are {count_vowels(input_str_lower)} vowel(s) in this "
            f"string."
        )
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
