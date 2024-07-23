# JSON Parser script
import sys


def is_JSONString(token):
    return token.startswith("\"") and token.endswith("\"")


def is_JSONBoolean(token):
    return token == "true" or token == "false"


def is_JSONNull(token):
    return token == "null"


def json_parse(text):
    if not (text.startswith("{") and text.endswith("}")):
        print("Error JSON Invalid : { or } missing")
        sys.exit(1)
    # Tokenize key-value pairs
    text = text[1:len(text)-1]
    tokens = text.split(",")
    for t in tokens:
        key_value = t.strip().split(": ")

        if len(key_value) != 2 or not is_JSONString(key_value[0]):
            print("Error JSON Invalid : \"key\": value format violated")
            sys.exit(1)
        # Checks for string
        if key_value[1].startswith("\""):
            if not is_JSONString(key_value[1]):
                print(f"Error JSON Invalid : \" {key_value[1]} \" improperly formatted")
                sys.exit(1)
            continue
        # Checks for a numeric
        if key_value[1][0].isnumeric():
            if not key_value[1].isnumeric():
                print(f"Error JSON Invalid : {key_value[1]} is not numeric")
            continue
        # Checks for boolean or null
        if not (is_JSONBoolean(key_value[1]) or is_JSONNull(key_value[1])):
            print(f"Error JSON Invalid : \" {key_value[1]} \" improperly formatted")
            sys.exit(1)

    print("Success!")
    sys.exit(0)




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: parse [filename].json")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            json_text = file.read()
            json_parse(json_text.strip())
    except FileNotFoundError:
        print(f"parse: {sys.argv[1]}: No such file or directory")
        sys.exit(1)



