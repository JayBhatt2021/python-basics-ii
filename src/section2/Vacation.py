from abc import ABC, abstractmethod
from typing import Dict


class Vacation(ABC):
    """An abstract class representing a Vacation."""

    def __init__(self, budget: float, destination: str) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        self.budget = budget
        self.destination = destination

    @abstractmethod
    def over_budget(self) -> float:
        """Abstract method to calculate how much the vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        pass


class AllInclusiveVacation(Vacation):
    """A class representing an all-inclusive vacation."""

    def __init__(
        self,
        budget: float,
        destination: str,
        brand: str,
        rating: int,
        price: float,
    ) -> None:
        """Initialize an all-inclusive vacation.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :param brand: The brand of the all-inclusive vacation.
        :param rating: The rating of the all-inclusive vacation.
        :param price: The price of the all-inclusive vacation.
        """
        super().__init__(budget, destination)
        self.brand = brand
        self.rating = rating
        self.price = price

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        budget_difference = self.over_budget()
        over_budget_str = (
            f"This all-inclusive vacation is ${abs(budget_difference):.2f} "
            f"{'over' if budget_difference > 0 else 'under'} budget."
        )

        return (
            f"Budget: ${self.budget:.2f}\nDestination: {self.destination}\n"
            f"Brand: {self.brand}\nRating: {self.rating} stars\nPrice: "
            f"${self.price:.2f}\n{over_budget_str}"
        )

    def over_budget(self) -> float:
        """Calculate how much the all-inclusive vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        return self.price - self.budget


class PiecemealVacation(Vacation):
    """A class representing a piecemeal vacation."""

    def __init__(self, budget: float, destination: str) -> None:
        """Initialize a piecemeal vacation.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        super().__init__(budget, destination)
        self.items_to_costs: Dict[str, float] = {}

    def __str__(self) -> str:
        """Return a string representation of the piecemeal vacation.

        :return: A string representing the piecemeal vacation.
        """
        budget_difference = self.over_budget()
        over_budget_str = (
            f"This piecemeal vacation is ${abs(budget_difference):.2f} "
            f"{'over' if budget_difference > 0 else 'under'} budget."
        )

        return (
            f"Budget: ${self.budget:.2f}\nDestination: {self.destination}\n"
            f"Items and Their Respective Costs: {self.items_to_costs}\n"
            f"{over_budget_str}"
        )

    def assign_item_to_cost(self, item: str, cost: float) -> None:
        """Assign an item with its cost in the piecemeal vacation.

        :param item: The item to add to the vacation.
        :param cost: The cost associated with the item.
        """
        self.items_to_costs[item] = cost

    def over_budget(self) -> float:
        """Calculate how much the piecemeal vacation is over budget.

        :return: The amount by which the vacation is over budget.
        """
        total_cost = sum(self.items_to_costs.values())
        return total_cost - self.budget


def main() -> None:
    """Generate two types of vacations, prompt for input, and display details.
    """
    try:
        # All-inclusive Vacation
        ai_vacation_budget = float(
            input("Enter the budget for your all-inclusive vacation: ")
        )
        ai_vacation_destination = input(
            "Enter the destination for your all-inclusive vacation: "
        )
        ai_vacation_brand = input(
            "Enter the brand for your all-inclusive vacation: "
        )
        ai_vacation_rating = int(
            input("Enter the rating for your all-inclusive vacation: ")
        )
        ai_vacation_price = float(
            input("Enter the price for your all-inclusive vacation: ")
        )
        ai_vacation = AllInclusiveVacation(
            ai_vacation_budget,
            ai_vacation_destination,
            ai_vacation_brand,
            ai_vacation_rating,
            ai_vacation_price,
        )

        # Piecemeal Vacation
        p_vacation_budget = float(
            input("\nEnter the budget for your piecemeal vacation: ")
        )
        p_vacation_destination = input(
            "Enter the destination for your piecemeal vacation: "
        )
        p_vacation = PiecemealVacation(
            p_vacation_budget,
            p_vacation_destination,
        )

        while True:
            p_item = input(
                "\nEnter an item you must pay for in your piecemeal vacation: "
            )
            p_cost = float(input("Enter the cost for this item: "))
            p_vacation.assign_item_to_cost(p_item, p_cost)

            continue_adding_items = input(
                '\nDo you want to continue adding items ("yes" or "no")? '
            )
            if continue_adding_items.lower() != "yes":
                break

        # Displays both vacations
        print(f"\nAll-inclusive Vacation:\n{ai_vacation}")
        print(f"\nPiecemeal Vacation:\n{p_vacation}")
    except ValueError:
        print("\nInput must be a valid number. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
