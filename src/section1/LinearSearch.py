from typing import List
import random


def linear_search(num_list: List[int], key: int) -> None:
    """Search for a key in a list and print its indices if found.

    :param num_list: The list of numbers to search.
    :param key: The value to search for.
    :return: None
    """
    key_indices = [i for i, num in enumerate(num_list) if num == key]

    if not key_indices:
        print(f"{key} is not found in the list.")
    else:
        print(f"{key} is found at indices: {key_indices}.")


def main() -> None:
    """Generate two lists of numbers, search for a user-provided key, and print
    the indices where the key is found.

    :return: None
    """
    try:
        # Prompts user for a value to search for
        key = int(input("Enter a value to search for: "))

        # Predefined List
        predefined_nums = [1, 4, 4, 22, -5, 10, 21, -47, 23]
        print(f"\nPredefined numbers: {predefined_nums}")
        linear_search(predefined_nums, key)

        # Random List
        random_nums = [random.randint(-100, 100) for _ in range(20)]
        print(f"\nRandom numbers: {random_nums}")
        linear_search(random_nums, key)
    except ValueError:
        print("\nInput must be an integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
