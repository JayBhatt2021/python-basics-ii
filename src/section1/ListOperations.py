from typing import List
import random


def longest_positive_continuous_length(num_list: List[int]) -> int:
    """Find the length of the longest continuous series of positive numbers in a
    list.

    :param num_list: The list of numbers.
    :return: The length of the longest continuous series of positive numbers.
    """
    length, longest_length = 0, 0

    for num in num_list:
        if num > 0:
            length += 1
        else:
            # If the current series is longer than the longest recorded series,
            # update the longest length
            if length > longest_length:
                longest_length = length

            length = 0

    # If the last positive series is the longest, update the longest length
    if length > longest_length:
        longest_length = length

    return longest_length


def main() -> None:
    """Generate two lists of numbers, find the maximum values from each,
    calculate their sum, and determine the length of the longest continuous
    series of positive numbers in each list.
    """
    # Generates two integer lists and prints them
    predefined_nums = [1, 4, 13, 43, -25, 17, 22, -37, 29]
    random_nums = [random.randint(-100, 100) for _ in range(20)]
    print(f"Predefined numbers: {predefined_nums}")
    print(f"Random numbers: {random_nums}")

    # Finds the max of each list, calculates their sum, and prints them
    predefined_max = max(predefined_nums)
    random_max = max(random_nums)
    print(f"\nMaximum value in the predefined list: {predefined_max}")
    print(f"Maximum value in the random list: {random_max}")
    print(f"Sum of the maximum values: {predefined_max + random_max}")

    # Prints the length of the longest continuous series of positive numbers in
    # each list
    print(
        f"\nThe length of the longest continuous series of positive numbers in "
        f"the predefined list: "
        f"{longest_positive_continuous_length(predefined_nums)}"
    )
    print(
        f"The length of the longest continuous series of positive numbers in "
        f"the random list: {longest_positive_continuous_length(random_nums)}"
    )


if __name__ == "__main__":
    main()
