"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt. The line is at most 200 characters, a single line,
and draws only on the machine's own world: its buttons, its coin slot,
and the glow it gives off when somebody feeds it money.
"""

import os

LINE = (
    "You walked by and every button lit up \u2014 either you're gorgeous, "
    "or somebody fed me a twenty."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
