from pathlib import Path

from itch import process_itch
from steam import process_steam

def main():

    print("==============================")
    print("      Review Converter")
    print("==============================")
    print()
    print("1 - Steam")
    print("2 - itch.io")
    print()

    choice = input(
        "Choose the source: "
    ).strip()


    if choice == "1":
        source = "Steam"

    elif choice == "2":
        source = "itch.io"

    else:
        print("Invalid choice.")
        return


    print()
    print(f"Selected: {source}")
    print()


    # ----------------------------------------------
    # Ask for directories
    # ----------------------------------------------

    input_path = input(
        "Input directory: "
    ).strip()

    output_path = input(
        "Output directory: "
    ).strip()


    input_dir = Path(input_path)
    output_dir = Path(output_path)


    # ----------------------------------------------
    # Validate input
    # ----------------------------------------------

    if not input_dir.exists():
        print(
            f"Input directory does not exist: "
            f"{input_dir}"
        )
        return


    # ----------------------------------------------
    # Process
    # ----------------------------------------------

    if choice == "1":
        process_steam(
            input_dir,
            output_dir
        )

    elif choice == "2":
        process_itch(
            input_dir,
            output_dir
        )


    print()
    print("Done!")


if __name__ == "__main__":
    main()