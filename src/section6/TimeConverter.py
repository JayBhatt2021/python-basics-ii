class TimeFormatException(Exception):
    """Replace this."""

    def __init__(self, message: str = "The time format is incorrect.") -> None:
        super().__init__(message)


def convert_time(original_time: str) -> str:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    if len(original_time) != 5:
        raise TimeFormatException(
            "The length of the time string must be five characters long!"
        )

    if ":" not in original_time:
        raise TimeFormatException(
            'The time string must follow the following format: "HH:MM".'
        )

    original_hours_str, original_minutes_str = original_time.split(":")
    original_hours, original_minutes = (
        int(original_hours_str),
        int(original_minutes_str),
    )

    if original_hours < 0 or original_hours > 23:
        raise TimeFormatException(
            "The hours in the time string must be between 0 and 23, inclusive."
        )

    if original_minutes < 0 or original_minutes > 59:
        raise TimeFormatException(
            "The minutes in the time string must be between 0 and 59, "
            "inclusive."
        )

    converted_hours = convert_hours(original_hours)
    converted_minutes = convert_minutes(original_minutes)
    am_pm_str = determine_am_or_pm(original_hours)

    return f"{converted_hours}:{converted_minutes} {am_pm_str}"


def convert_hours(hours: int) -> str:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    if hours > 12:
        hours %= 12

    if hours < 10:
        return f"0{hours}"

    return f"{hours}"


def convert_minutes(minutes: int) -> str:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    if minutes < 10:
        return f"0{minutes}"

    return f"{minutes}"


def determine_am_or_pm(hours: int) -> str:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    if hours // 12 == 0:
        return "AM"

    return "PM"


def main() -> None:
    """Copy contents from one file to another."""
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
            if choice.lower() == "no":
                break

        print("\nThank you for using the TimeConverter program!")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
