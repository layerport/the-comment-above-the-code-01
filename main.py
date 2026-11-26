"""Write the competition entry: one funny, painfully honest comment
a developer would leave above fragile production code."""

import os

ENTRY = "// TODO(2019): delete this after the migration. The migration finished in 2021. This IS the database now."


def main():
    # The gate only accepts 1-200 characters, so fail loudly here
    # rather than shipping a line the scorer would reject.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
