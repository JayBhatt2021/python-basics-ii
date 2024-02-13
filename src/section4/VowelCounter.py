def count_vowels(string: str) -> int:
    """Calculate how much the piecemeal vacation is over budget.

    :return: The amount by which the vacation is over budget.
    """
    if not string:
        return 0

    return count_vowels(string[1::]) + (1 if is_vowel(string[0]) else 0)


def is_vowel(char: str) -> bool:
    """Calculate how much the piecemeal vacation is over budget.

    :return: The amount by which the vacation is over budget.
    """
    return char in ["a", "e", "i", "o", "u"]


def main() -> None:
    """Generate two types of vacations, prompt for input, and display details.

    :return: None
    """
    try:
        input_str = input("Enter a string: ")
        print(
            f"\nThere are {count_vowels(input_str.lower())} vowel(s) in this "
            f"string."
        )
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'An unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
