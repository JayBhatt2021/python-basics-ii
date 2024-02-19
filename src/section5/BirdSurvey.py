class Bird:
    """A class representing a bird."""

    def __init__(self, species_name: str) -> None:
        """Initialize a bird.

        :param species_name: The name of the bird species.
        """
        self.species_name = species_name
        self.count = 1
        self.next = None


class BirdSurvey:
    """A class representing a bird survey."""

    def __init__(self) -> None:
        """Initialize the bird survey."""
        self.head = None
        self.length = 0

    def append(self, species_name: str) -> None:
        """Add a bird to the survey or increment its count if already present.

        :param species_name: The name of the bird species to add.
        """
        new_node = Bird(species_name)

        # Initializes the head if the linked list is empty
        if not self.head:
            self.head = new_node
            self.length += 1
            return

        previous, current = None, self.head
        while current:
            # Increments the count of the specified bird if it's already present
            if current.species_name == species_name:
                current.count += 1
                return

            previous = current
            current = current.next

        # Adds a new bird to the end of the linked list
        previous.next = new_node
        self.length += 1

    def delete(self, species_name: str) -> None:
        """Delete a bird species from the survey.

        :param species_name: The name of the bird species to delete.
        """
        # Exits immediately if the linked list is empty
        if self.length == 0:
            return

        # Moves the head to the next bird if the species to delete is the head
        if self.head.species_name == species_name:
            self.head = self.head.next
            self.length -= 1
            return

        previous, current = None, self.head
        while current:
            # Removes the current bird species if it is the one to delete
            if current.species_name == species_name:
                previous.next = current.next
                return

            # Updates the previous and current pointers
            previous = current
            current = current.next

    def get_bird_count(self, species_name: str) -> int:
        """Get the count of a specific bird species in the survey.

        :param species_name: The name of the bird species to get the count of.
        :return: The count of the specified bird species.
        """
        current = self.head
        while current:
            # Returns the count if the current bird matches the given species
            if current.species_name == species_name:
                return current.count

            current = current.next

        # Returns 0 if the given species is not found
        return 0

    def print_survey(self) -> None:
        """Print the bird survey."""
        current = self.head
        while current:
            print(f"Species: {current.species_name}, Count: {current.count}")
            current = current.next


def main() -> None:
    """Run the bird survey program."""
    try:
        bird_survey = BirdSurvey()

        # Handles BirdSurvey addition
        bird_total = int(
            input("How many birds do you want to input in the survey? ")
        )
        for i in range(1, bird_total + 1):
            species_name = input(f"Enter the species name of bird #{i}: ")
            bird_survey.append(species_name)

        # Handles BirdSurvey accession
        inputted_species = input(
            "\nEnter the species name of the bird you want to see the count of:"
            " "
        )
        inputted_species_count = bird_survey.get_bird_count(inputted_species)
        print(f"There are {inputted_species_count} {inputted_species}(s).")

        # Handles BirdSurvey printing and deletion
        print("\nBird Survey (Before Deletion):")
        bird_survey.print_survey()

        deleted_species = input(
            "\nEnter the species name of the bird(s) you want to omit: "
        )
        bird_survey.delete(deleted_species)

        print("\nBird Survey (After Deletion):")
        bird_survey.print_survey()
    except ValueError:
        print("\nThe bird count must be a valid integer. Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
