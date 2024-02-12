from abc import abstractmethod


class Vacation:
    """An abstract class representing a Vacation."""

    def __init__(self, budget: float, destination: str) -> None:
        """

        :param budget:
        :param destination:
        :return: None
        """
        self.budget = budget
        self.destination = destination

    @abstractmethod
    def over_budget(self) -> float:
        """

        :return:
        """
        pass


class AllInclusiveVacation(Vacation):
    """Replace this"""

    def __init__(self, budget: float, destination: str, brand: str, rating: int,
                 price: float) -> None:
        """

        :param budget:
        :param destination:
        :param brand:
        :param rating:
        :param price:
        :return: None
        """
        super().__init__(budget, destination)
        self.brand = brand
        self.rating = rating
        self.price = price

    def __str__(self) -> str:
        """

        :return:
        """
        budget_difference = self.over_budget()
        over_budget_str = (
            f"This all-inclusive vacation is ${budget_difference:.2f} over "
            f"budget."
        ) if budget_difference > 0 else (
            f"This all-inclusive vacation is ${-budget_difference:.2f} under "
            f"budget."
        )

        return (
            f"Budget: ${self.budget:.2f}\nDestination: {self.destination}\n"
            f"Brand: {self.brand}\nRating: {self.rating} stars\nPrice: "
            f"${self.price:.2f}\n{over_budget_str}"
        )

    def over_budget(self) -> float:
        """

        :return:
        """
        return self.price - self.budget


class PiecemealVacation(Vacation):
    """Replace this"""

    def __init__(self, budget: float, destination: str) -> None:
        """

        :param budget:
        :param destination:
        :return: None
        """
        super().__init__(budget, destination)
        self.items_to_costs = {}

    def __str__(self) -> str:
        """

        :return:
        """
        budget_difference = self.over_budget()
        over_budget_str = (
            f"This piecemeal vacation is ${budget_difference:.2f} over budget."
        ) if budget_difference > 0 else (
            f"This piecemeal vacation is ${-budget_difference:.2f} under "
            f"budget."
        )

        return (
            f"Budget: ${self.budget:.2f}\nDestination: {self.destination}\n"
            f"Items and their respective costs: {self.items_to_costs}\n"
            f"{over_budget_str}"
        )

    def assign_item_to_cost(self, item: str, cost: float) -> None:
        """

        :param item:
        :param cost:
        :return:
        """
        self.items_to_costs[item] = cost

    def over_budget(self) -> float:
        """

        :return:
        """
        total_cost = sum([cost for cost in self.items_to_costs.values()])
        return total_cost - self.budget


def main() -> None:
    """Generate two lists of numbers, search for a user-provided key, and print
    the indices where the key is found.

    :return: None
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
                "Do you want to continue adding items ('yes' or 'no')? "
            )
            if continue_adding_items.lower() == "no":
                break

        # Prints both vacations
        print(f"\nAll-inclusive Vacation:\n{ai_vacation}")
        print(f"\nPiecemeal Vacation:\n{p_vacation}")
    except ValueError:
        print("\nInput must be an integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram ended by user.")


if __name__ == "__main__":
    main()
