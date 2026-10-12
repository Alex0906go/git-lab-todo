import sys
from pathlib import Path

DB = Path("todo.txt")


def add(text):
    with DB.open("a") as f:
        f.write(text + "\n")


def show():
    if not DB.exists():
        return
    for i, line in enumerate(DB.read_text().splitlines(), 1):
        print(f"{i}. {line}")


if __name__ == "__main__":
    command, *args = sys.argv[1:] or ["list"]

    if command == "add":
        add(" ".join(args))
    elif command == "list":
        show()