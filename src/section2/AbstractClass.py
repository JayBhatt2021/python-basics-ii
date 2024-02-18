from abc import ABC
import math


class GeometricObject(ABC):
    """An abstract class representing a geometric object."""

    def __init__(self, side: float) -> None:
        """Initialize the geometric object.

        :param side: The length of a side of the geometric object.
        """
        self.side = side

    def __str__(self) -> str:
        """Return a string representation of the geometric object.

        :return: A string representing the geometric object.
        """
        return f"Side: {self.side:.2f} units"


class Octagon(GeometricObject):
    """A class representing an octagon."""

    def __init__(self, side: float) -> None:
        """Initialize the octagon.

        :param side: The length of a side of the octagon.
        """
        super().__init__(side)

    def __str__(self) -> str:
        """Return a string representation of the octagon.

        :return: A string representing the octagon.
        """
        return (
            f"{super().__str__()}\nPerimeter: {self.perimeter():.2f} units\n"
            f"Area: {self.area():.2f} units^2"
        )

    def __eq__(self, other: object) -> bool:
        """Check if two octagons are equal.

        :param other: Another object to compare with.
        :return: True if both objects are octagons with the same side length,
                 False otherwise.
        """
        return isinstance(other, Octagon) and self.side == other.side

    def perimeter(self) -> float:
        """Calculate the perimeter of the octagon.

        :return: The perimeter of the octagon.
        """
        return 8 * self.side

    def area(self) -> float:
        """Calculate the area of the octagon.

        :return: The area of the octagon.
        """
        return (2 + 4 / math.sqrt(2)) * self.side ** 2

    def clone(self) -> "Octagon":
        """Create a clone of the octagon.

        :return: A new octagon object with the same side length.
        """
        return Octagon(self.side)


def main() -> None:
    """Demonstrate the functionality of the classes."""
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
