# JSON Parser script
import sys


def json_parse(text):
    if len(text) == 2 and text.startswith("{") and text.endswith("}"):
        print("Success!")
        sys.exit(0)
    else:
        print("Error: JSON Invalid { or } missing")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: parse [filename].json")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            json_text = file.read()
            json_parse(json_text)
    except FileNotFoundError:
        print(f"parse: {sys.argv[1]}: No such file or directory")
        sys.exit(1)



