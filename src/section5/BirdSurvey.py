class Bird:
    """A class representing a simple calculator."""

    def __init__(self, species_name: str) -> None:
        """Initialize the calculator.

        :return: None
        """
        self.species_name = species_name
        self.count = 1
        self.next = None


class BirdSurvey:
    """A class representing a simple calculator."""

    def __init__(self, head: Bird = None) -> None:
        """Initialize the calculator.

        :return: None
        """
        self.head = head
        self.length = 0

    def append(self, bird_name: str) -> None:
        """Enter numbers into the calculator.

        :return: None
        """
        if not self.head:
            self.head = Bird(bird_name)
            self.length += 1
            return

        current = self.head

        while current.next:
            if current.species_name == bird_name:
                current.count += 1
                return

            current = current.next

        current.next = Bird(bird_name)
        self.length += 1

    def delete(self, bird_name: str) -> None:
        """Enter numbers into the calculator.

        :return: None
        """
        if self.length == 0:
            return

        if self.head.species_name == bird_name:
            self.head = self.head.next
            self.length -= 1
            return

        previous = None
        current = self.head

        while current:
            if current.species_name == bird_name:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def get_bird_count(self, bird_name: str) -> int:
        """

        :param bird_name:
        :return:
        """
        current = self.head

        while current:
            if current.species_name == bird_name:
                return current.count

            current = current.next

        return 0

    def print_survey(self) -> None:
        """

        :return:
        """
        current = self.head
        while current:
            print(f"Name = {current.species_name}, Count = {current.count}")
            current = current.next


def main() -> None:
    """Run the calculator program.

    :return: None
    """
    # You will write a program that uses BirdSurvey to record the data from a recent
    # bird survey.  Use a loop to read bird names until done is entered.  Illustrate
    # the use of each of the methods mentioned above, with the last being a Report
    # of all the species of birds entered and the count for each species.
    try:
        bird_survey = BirdSurvey()
        bird_total = int(
            input(
                "How many different types of birds do you want input in the "
                "survey? "
            )
        )

        for i in range(1, bird_total + 1):
            species_name = input(f"Enter the species name of bird #{i}: ")
            bird_survey.append(species_name)

        inputted_species = input(
            "\nEnter the species name of the bird you want to see the count "
            "of: "
        )
        inputted_species_count = bird_survey.get_bird_count(inputted_species)
        print(f"There is(are) {inputted_species_count} {inputted_species}(s).")

        print("\nBird Survey (Before Deletion): ")
        bird_survey.print_survey()
        deleted_species = input(
            "\nEnter the species name of the bird you want to omit: "
        )
        bird_survey.delete(deleted_species)
        print("\nBird Survey (After Deletion): ")
        bird_survey.print_survey()
    except ValueError:
        print("\nThe bird count must be a valid integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
