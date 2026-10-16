import sys
from pathlib import Path

DB = Path("todo.txt")

def add(text):
    with DB.open("a") as f:
        f.write(text + "\n")

def done(number):
    lines = DB.read_text().splitlines()
    del lines[number - 1]
    DB.write_text("".join(f"{line}\n" for line in lines))

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
    elif command == "done":
        done(int(args[0]))