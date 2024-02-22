import re


class TimeFormatException(Exception):
    """Exception raised for invalid time format."""

    def __init__(self, message: str = "The time format is incorrect.") -> None:
        """Initialize an instance of TimeFormatException.

        :param message: The error message.
        """
        super().__init__(message)


def convert_time(original_time: str) -> str:
    """Convert time from 24-hour to 12-hour format.

    :param original_time: The time in 24-hour format (HH:MM).
    :return: The time converted to 12-hour format (HH:MM AM/PM).
    :raises TimeFormatException: If the time format is invalid.
    """
    validate_time_format(original_time)
    original_hours_str, original_minutes_str = original_time.split(":")
    original_hours, original_minutes = (
        int(original_hours_str),
        int(original_minutes_str),
    )

    converted_hours = convert_hours(original_hours)
    converted_minutes = convert_minutes(original_minutes)
    am_pm_str = determine_am_or_pm(original_hours)

    return f"{converted_hours}:{converted_minutes} {am_pm_str}"


def validate_time_format(original_time: str) -> None:
    """Validate the format of the 24-hour time string.

    :param original_time: The 24-hour time string to validate.
    :raises TimeFormatException: If the time format is invalid.
    """
    if not bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", original_time)):
        raise TimeFormatException(
            'The 24-hour time string must be in the format "HH:MM" and '
            'represent a valid time.'
        )


def convert_hours(hours: int) -> str:
    """Convert hours to 12-hour format.

    :param hours: The hours to convert.
    :return: The hours in 12-hour format.
    """
    if hours > 12:
        hours %= 12
    return f"{hours:02d}"


def convert_minutes(minutes: int) -> str:
    """Convert minutes to 12-hour format.

    :param minutes: The minutes to convert.
    :return: The minutes in 12-hour format.
    """
    return f"{minutes:02d}"


def determine_am_or_pm(hours: int) -> str:
    """Determine whether it's AM or PM.

    :param hours: The hours of the time.
    :return: "AM" if before noon, otherwise "PM".
    """
    return "AM" if hours < 12 else "PM"


def main() -> None:
    """Main function to convert time."""
    try:
        while True:
            original_time = input("Enter the time in 24-hour notation: ")

            try:
                converted_time = convert_time(original_time)
                print(
                    f"{original_time} is equivalent to {converted_time} in "
                    f"12-hour notation."
                )
            except TimeFormatException as tfe:
                print(tfe)

            choice = input(
                '\nDo you want to convert more 24-hour times ("yes" or "no")?: '
            )
            if choice.lower() != "yes":
                break
            print()

        print("\nThank you for using the TimeConverter program!")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
