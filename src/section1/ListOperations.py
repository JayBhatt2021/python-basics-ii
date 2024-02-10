import random


def main() -> None:
    """Prompt user for name and age, then print the input.

    :return: None
    """
    # Prompts user for name and age
    nums = [1, 4, 13, 43, -25, 17, 22, -37, 29]
    random_nums = [random.randint(-100, 100) for _ in range(20)]
    print(f"nums: {nums}")
    print(f"random_nums: {random_nums}")

    # Prompts user for name and age
    nums_max = max(nums)
    print(f'\nMaximum Value of "nums": {nums_max}')
    random_nums_max = max(random_nums)
    print(f'Maximum Value of "random_nums": {random_nums_max}')
    print(f"Sum of the Maximum Values: {nums_max + random_nums_max}")


if __name__ == "__main__":
    main()
