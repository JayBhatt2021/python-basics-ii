from typing import List


class Node:
    """A class representing a node."""

    def __init__(self, num: int) -> None:
        """Initialize a bird.

        :param num: The name of the bird species.
        :return: None
        """
        self.num = num
        self.previous = None
        self.next = None


class DoublyLinkedList:
    """A class representing a bird survey."""

    def __init__(self, head: Node = None) -> None:
        """Initialize the bird survey.

        :return: None
        """
        self.head = head

    def __str__(self) -> str:
        """Initialize the bird survey.

        :return: Replace this
        """
        current, str_representation = self.head, ""

        while current:
            str_representation += f"{current.num} -> "
            current = current.next
        str_representation += "None"

        return str_representation

    def append(self, num: int) -> None:
        """Add a bird to the survey or increment its count if already present.

        :param species_name: The name of the bird species to add.
        :return: None
        """
        new_node = Node(num)

        # Initializes the head if the linked list is empty
        if not self.head:
            self.head = new_node
            return

        # Initializes the head if the linked list is empty
        current = self.head
        while current.next:
            current = current.next

        # Initializes the head if the linked list is empty
        current.next = new_node
        new_node.previous = current

    def calculate_sum(self) -> int:
        """Print the bird survey.

        :return: None
        """
        current, total = self.head, 0

        while current:
            total += current.num
            current = current.next

        return total


def calculate_list_sum(num_list: List[int]) -> int:
    """Print the bird survey.

    :return: None
    """
    return sum(num_list)


def main() -> None:
    """Generate two lists of numbers, search for a user-provided key, and print
    the indices where the key is found.

    :return: None
    """
    try:
        # --- List ---
        while True:
            list_count = int(
                input(
                    "How many integers do you want to add to the list (max is "
                    "10)?: "
                )
            )

            if list_count <= 10:
                break
            print("\nYou cannot enter more than 10 integers.")

        num_list = []
        print("\nList Numbers:")
        for i in range(1, list_count + 1):
            num = int(input(f"Enter integer #{i}: "))
            num_list.append(num)

        print(f"\nList: {num_list}")
        print(
            f"The sum of the numbers in the list is "
            f"{calculate_list_sum(num_list)}.\n"
        )

        # --- Doubly Linked List ---
        while True:
            linked_list_count = int(
                input(
                    "How many integers do you want to add to the doubly "
                    "linked list (max is 10)?: "
                )
            )

            if linked_list_count <= 10:
                break
            print("\nYou cannot enter more than 10 integers.")

        num_linked_list = DoublyLinkedList()
        print("\nDoubly Linked List Numbers:")
        for i in range(1, linked_list_count + 1):
            num = int(input(f"Enter integer #{i}: "))
            num_linked_list.append(num)

        print(f"\nDoubly Linked List: {num_linked_list}")
        print(
            f"The sum of the numbers in the doubly linked list is "
            f"{num_linked_list.calculate_sum()}."
        )
    except ValueError:
        print("\nInput must be an integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
