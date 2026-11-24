import sys


def clean_text(text):
    """Remove trailing whitespace and repeated blank lines."""
    lines = text.splitlines()

    cleaned_lines = []
    previous_empty = False

    for line in lines:
        line = line.rstrip()

        if line == "":
            if previous_empty:
                continue
            previous_empty = True
        else:
            previous_empty = False

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def main():
    text = sys.stdin.read()
    result = clean_text(text)
    print(result)


if __name__ == "__main__":
    main()

