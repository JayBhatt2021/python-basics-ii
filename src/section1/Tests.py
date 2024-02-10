class Student:
    """A simple counter for tracking occurrences."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialize the counter.

        :return: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.test_scores = []

    def __str__(self) -> str:
        """Initialize the counter.

        :return: None
        """
        average_score = self.calculate_average_score()
        properties = [self.first_name, self.last_name,
                      f"{self.test_scores[0]:.2f}",
                      f"{self.test_scores[1]:.2f}",
                      f"{self.test_scores[2]:.2f}",
                      f"{self.test_scores[3]:.2f}",
                      f"{self.test_scores[4]:.2f}",
                      f"{average_score:.2f}",
                      self.calculate_grade(average_score)]
        return "\t".join(map(str, properties))

    def add_test_score(self, test_score: float) -> None:
        """Increment the counter.

        :return: None
        """
        if len(self.test_scores) + 1 < 6:
            self.test_scores.append(test_score)

    def calculate_average_score(self) -> float:
        """Increment the counter.

        :return: None
        """
        test_count = len(self.test_scores)
        return 0.0 if not test_count else sum(self.test_scores) / test_count

    def calculate_grade(self, average_score: float) -> str:
        """Increment the counter.

        :return: None
        """
        grade = "F"

        if average_score >= 90:
            grade = "A"
        elif average_score >= 80:
            grade = "B"
        elif average_score >= 70:
            grade = "C"
        elif average_score >= 60:
            grade = "D"

        return grade


def main() -> None:
    """Simulate 100 coin flips and count the number of heads and tails."""
    #
    first_names = ["Jack", "Lisa", "Andy", "Ravi", "Bonny", "Danny", "Sam",
                   "Robin", "Sun", "Kiran"]
    last_names = ["Johnson", "Aniston", "Cooper", "Gupta", "Blair", "Clark",
                  "Kennedy", "Bronson", "Xie", "Patel"]
    test_one_scores = [85, 80, 78, 92, 23, 60, 77, 93, 79, 85]
    test_two_scores = [83, 90, 81, 83, 45, 85, 31, 94, 85, 72]
    test_three_scores = [77, 95, 11, 30, 96, 45, 52, 89, 28, 49]
    test_four_scores = [91, 93, 90, 69, 38, 39, 74, 77, 93, 75]
    test_five_scores = [76, 48, 73, 87, 59, 67, 83, 97, 82, 63]

    #
    headings = ["F.N.", "L.N.", "Test1", "Test2", "Test3", "Test4", "Test5",
                "Average", "Grade"]
    print("\t".join(headings))

    #
    for i in range(len(first_names)):
        student = Student(first_names[i], last_names[i])
        student.add_test_score(test_one_scores[i])
        student.add_test_score(test_two_scores[i])
        student.add_test_score(test_three_scores[i])
        student.add_test_score(test_four_scores[i])
        student.add_test_score(test_five_scores[i])
        print(student)


if __name__ == "__main__":
    main()
