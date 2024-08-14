# JSON Parser script
import sys


class JSONParser:

    def __init__(self, text):
        self.i = 0
        self.text = text

    def parse(self):
        self.text = self.text.strip()
        return self.process_object()

    def current_char(self):
        if self.i < len(self.text):
            return self.text[self.i]
        return ""

    def process_object(self):
        obj = {}
        if self.text[self.i] != "{":
            raise ValueError("JSONObject Missing {")
            return None
        self.i += 1

        while True:
            self.skip_whitespace()

            if self.current_char() == "}":
                self.i += 1
                return obj

            key = self.process_string()
            self.skip_whitespace()

            if self.current_char() != ":":
                raise ValueError("Expected : after key")
            
            self.skip_whitespace()
            value = self.process_value()

    def skip_whitespace(self):
        while self.i < len(self.text) and self.current_char().isspace():
            self.i += 1

    def process_string(self):
        if self.current_char() != "\"":
            raise ValueError("String missing \"")
        self.i += 1
        start = self.i
        while self.current_char() != '"':
            if self.current_char() == '\\':
                self.i += 2
            else:
                self.i += 1
        end = self.i
        self.i += 1  # Skip closing quote
        return self.text[start:end]

    def process_value(self):
        if self.current_char() == "{":
            return self.process_object()
        if self.current_char() == "[":
            return self.process_array()
        if self.current_char().isdigit():
            return self.process_number()

    def process_array(self):
        arr = []
        self.i += 1

        while True:
            self.skip_whitespace()

            if self.current_char() == "]":
                self.i += 1
                return arr

            value = self.process_value()
            arr.append(value)
            self.skip_whitespace()

            if self.current_char() == ",":
                self.i += 1
            elif self.current_char() != ']':
                raise ValueError("Expected ',' or ']' in array")

    def process_number(self):
        start = self.i
        while self.current_char().isdigit():
            self.skip_whitespace()
            if not self.current_char().isdigit():
                raise ValueError("Digit not properly formatted")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: parse [filename].json")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            json_text = file.read()
            try:
                parser = JSONParser(json_text)
                parsed_json = parser.parse()
                print("Success!\n")
                print(parsed_json)
                sys.exit(0)
            except Exception as e:
                print("Fail!\n")
                print(e)
                sys.exit(1)
    except FileNotFoundError:
        print(f"parse: {sys.argv[1]}: No such file or directory")
        sys.exit(1)
