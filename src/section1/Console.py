def main() -> None:
    """Prompt user for name and age, then print the input."""
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        print(f"\nName: {name}\nAge: {age}")
    except ValueError:
        print("\nAge must be an integer! Exiting program...")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")


if __name__ == "__main__":
    main()
