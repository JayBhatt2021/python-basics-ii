from typing import List
import random


def binary_search(num_list: List[int], key: int) -> int:
    """Search for a key in a sorted list using binary search.

    :param num_list: The list of numbers to search (must be sorted).
    :param key: The value to search for.
    :return: The index of the key if found, otherwise the index where it should
             be inserted to maintain sorted order.
    """
    start = 0
    end = len(num_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if num_list[middle] == key:
            return middle
        elif num_list[middle] < key:
            start = middle + 1
        else:
            end = middle - 1

    # If key is not found, return the negative insertion point
    return -start


def main() -> None:
    """Generate two lists of numbers, search for a user-provided key, and print
    the indices where the key is found.
    """
    try:
        # Prompts the user for a value to search for
        key = int(input("Enter a value to search for: "))

        # Predefined List
        predefined_nums = [1, 4, 4, 22, -5, 10, 21, -47, 23]
        predefined_nums.sort()
        print(f"\nPredefined numbers: {predefined_nums}")
        predefined_nums_key_index = binary_search(predefined_nums, key)
        if predefined_nums_key_index >= 0:
            print(f"{key} is found at index {predefined_nums_key_index}.")
        else:
            insert_index = -predefined_nums_key_index
            print(
                f"{key} is not found. It would be inserted at index "
                f"{insert_index} to maintain sorted order."
            )

        # Random List
        random_nums = sorted([random.randint(-100, 100) for _ in range(20)])
        print(f"\nRandom numbers: {random_nums}")
        random_nums_key_index = binary_search(random_nums, key)
        if random_nums_key_index >= 0:
            print(f"{key} is found at index {random_nums_key_index}.")
        else:
            insert_index = -random_nums_key_index
            print(
                f"{key} is not found. It would be inserted at index "
                f"{insert_index} to maintain sorted order."
            )
    except ValueError:
        print("\nInput must be an integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
