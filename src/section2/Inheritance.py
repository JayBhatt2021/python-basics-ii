class Person:
    """An abstract class representing a Vacation."""

    def __init__(self, name: str, address: str, phone_number: str,
                 email_address: str) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return (
            f"(Person)\nName: {self.name}\nAddress: {self.address}\nPhone "
            f"Number: {self.phone_number}\nEmail Address: {self.email_address}"
        )


class Student(Person):
    """An abstract class representing a Vacation."""

    Freshman, Sophomore, Junior, Senior = range(4)

    def __init__(self, name: str, address: str, phone_number: str,
                 email_address: str, class_status: int) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        super().__init__(name, address, phone_number, email_address)
        self.class_status = class_status

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return (
            f"(Student)\nName: {self.name}\nAddress: {self.address}\nPhone "
            f"Number: {self.phone_number}\nEmail Address: {self.email_address}"
            f"\nClass Status: {self.class_status}"
        )


class MyDate:
    """An abstract class representing a Vacation."""

    def __init__(self, day: int, month: int, year: int) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return f"{self.month}/{self.day}/{self.year}"


class Employee(Person):
    """An abstract class representing a Vacation."""

    def __init__(self, name: str, address: str, phone_number: str,
                 email_address: str, office_location: str,
                 salary: float, date_hired: MyDate) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        super().__init__(name, address, phone_number, email_address)
        self.office_location = office_location
        self.salary = salary
        self.date_hired = date_hired

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return (
            f"(Employee)\nName: {self.name}\nAddress: {self.address}\nPhone "
            f"Number: {self.phone_number}\nEmail Address: {self.email_address}"
            f"\nOffice Location: {self.office_location}\nSalary: $"
            f"{self.salary:.2f}\nDate Hired: {self.date_hired}"
        )


class Faculty(Employee):
    """An abstract class representing a Vacation."""

    def __init__(self, name: str, address: str, phone_number: str,
                 email_address: str, office_location: str,
                 salary: float, date_hired: MyDate, office_hours: str,
                 rank: str) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        super().__init__(name, address, phone_number, email_address,
                         office_location, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return (
            f"(Faculty)\nName: {self.name}\nAddress: {self.address}\nPhone "
            f"Number: {self.phone_number}\nEmail Address: {self.email_address}"
            f"\nOffice Location: {self.office_location}\nSalary: $"
            f"{self.salary:.2f}\nDate Hired: {self.date_hired}\nOffice Hours: "
            f"{self.office_hours}\nRank: {self.rank}"
        )


class Staff(Employee):
    """An abstract class representing a Vacation."""

    def __init__(self, name: str, address: str, phone_number: str,
                 email_address: str, office_location: str,
                 salary: float, date_hired: MyDate, title: str) -> None:
        """Initialize a vacation with budget and destination.

        :param budget: The budget for the vacation.
        :param destination: The destination of the vacation.
        :return: None
        """
        super().__init__(name, address, phone_number, email_address,
                         office_location, salary, date_hired)
        self.title = title

    def __str__(self) -> str:
        """Return a string representation of the all-inclusive vacation.

        :return: A string representing the all-inclusive vacation.
        """
        return (
            f"(Faculty)\nName: {self.name}\nAddress: {self.address}\nPhone "
            f"Number: {self.phone_number}\nEmail Address: {self.email_address}"
            f"\nOffice Location: {self.office_location}\nSalary: $"
            f"{self.salary:.2f}\nDate Hired: {self.date_hired}\nTitle: "
            f"{self.title}"
        )


def main() -> None:
    """Generate two types of vacations, prompt for input, and display details.

    :return: None
    """
    # Person
    person = Person()
    print(person)

    # Student
    student = Student()
    print(student)

    # Employee
    employee = Employee()
    print(employee)

    # Faculty
    faculty = Faculty()
    print(faculty)

    # Staff
    staff = Staff()
    print(staff)


if __name__ == "__main__":
    main()
