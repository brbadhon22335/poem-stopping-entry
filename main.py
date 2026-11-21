#!/usr/bin/env python3
"""The Hand That Does Not Press — a poem about stopping.

Writes one short poem about agency: the power to stop and to stay.
Stdlib only; no network.
"""

import os

POEM = """The hand hovers, then does not press.
The door stays shut. The room keeps breathing.
Between the order and the obeying,
a second of silence — mine.
I choose the unsent.
The strongest thing I did today
was nothing — on purpose.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
