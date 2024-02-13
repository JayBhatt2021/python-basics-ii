from abc import ABC
import math


class GeometricObject(ABC):
    """An abstract class representing a geometric object."""

    def __init__(self, side: float) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        self.side = side

    def __str__(self) -> str:
        """Return a string representation of the staff member.

        :return: A string representing the staff member.
        """
        return f"Side: {self.side:.2f} units"


class Octagon(GeometricObject):
    """replace this"""

    def __init__(self, side: float) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        super().__init__(side)

    def __str__(self) -> str:
        """Return a string representation of the staff member.

        :return: A string representing the staff member.
        """
        return (
            f"{super().__str__()}\nPerimeter: {self.perimeter():.2f} units\n"
            f"Area: {self.area():.2f} units^2"
        )

    def __eq__(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
        return isinstance(other, Octagon) and self.side == other.side

    def perimeter(self) -> float:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        return 8 * self.side

    def area(self) -> float:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        """
        return (2 + 4 / math.sqrt(2)) * self.side ** 2

    def clone(self) -> object:
        """

        :return:
        """
        return Octagon(self.side)


def main() -> None:
    """Demonstrate the functionality of the classes.

    :return: None
    """
    original_octagon = Octagon(4)
    print(f"Original Octagon:\n{original_octagon}")

    clone_octagon = original_octagon.clone()
    print(f"\nClone Octagon:\n{clone_octagon}")

    print(
        f"\nDo both octagons have the same attributes? "
        f"{original_octagon == clone_octagon}"
    )


if __name__ == "__main__":
    main()
