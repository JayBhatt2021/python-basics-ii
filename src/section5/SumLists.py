from typing import List


class Node:
    """A class representing a node in a doubly linked list."""

    def __init__(self, num: int) -> None:
        """Initialize a node with a value.

        :param num: The value of the node.
        """
        self.num = num
        self.previous = None
        self.next = None


class DoublyLinkedList:
    """A class representing a doubly linked list."""

    def __init__(self, head: Node = None) -> None:
        """Initialize an instance of DoublyLinkedList with an optional head
        node.

        :param head: The head node of the list.
        """
        self.head = head

    def __str__(self) -> str:
        """Return a string representation of DoublyLinkedList.

        :return: The string representation of DoublyLinkedList.
        """
        current, str_representation = self.head, ""

        while current:
            str_representation += f"{current.num} -> "
            current = current.next
        str_representation += "None"

        return str_representation

    def append(self, num: int) -> None:
        """Add a node with the given value to the end of the list.

        :param num: The value of the node to append.
        """
        new_node = Node(num)

        # Initializes the head if the doubly linked list is empty
        if not self.head:
            self.head = new_node
            return

        previous, current = None, self.head
        while current:
            previous = current
            current = current.next

        # Creates a double-link between the previous and new nodes
        previous.next = new_node
        new_node.previous = previous

    def calculate_sum(self) -> int:
        """Calculate the sum of all values in the doubly linked list.

        :return: The sum of all values.
        """
        current, total = self.head, 0

        while current:
            total += current.num
            current = current.next

        return total


def calculate_list_sum(num_list: List[int]) -> int:
    """Calculate the sum of all numbers in a list.

    :param num_list: The list of numbers.
    :return: The sum of all numbers.
    """
    return sum(num_list)


def main() -> None:
    """Main function to run the program."""
    try:
        # Input and Sum Calculation for Regular List
        list_size = int(
            input(
                "How many integers do you want to add to the list (max is 10)?"
                ": "
            )
        )
        list_size = min(list_size, 10)
        num_list = [
            int(input(f"Enter integer #{i}: ")) for i in range(1, list_size + 1)
        ]
        print(f"\nList: {num_list}")
        print(
            f"The sum of the numbers in the list is "
            f"{calculate_list_sum(num_list)}.\n"
        )

        # Input and Sum Calculation for Doubly Linked List
        linked_list_size = int(
            input(
                "How many integers do you want to add to the doubly linked "
                "list (max is 10)?: "
            )
        )
        linked_list_size = min(linked_list_size, 10)
        num_linked_list = DoublyLinkedList()
        for i in range(1, linked_list_size + 1):
            num_linked_list.append(int(input(f"Enter integer #{i}: ")))
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
