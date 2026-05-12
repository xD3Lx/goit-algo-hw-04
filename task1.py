import argparse
import shutil
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Copy files recursively and sort them by extension."
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the source directory.",
    )
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Path to the destination directory. Defaults to 'dist'.",
    )

    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    try:
        for elem in src.iterdir():
            if elem.is_dir():
                recursive_copy(elem, dst)
            else:
                extension = elem.suffix.lower()[1:]
                folder = dst / extension
                folder.mkdir(parents=True, exist_ok=True)
                destination = folder / elem.name
                print(f"Copying {elem} to {destination}")
                shutil.copy2(elem, destination)
    except (FileNotFoundError | PermissionError) as e:
        print(f"An error occurred: {e}")

def main():
    args = parse_arguments()
    source = args.source
    destination = args.destination
    print(f"Source directory: {source}")
    print(f"Destination directory: {args.destination}")

    if not source.exists():
        print(f"Error: The source directory ('{source}') does not exist.")
        return
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Failed to create destination directory: {e}")
        return
    recursive_copy(source, destination)
    print(f"Files copied to {destination}")

if __name__ == "__main__":
    main()
