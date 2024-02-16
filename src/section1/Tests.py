from typing import List


class Student:
    """A class representing a student with test scores."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialize a student with first and last name.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.test_scores = []

    def __str__(self) -> str:
        """Return string representation of the student.

        :return: A formatted string representing the student's data.
        """
        average_score = self.calculate_average_score()
        return (
            f"{self.first_name}\t{self.last_name}\t"
            + "\t".join(f"{score:.2f}" for score in self.test_scores)
            + f"\t{average_score:.2f}\t{self.calculate_grade(average_score)}"
        )

    def add_test_score(self, test_score: float) -> None:
        """Add a test score to the list of test scores.

        :param test_score: The test score to add.
        """
        if len(self.test_scores) < 5:
            self.test_scores.append(test_score)

    def calculate_average_score(self) -> float:
        """Calculate the average test score of the student.

        :return: The average test score.
        """
        return (
            sum(self.test_scores) / len(self.test_scores) if self.test_scores
            else 0.0
        )

    @staticmethod
    def calculate_grade(average_score: float) -> str:
        """Calculate the grade based on the average test score.

        :param average_score: The average test score of the student.
        :return: The grade corresponding to the average test score.
        """
        if average_score >= 90:
            return "A"
        elif average_score >= 80:
            return "B"
        elif average_score >= 70:
            return "C"
        elif average_score >= 60:
            return "D"
        else:
            return "F"


def print_student_table(students: List[Student]) -> None:
    """Print a table of student names, test scores, average, and grade.

    :param students: A list of Student objects.
    """
    headings = [
        "F.N.",
        "L.N.",
        "Test1",
        "Test2",
        "Test3",
        "Test4",
        "Test5",
        "Average",
        "Grade",
    ]
    print("\t".join(headings))

    for student in students:
        print(student)


def main() -> None:
    """Prompt user to enter student data and print it in a formatted table."""
    try:
        students = []

        while True:
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            student = Student(first_name, last_name)

            print(F"\nEnter the test scores of {first_name} {last_name}.")
            for i in range(1, 6):
                test_score = float(input(f"Test score #{i}: "))
                student.add_test_score(test_score)

            students.append(student)

            continue_loop = input(
                "\nDo you want to stop adding students (enter 'yes' or 'no')?: "
            )
            if continue_loop.lower() == "yes":
                break
            print()

        print()
        print_student_table(students)
    except ValueError:
        print("\nThe test score must be a float! Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
