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


def perform_parallel_sum(num_list: List[int]) -> int:
    """Calculate the sum of integers in a list in parallel using multiple
    threads.

    :param num_list: The list of integers to sum.
    :return: The sum of integers in the list.
    """
    # Gets the length of num_list and determines the number of threads to use
    n, num_threads = len(num_list), multiprocessing.cpu_count()

    # Divides the list into smaller chunks
    chunk_size = n // num_threads
    chunks = [num_list[i:i + chunk_size] for i in range(0, n, chunk_size)]

    # Initializes ThreadPoolExecutor with max_workers set to num_threads
    with (concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as
          executor):
        # Submits tasks to the executor
        futures = [executor.submit(sum_chunk, chunk) for chunk in chunks]

        # Gets results from the futures
        results = [
            future.result()
            for future in concurrent.futures.as_completed(futures)
        ]

    # Adds the results from the futures
    return sum(results)


def sum_chunk(chunk: List[int]) -> int:
    """Calculate the sum of integers in a chunk of a list.

    :param chunk: The chunk of integers to sum.
    :return: The sum of integers in the chunk.
    """
    return sum(chunk)


def main() -> None:
    """Main function to calculate the sum of integers in parallel."""
    try:
        # Generates a random list
        random_list = generate_random_list(-100_000, 100_000, 100_000)

        # Parallel Sum
        parallel_sum_start = time.time()
        parallel_sum = perform_parallel_sum(random_list)
        parallel_sum_end = time.time()
        parallel_sum_duration = parallel_sum_end - parallel_sum_start

        print(f"Sum: {parallel_sum}")
        print(f"Parallel Sum Time: {parallel_sum_duration:.8f} seconds")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
