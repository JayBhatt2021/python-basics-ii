import multiprocessing
import random
import time
from typing import List


def generate_random_list(
        lower_bound: int,
        upper_bound: int,
        length: int,
    ) -> List[int]:
    """Convert time from 24-hour to 12-hour format.

    :param original_time: The time in 24-hour format (HH:MM).
    :return: The time converted to 12-hour format (HH:MM AM/PM).
    :raises TimeFormatException: If the time format is invalid.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(length)]


def perform_bubble_sort(num_list: List[int]) -> List[int]:
    """Convert time from 24-hour to 12-hour format.

    :param original_time: The time in 24-hour format (HH:MM).
    :return: The time converted to 12-hour format (HH:MM AM/PM).
    :raises TimeFormatException: If the time format is invalid.
    """
    n = len(num_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num_list[j + 1] > num_list[j]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list

def perform_parallel_sort(num_list: List[int]) -> List[int]:
    """Convert time from 24-hour to 12-hour format.

    :param original_time: The time in 24-hour format (HH:MM).
    :return: The time converted to 12-hour format (HH:MM AM/PM).
    :raises TimeFormatException: If the time format is invalid.
    """
    # Splits num_list into chunks for each process
    n = len(num_list)
    process_num = multiprocessing.cpu_count()
    chunk_size = n // process_num
    chunks = [num_list[i:i + chunk_size] for i in range(0, n, chunk_size)]

    # Creates a queue to collect sorted chunks
    result_queue = multiprocessing.Queue()

    # Creates and starts sorting processes
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(
            target=sort_chunk,
            args=(chunk, result_queue),
        )
        processes.append(process)
        process.start()

    # Waits for all processes to finish
    for process in processes:
        process.join()

    # Collects sorted chunks from the queue
    sorted_chunks = [result_queue.get() for _ in range(process_num)]

    # Merges sorted chunks
    sorted_num_list = sorted(sum(sorted_chunks, []))

    return sorted_num_list


def sort_chunk(chunk: List[int], result_queue: 'Queue') -> None:
    """Convert time from 24-hour to 12-hour format.

    :param original_time: The time in 24-hour format (HH:MM).
    :return: The time converted to 12-hour format (HH:MM AM/PM).
    :raises TimeFormatException: If the time format is invalid.
    """
    sorted_chunk = sorted(chunk)
    result_queue.put(sorted_chunk)


def main() -> None:
    """Main function to convert time."""
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
        print(
            f"It took {bubble_sort_duration:.2f} seconds to bubble sort the "
            f"list."
        )

        # Parallel Sort
        parallel_sort_start = time.time()
        sorted_random_list_copy = perform_parallel_sort(random_list_copy)
        parallel_sort_end = time.time()
        parallel_sort_duration = parallel_sort_end - parallel_sort_start

        print(f"\nParallel Sorted List: {sorted_random_list_copy}")
        print(
            f"It took {parallel_sort_duration:.2f} seconds to parallel sort "
            f"the list."
        )
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
