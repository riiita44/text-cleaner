import sys
import argparse


def clean_text(text):
    """行末空欄と連続する空行を削除する"""
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
    parser = argparse.ArgumentParser(
        description="テキストの空白や重複行を整理するコマンド"
    )

    parser.add_argument(
        "-r", "--remove-duplicates",
        action="store_true",
        help="重複した行を削除する"
    )

    parser.add_argument(
        "-e", "--remove-empty",
        action="store_true",
        help="空行をすべて削除する"
    )

    args = parser.parse_args()

    text = sys.stdin.read()
    result = clean_text(text)

    if args.remove_duplicates:
        lines = result.splitlines()
        result = "\n".join(dict.fromkeys(lines))

    if args.remove_empty:
        lines = result.splitlines()
        result = "\n".join(line for line in lines if line != "")

    print(result)



if __name__ == "__main__":
    main()

