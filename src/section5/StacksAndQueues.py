from collections import deque
from typing import Deque, List


class ClothingItem:
    """Replace this."""

    def __init__(self, name: str, color: str,
                 washed_at_high_temp: bool) -> None:
        """

        :param name:
        :param color:
        :param washed_at_high_temp:
        """
        self.name = name
        self.color = color
        self.washed_at_high_temp = washed_at_high_temp


class ClothesStack:
    def __init__(self):
        """

        """
        self.clothes_stack: List[ClothingItem] = []

    def push(self, clothing_item: ClothingItem) -> None:
        """

        :param clothing_item:
        """
        if len(self.clothes_stack) < 20:
            self.clothes_stack.append(clothing_item)

        raise IndexError("The stack is full!")

    def pop(self) -> ClothingItem:
        """

        :return:
        """
        if len(self.clothes_stack) > 0:
            return self.clothes_stack.pop()

        raise IndexError("You cannot pop from an empty stack!")

    def peek(self) -> ClothingItem:
        """

        :return:
        """
        if len(self.clothes_stack) > 0:
            return self.clothes_stack[-1]

        raise IndexError("The stack is empty!")

    def get_clothes_of_color(self, color: str) -> List[ClothingItem]:
        """

        :param color:
        :return:
        """
        return [
            clothing_item for clothing_item in self.clothes_stack
            if clothing_item.color == color
        ]

    def get_num_of_clothes_that_can_be_washed_at_high_temperatures(self) -> int:
        """

        :return:
        """
        return sum(
            [
                1 for clothing_item in self.clothes_stack
                if clothing_item.washed_at_high_temp
            ]
        )


class Food:
    """Replace this."""

    def __init__(self, name: str, calories_per_serving: float,
                 servings_num: float) -> None:
        """

        :param name:
        :param calories_per_serving:
        :param servings_num:
        """
        self.name = name
        self.calories_per_serving = calories_per_serving
        self.servings_num = servings_num


class FoodQueue:
    """Replace this."""

    def __init__(self) -> None:
        """

        """
        self.food_queue: Deque[Food] = deque()

    def enqueue(self, food: Food) -> None:
        """

        :param food:
        :return:
        """
        if len(self.food_queue) < 20:
            self.food_queue.append(food)

        raise IndexError("The queue is full!")

    def dequeue(self) -> Food:
        """

        :param food:
        :return:
        """
        if len(self.food_queue) > 0:
            return self.food_queue.popleft()

        raise IndexError("You cannot dequeue from an empty queue!")

    def peek(self) -> Food:
        """

        :return:
        """
        if len(self.food_queue) > 0:
            return self.food_queue[0]

        raise IndexError("The queue is empty!")


def main() -> None:
    """

    :return:
    """
    pass


if __name__ == "__main__":
    main()
