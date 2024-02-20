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

    def __str__(self) -> str:
        """Return a string representation of the clothing item.

        :return: The string representation of the clothing item.
        """
        washed_at_high_temp_str = "Yes" if self.washed_at_high_temp else "No"
        return (
            f"Name: {self.name}\nColor: {self.color}\nCan be washed at high "
            f"temperatures? {washed_at_high_temp_str}"
        )


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

    def print_clothing_items(self) -> None:
        """Print all clothing items."""
        for i, clothing_item in enumerate(self.clothes_stack, start=1):
            print(f"Clothing Item #{i}")
            print(clothing_item)
            print()

    def get_clothes_of_color(self, color: str) -> List[ClothingItem]:
        """Get all clothing items of a specific color.

        :param color: The color of the clothing items to retrieve.
        :return: A list of clothing items with the specified color.
        """
        return [
            clothing_item for clothing_item in self.clothes_stack
            if clothing_item.color == color
        ]

    def get_count_of_high_temp_washable_clothes(self) -> int:
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

    def __str__(self) -> str:
        """Return a string representation of the food item.

        :return: The string representation of the food item.
        """
        return (
            f"Name: {self.name}\nCalories per Serving: "
            f"{self.calories_per_serving:.2f}\nNumber of Servings: "
            f"{self.servings_num:.2f}"
        )


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

    def print_food_items(self) -> None:
        """Print all food items."""
        for i, item in enumerate(self.food_queue, start=1):
            print(f"Food Item #{i}")
            print(item)
            print()

    def calculate_average_calories_per_serving(self) -> float:
        """Calculate the average calories per serving of all food items.

        :return: The average calories per serving of all food items.
        """
        if not self.food_queue:
            return 0.0

        total_calories_per_serving = sum(
            food_item.calories_per_serving for food_item in self.food_queue
        )
        return total_calories_per_serving / len(self.food_queue)

    def obtain_food_with_highest_total_calories(self) -> Food:
        """Obtain the food item with the highest total calories.

        :return: The food item with the highest total calories.
        """
        if not self.food_queue:
            raise ValueError("The queue is empty!")

        return max(
            self.food_queue,
            key=lambda food_item:
                food_item.calories_per_serving * food_item.servings_num,
        )


def main() -> None:
    """The main function."""
    try:
        # ClothesStack Methods
        stack_size = int(
            input(
                "How many clothing items do you want to push to the stack (max "
                "is 20)?: "
            )
        )
        stack_size = min(stack_size, 20)
        clothes_stack = ClothesStack()
        for i in range(1, stack_size + 1):
            print(f"Clothing Item #{i}")
            name = input("Enter the name of the clothing item: ")
            color = input("Enter the color of the clothing item: ")

            washed_at_high_temp_str = input(
                'Can the clothing item be washed at high temperatures ("yes" '
                'or "no")?: '
            )
            print()
            washed_at_high_temp = washed_at_high_temp_str.lower() == "yes"

            clothes_stack.push(ClothingItem(name, color, washed_at_high_temp))

        print("The following clothing item has been popped from the stack:")
        print(clothes_stack.pop())

        print("\nThe following clothing item is on the top of the stack:")
        print(clothes_stack.peek())

        print("\nAll Clothing Items:")
        print(clothes_stack.print_clothing_items())

        color = input(
            "\nWhat is the color of the clothing item(s) do you want to "
            "retrieve?: "
        )
        color_clothes = clothes_stack.get_clothes_of_color(color)
        print(f'All Clothing Items of Color "{color}":')
        for i, clothing_item in enumerate(color_clothes, start=1):
            print(f"Clothing Item #{i}")
            print(clothing_item)
            print()

        print(
            f"There are "
            f"{clothes_stack.get_count_of_high_temp_washable_clothes()} "
            f"clothing item(s) that can be washed at high temperatures."
        )

        # FoodQueue Methods
        queue_size = int(
            input(
                "\nHow many food items do you want to enqueue to the queue (max"
                " is 20)?: "
            )
        )
        queue_size = min(queue_size, 20)
        food_queue = FoodQueue()
        for i in range(1, queue_size + 1):
            print(f"Food Item #{i}")
            name = input("Enter the name of the food item: ")
            calories_per_serving = float(
                input(
                    "Enter the number of calories per serving of the food item"
                    ": "
                )
            )
            servings_num = float(
                input(
                    "Enter the number of servings of the food item: "
                )
            )
            print()

            food_queue.enqueue(Food(name, calories_per_serving, servings_num))

        print("The following food item has been dequeued from the queue:")
        print(food_queue.dequeue())

        print("\nThe following food item is in the front of the queue:")
        print(food_queue.peek())

        print("\nAll Food Items:")
        print(food_queue.print_food_items())

        print(
            f"\nThe average calories per serving of all food items is "
            f"{food_queue.calculate_average_calories_per_serving()} calories "
            f"per serving."
        )

        max_cal_food = food_queue.obtain_food_with_highest_total_calories()
        print(
            f"\nThe following food item contains the highest total calories ("
            f"{max_cal_food.calories_per_serving * max_cal_food.servings_num} "
            f"calories):"
        )
        print(max_cal_food)
    except ValueError:
        print("\nThe input must be valid! Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
