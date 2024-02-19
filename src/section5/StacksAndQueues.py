from collections import deque
from typing import Deque, List


class ClothingItem:
    """Represents an item of clothing."""

    def __init__(
        self,
        name: str,
        color: str,
        washed_at_high_temp: bool,
    ) -> None:
        """Initialize a clothing item.

        :param name: The name of the clothing item.
        :param color: The color of the clothing item.
        :param washed_at_high_temp: Whether the clothing item can be washed at
                                    high temperature.
        """
        self.name = name
        self.color = color
        self.washed_at_high_temp = washed_at_high_temp


class ClothesStack:
    """Represents a stack of clothing items."""

    def __init__(self) -> None:
        """Initialize the clothes stack."""
        self.clothes_stack: List[ClothingItem] = []

    def push(self, clothing_item: ClothingItem) -> None:
        """Push a clothing item onto the stack.

        :param clothing_item: The clothing item to push.
        """
        if len(self.clothes_stack) < 20:
            self.clothes_stack.append(clothing_item)
            return

        raise IndexError("The stack is full!")

    def pop(self) -> ClothingItem:
        """Pop a clothing item from the stack.

        :return: The popped clothing item.
        """
        if self.clothes_stack:
            return self.clothes_stack.pop()

        raise IndexError("You cannot pop from an empty stack!")

    def peek(self) -> ClothingItem:
        """Get the top clothing item from the stack without removing it.

        :return: The top clothing item.
        """
        if self.clothes_stack:
            return self.clothes_stack[-1]

        raise IndexError("The stack is empty!")

    def get_clothes_of_color(self, color: str) -> List[ClothingItem]:
        """Get all clothing items of a specific color.

        :param color: The color of the clothing items to retrieve.
        :return: A list of clothing items with the specified color.
        """
        return [
            clothing_item for clothing_item in self.clothes_stack
            if clothing_item.color == color
        ]

    def get_num_of_clothes_that_can_be_washed_at_high_temperatures(self) -> int:
        """Get the number of clothing items that can be washed at high
        temperatures.

        :return: The number of clothing items that can be washed at high
                 temperatures.
        """
        return sum(
            1 for clothing_item in self.clothes_stack
            if clothing_item.washed_at_high_temp
        )


class Food:
    """Represents a food item."""

    def __init__(
        self,
        name: str,
        calories_per_serving: float,
        servings_num: float
    ) -> None:
        """Initialize a food item.

        :param name: The name of the food item.
        :param calories_per_serving: The number of calories per serving of the
                                     food item.
        :param servings_num: The number of servings of the food item.
        """
        self.name = name
        self.calories_per_serving = calories_per_serving
        self.servings_num = servings_num


class FoodQueue:
    """Represents a queue of food items."""

    def __init__(self) -> None:
        """Initialize the food queue."""
        self.food_queue: Deque[Food] = deque()

    def enqueue(self, food: Food) -> None:
        """Enqueue a food item into the queue.

        :param food: The food item to enqueue.
        """
        if len(self.food_queue) < 20:
            self.food_queue.append(food)
            return

        raise IndexError("The queue is full!")

    def dequeue(self) -> Food:
        """Dequeue a food item from the queue.

        :return: The dequeued food item.
        """
        if self.food_queue:
            return self.food_queue.popleft()

        raise IndexError("You cannot dequeue from an empty queue!")

    def peek(self) -> Food:
        """Get the first food item in the queue without removing it.

        :return: The first food item in the queue.
        """
        if self.food_queue:
            return self.food_queue[0]

        raise IndexError("The queue is empty!")


def main() -> None:
    """The main function."""
    pass


if __name__ == "__main__":
    main()
