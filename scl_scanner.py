import sys
import json

# Keywords
KEYWORDS = [
    "int",
    "print",
    "if",
    "else",
    "while"
]

# Identifiers found in the source program
IDENTIFIERS = []

# Operators
OPERATORS = {
    "=": "ASSIGN",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
    "<": "LESS_THAN",
    ">": "GREATER_THAN",
    "==": "EQUAL",
    "!=": "NOT_EQUAL",
    "<=": "LESS_EQUAL",
    ">=": "GREATER_EQUAL"
}

# Special characters
SPECIAL_CHARACTERS = {
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    ";": "SEMICOLON",
    ",": "COMMA"
}


def scan(source_code):
    tokens = []
    IDENTIFIERS.clear()

    i = 0

    while i < len(source_code):
        current = source_code[i]

        # Ignore whitespace
        if current.isspace():
            i += 1
            continue

        # Ignore comments
        if current == "/" and i + 1 < len(source_code):
            if source_code[i + 1] == "/":
                i += 2

                while i < len(source_code) and source_code[i] != "\n":
                    i += 1

                continue

        # Identifiers and keywords
        if current.isalpha() or current == "_":
            start = i

            while (
                i < len(source_code)
                and (
                    source_code[i].isalnum()
                    or source_code[i] == "_"
                )
            ):
                i += 1

            value = source_code[start:i]

            if value in KEYWORDS:
                tokens.append({
                    "type": "KEYWORD",
                    "value": value
                })
            else:
                tokens.append({
                    "type": "IDENTIFIER",
                    "value": value
                })

                if value not in IDENTIFIERS:
                    IDENTIFIERS.append(value)

            continue

        # Integer constants
        if current.isdigit():
            start = i

            while i < len(source_code) and source_code[i].isdigit():
                i += 1

            value = source_code[start:i]

            tokens.append({
                "type": "INTEGER",
                "value": value
            })

            continue

        # Two-character operators
        if i + 1 < len(source_code):
            two_character_operator = source_code[i:i + 2]

            if two_character_operator in OPERATORS:
                tokens.append({
                    "type": OPERATORS[two_character_operator],
                    "value": two_character_operator
                })

                i += 2
                continue

        # One-character operators
        if current in OPERATORS:
            tokens.append({
                "type": OPERATORS[current],
                "value": current
            })

            i += 1
            continue

        # Special characters
        if current in SPECIAL_CHARACTERS:
            tokens.append({
                "type": SPECIAL_CHARACTERS[current],
                "value": current
            })

            i += 1
            continue

        # Unknown character
        tokens.append({
            "type": "UNKNOWN",
            "value": current
        })

        i += 1

    return tokens


def main():
    if len(sys.argv) != 2:
        print("Usage: python scl_scanner.py <source_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            source_code = file.read()

    except FileNotFoundError:
        print("Error: File '" + filename + "' was not found.")
        sys.exit(1)

    tokens = scan(source_code)

    print("Tokens:")
    print("----------------------------------------")

    for token in tokens:
        print(
            "{:<15} {}".format(
                token["type"],
                token["value"]
            )
        )

    print("----------------------------------------")
    print("Identifiers:")

    for identifier in IDENTIFIERS:
        print(identifier)

    if "." in filename:
        json_filename = filename.rsplit(".", 1)[0] + ".json"
    else:
        json_filename = filename + ".json"

    with open(json_filename, "w") as json_file:
        json.dump(tokens, json_file, indent=4)

    print("----------------------------------------")
    print("JSON output written to: " + json_filename)


if __name__ == "__main__":
    main()