import os

FILES_DIR_PATH = "./files/"
"""The relative file path to the "files" directory."""


def determine_program_termination(file: str) -> str:
    """Determine whether to abort or continue the program.

    :param file: The name of the file to check.
    :return: The action to take: "abort", "rename", or "correct".
    """
    if not verify_file_existence_and_readability(file):
        print("\nThis file does not exist or is not readable.")
        print("Options:\n1) Abort Program\n2) Enter New File Name")

        choice = int(input("Choose an option: "))
        if choice == 1:
            return "abort"
        else:
            print()
            return "rename"

    return "correct"


def verify_file_existence_and_readability(file: str) -> bool:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    file_path = os.path.join(FILES_DIR_PATH, file)
    return os.path.exists(file_path) and os.access(file_path, os.R_OK)


def main() -> None:
    """Copy contents from one file to another."""
    try:
        # Original File
        while True:
            original_file = input(
                "Enter the name of the file you want to copy FROM: "
            )

            status = determine_program_termination(original_file)
            if status == "correct":
                break
            elif status == "abort":
                return
            elif status == "rename":
                continue

        # Copy File
        while True:
            copy_file = input(
                "\nEnter the name of the file you want to copy TO: "
            )

            if verify_file_existence_and_readability(copy_file):
                overwrite_str = input(
                    '\nThis file already exists. Do you wish to overwrite it '
                    '("yes" or "no")?: '
                )

                if overwrite_str.lower() != "yes":
                    continue
            break

        # Copies contents of the original file to the copy file
        with open(os.path.join(FILES_DIR_PATH, original_file), "r") as o_file:
            original_file_lines = o_file.readlines()

        with open(os.path.join(FILES_DIR_PATH, copy_file), "w") as c_file:
            for line in original_file_lines:
                c_file.write(f"{line.strip()}\n")

        print(
            f"\nThe contents of {original_file} have been successfully copied "
            f"over to {copy_file}."
        )
    except ValueError:
        print("\nThe input must be a valid integer! Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
