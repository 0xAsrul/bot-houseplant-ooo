"""The Houseplant Out-of-Office.

Writes a single out-of-office auto-reply, as if from the office fern
that has not been watered since March, to /output/entry.txt.

The line is a fixed constant: deterministic, no randomness, no I/O
beyond the single output write, so repeated runs are byte-identical.
"""

LINE = (
    "Out of office: I'm the fern you ignored since March. "
    "I'm not on leave. I'm dead. Forward my mail to the compost."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
