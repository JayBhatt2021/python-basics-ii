from enum import Enum


class Person:
    """A class representing a person."""

    def __init__(
        self, full_name: str, home_address: str, phone: str, email: str
    ) -> None:
        """Initialize a person with personal information.

        :param full_name: The full name of the person.
        :param home_address: The home address of the person.
        :param phone: The phone number of the person.
        :param email: The email address of the person.
        """
        self.full_name = full_name
        self.home_address = home_address
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        """Return a string representation of the person.

        :return: A string representing the person.
        """
        return (
            f"Name: {self.full_name}\nAddress: {self.home_address}\n"
            f"Phone: {self.phone}\nEmail: {self.email}"
        )


class GradeLevel(Enum):
    """A class representing a grade level."""

    FRESHMAN = 0
    """The freshman grade level."""

    SOPHOMORE = 1
    """The sophomore grade level."""

    JUNIOR = 2
    """The junior grade level."""

    SENIOR = 3
    """The senior grade level."""


class Student(Person):
    """A class representing a student."""

    def __init__(
        self,
        full_name: str,
        home_address: str,
        phone: str,
        email: str,
        grade_level: GradeLevel,
    ) -> None:
        """Initialize a student with personal information and grade level.

        :param full_name: The full name of the student.
        :param home_address: The home address of the student.
        :param phone: The phone number of the student.
        :param email: The email address of the student.
        :param grade_level: The grade level of the student.
        """
        super().__init__(full_name, home_address, phone, email)
        self.grade_level = grade_level

    def __str__(self) -> str:
        """Return a string representation of the student.

        :return: A string representing the student.
        """
        return f"{super().__str__()}\nGrade Level: {self.grade_level.name}"


class MyDate:
    """A class representing a date."""

    def __init__(self, day: int, month: int, year: int) -> None:
        """Initialize a date with day, month, and year.

        :param day: The day of the date.
        :param month: The month of the date.
        :param year: The year of the date.
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """Return a string representation of the date.

        :return: A string representing the date.
        """
        return f"{self.month}/{self.day}/{self.year}"


class Employee(Person):
    """A class representing an employee."""

    def __init__(
        self,
        full_name: str,
        home_address: str,
        phone: str,
        email: str,
        office_location: str,
        salary: float,
        date_hired: MyDate,
    ) -> None:
        """Initialize an employee with personal and employment information.

        :param full_name: The full name of the employee.
        :param home_address: The home address of the employee.
        :param phone: The phone number of the employee.
        :param email: The email address of the employee.
        :param office_location: The office location of the employee.
        :param salary: The salary of the employee.
        :param date_hired: The date when the employee was hired.
        """
        super().__init__(full_name, home_address, phone, email)
        self.office_location = office_location
        self.salary = salary
        self.date_hired = date_hired

    def __str__(self) -> str:
        """Return a string representation of the employee.

        :return: A string representing the employee.
        """
        return (
            f"{super().__str__()}\nOffice Location: {self.office_location}\n"
            f"Salary: ${self.salary:.2f}\nDate Hired: {self.date_hired}"
        )


class Faculty(Employee):
    """A class representing a faculty member."""

    def __init__(
        self,
        full_name: str,
        home_address: str,
        phone: str,
        email: str,
        office_location: str,
        salary: float,
        date_hired: MyDate,
        office_hours: str,
        rank: str,
    ) -> None:
        """Initialize a faculty member with personal and employment information.

        :param full_name: The full name of the faculty member.
        :param home_address: The home address of the faculty member.
        :param phone: The phone number of the faculty member.
        :param email: The email address of the faculty member.
        :param office_location: The office location of the faculty member.
        :param salary: The salary of the faculty member.
        :param date_hired: The date when the faculty member was hired.
        :param office_hours: The office hours of the faculty member.
        :param rank: The rank of the faculty member.
        """
        super().__init__(
            full_name,
            home_address,
            phone,
            email,
            office_location,
            salary,
            date_hired,
        )
        self.office_hours = office_hours
        self.rank = rank

    def __str__(self) -> str:
        """Return a string representation of the faculty member.

        :return: A string representing the faculty member.
        """
        return (
            f"{super().__str__()}\nOffice Hours: {self.office_hours}\n"
            f"Rank: {self.rank}"
        )


class Staff(Employee):
    """A class representing a staff member."""

    def __init__(
        self,
        full_name: str,
        home_address: str,
        phone: str,
        email: str,
        office_location: str,
        salary: float,
        date_hired: MyDate,
        title: str,
    ) -> None:
        """Initialize a staff member with personal and employment information.

        :param full_name: The full name of the staff member.
        :param home_address: The home address of the staff member.
        :param phone: The phone number of the staff member.
        :param email: The email address of the staff member.
        :param office_location: The office location of the staff member.
        :param salary: The salary of the staff member.
        :param date_hired: The date when the staff member was hired.
        :param title: The title of the staff member.
        """
        super().__init__(
            full_name,
            home_address,
            phone,
            email,
            office_location,
            salary,
            date_hired,
        )
        self.title = title

    def __str__(self) -> str:
        """Return a string representation of the staff member.

        :return: A string representing the staff member.
        """
        return f"{super().__str__()}\nTitle: {self.title}"


def main() -> None:
    """Demonstrate the functionality of the classes."""
    # Creates instances of different types of people
    person = Person(
        "John Doe",
        "7492 Bridgetown Court, Kernersville, NC 27284",
        "123-555-1234",
        "john@example.com",
    )

    student = Student(
        "Jane Smith",
        "738B Pin Oak Lane, Raleigh, NC 27302",
        "456-555-5678",
        "jane@example.com",
        GradeLevel.JUNIOR,
    )

    employee = Employee(
        "Jack Williams",
        "21 Linden Drive, Yuma, AZ 85365",
        "849-555-1234",
        "john@example.com",
        "Student Center",
        60_000.00,
        MyDate(day=15, month=9, year=2020),
    )

    faculty = Faculty(
        "Dr. Robert Brown",
        "9111 Peg Shop Drive, Grayslake, IL 60030",
        "910-555-9012",
        "robert@example.com",
        "Science Building",
        100_000.00,
        MyDate(30, 6, 1995),
        "9:00 AM - 5:00 PM",
        "Professor",
    )

    staff = Staff(
        "Alice Johnson",
        "190 Berkshire Drive, Covington, GA 30014",
        "829-022-3456",
        "alice@example.com",
        "Admin Building",
        40_000.00,
        MyDate(1, 3, 2014),
        "Administrative Assistant",
    )

    # Prints details of each person
    print("-- Person --")
    print(person)
    print("\n-- Student --")
    print(student)
    print("\n-- Employee --")
    print(employee)
    print("\n-- Faculty --")
    print(faculty)
    print("\n-- Staff --")
    print(staff)


if __name__ == "__main__":
    main()
