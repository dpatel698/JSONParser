
# JSONParser

This project is a simple JSON parser implemented in Python. It demonstrates fundamental parsing techniques, including lexical and syntactic analysis, to read and interpret JSON data. This project was a great way to understand parsing concepts that are applicable to various data formats and even compiler design.

## Key Concepts

- **Lexical Analysis**: Breaking down a sequence of characters into tokens.
- **Syntactic Analysis**: Analyzing tokens to match them against a formal grammar.

## Features

- Parses JSON objects and arrays.
- Supports string, numeric, boolean, and null values.
- Provides error handling for malformed JSON inputs.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dpatel698/JSONParser.git
   cd JSONParser
   ```

# Usage
To parse a JSON file, run the following command:

```bash
python json_parser.py [filename].json
```

The program will output "Success!" and the parsed JSON object if the input is valid.
It will output "Fail!" and an error message if the input is invalid.

# Example
Given a JSON file example.json:

```json
{
  "name": "John",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Science"],
  "address": {
    "city": "New York",
    "zip": "10001"
  }
}
```

Run the parser:
```bash
python json_parser.py example.json
```

Expected output:
```text
Success!

{'name': 'John', 'age': 30, 'isStudent': False, 'courses': ['Math', 'Science'], 'address': {'city': 'New York', 'zip': '10001'}}

```

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
