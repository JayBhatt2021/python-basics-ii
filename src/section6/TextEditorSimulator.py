import os

FILES_DIR_PATH = "./files/"
"""The relative file path to the "files" directory."""


class TextEditorSimulator:
    """A class representing a button simulator."""

    def __init__(self, file: str) -> None:
        """Initialize the button simulator."""
        self.file = file

    def simulate_text_editor(self) -> None:
        """Simulate pressing buttons."""
        self.display_file_contents()
        self.overwrite_file()
        print("\nThank you for using TextEditorSimulator!")

    def display_file_contents(self) -> None:
        """Simulate pressing buttons."""
        print(f'\nContents of "{self.file}":')
        with open(os.path.join(FILES_DIR_PATH, self.file), "r") as file:
            for line in file:
                print(line.strip())

    def overwrite_file(self) -> None:
        """Simulate pressing buttons."""
        choice = input(
            f'\nDo you want to overwrite the text in "{self.file}" ("yes" or '
            f'"no")?: '
        )
        if choice.lower() != "yes":
            return

        new_file_text = input(f'Enter the new text for "{self.file}": ')
        with open(os.path.join(FILES_DIR_PATH, self.file), "w") as file:
            file.write(new_file_text)

        print(f'\n"{self.file}" has been overwritten.')


def verify_file_existence_and_readability(file: str) -> bool:
    """Verify the existence and readability of a file.

    :param file: The name of the file to verify.
    :return: True if the file exists and is readable, False otherwise.
    """
    file_path = os.path.join(FILES_DIR_PATH, file)
    return os.path.exists(file_path) and os.access(file_path, os.R_OK)


def main() -> None:
    """Run the button simulator program."""
    try:
        while True:
            file = input("Enter the name of the file: ")
            if verify_file_existence_and_readability(file):
                break
            else:
                print(
                    f'\n"{file}" does not exist or is not readable. Please try '
                    f'again.'
                )

        text_editor_simulator = TextEditorSimulator(file)
        text_editor_simulator.simulate_text_editor()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f'\nAn unexpected error occurred: "{e}".')


if __name__ == "__main__":
    main()
