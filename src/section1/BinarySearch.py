from typing import List
import random


def binary_search(num_list: List[int], key: int) -> int:
    """Search for a key in a list and print its indices if found.

    :param num_list: The list of numbers to search.
    :param key: The value to search for.
    :return: None
    """
    start = 0
    end = len(num_list) - 1
    middle = (start + end) // 2

    while start <= end:
        if num_list[middle] == key:
            return middle
        elif num_list[middle] < key:
            start = middle + 1
        else:
            end = middle - 1

        middle = (start + end) // 2

    return -(middle + 1)


def main() -> None:
    """Generate two lists of numbers, search for a user-provided key,
    and print the indices where the key is found.

    :return: None
    """
    try:
        # Prompts user for a value to search for
        key = int(input("Enter a value to search for: "))

        # Predefined list and search
        predefined_nums = [1, 4, 4, 22, -5, 10, 21, -47, 23]
        predefined_nums.sort()
        print(f"\nPredefined numbers: {predefined_nums}")
        predefined_nums_key_index = binary_search(predefined_nums, key)
        if predefined_nums_key_index < 0:
            print(
                f"{key} is not found. However, it would be inserted on index "
                f"{-1 * predefined_nums_key_index} to preserve the sorting "
                f"order."
            )
        else:
            print(f"{key} is found on index {predefined_nums_key_index}.")

        # Random list and search
        random_nums = [random.randint(-100, 100) for _ in range(20)]
        random_nums.sort()
        print(f"\nRandom numbers: {random_nums}")
        random_nums_key_index = binary_search(random_nums, key)
        if random_nums_key_index < 0:
            print(
                f"{key} is not found. However, it would be inserted on index "
                f"{-1 * random_nums_key_index} to preserve the sorting order."
            )
        else:
            print(f"{key} is found on index {random_nums_key_index}.")
    except ValueError:
        print("\nInput must be an integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram ended by user.")


if __name__ == "__main__":
    main()
