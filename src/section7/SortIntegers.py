import concurrent.futures
import multiprocessing
import random
import time
from typing import List


def generate_random_list(
        lower_bound: int,
        upper_bound: int,
        length: int,
) -> List[int]:
    """Generate a random list of integers within a specified range.

    :param lower_bound: The lower bound of the range.
    :param upper_bound: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A random list of integers.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(length)]


def perform_bubble_sort(num_list: List[int]) -> List[int]:
    """Sort a list of integers using bubble sort.

    :param num_list: The list of integers to sort.
    :return: The sorted list of integers.
    """
    n = len(num_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list


def perform_parallel_sort(num_list: List[int]) -> List[int]:
    """Sort a list of integers in parallel using multiple processes.

    :param num_list: The list of integers to sort.
    :return: The sorted list of integers.
    """
    # Gets the length of num_list and determines the number of threads to use
    n, num_threads = len(num_list), multiprocessing.cpu_count()

    # Splits the list into sub-lists for each thread
    chunk_size = n // num_threads
    chunks = [num_list[i:i + chunk_size] for i in range(0, n, chunk_size)]

    # Sorts each sub-list in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        sorted_chunks = list(executor.map(sort_chunk, chunks))

    # Merges the sorted sub-lists into a single sorted list
    return sorted(sum(sorted_chunks, []))


def sort_chunk(chunk: List[int]) -> List[int]:
    """Sort a chunk of a list of integers.

    :param chunk: The chunk of integers to sort.
    """
    return sorted(chunk)


def main() -> None:
    """Main function to compare bubble sort and parallel sort."""
    try:
        # Generates two random lists
        random_list = generate_random_list(-100_000, 100_000, 10_000)
        random_list_copy = random_list[:]

        # Bubble Sort
        bubble_sort_start = time.time()
        sorted_random_list = perform_bubble_sort(random_list)
        bubble_sort_end = time.time()
        bubble_sort_duration = bubble_sort_end - bubble_sort_start

        print(f"Bubble Sorted List: {sorted_random_list}")
        print(f"Bubble Sort Time: {bubble_sort_duration:.8f} seconds")

        # Parallel Sort
        parallel_sort_start = time.time()
        sorted_random_list_copy = perform_parallel_sort(random_list_copy)
        parallel_sort_end = time.time()
        parallel_sort_duration = parallel_sort_end - parallel_sort_start

        print(f"\nParallel Sorted List: {sorted_random_list_copy}")
        print(f"Parallel Sort Time: {parallel_sort_duration:.8f} seconds")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
