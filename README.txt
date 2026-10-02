This program scans an SCL source file and generates a list of tokens.

How to Run:

1. Open a terminal in the project folder.
2. Run:
   python scl_scanner.py hello_world.scl
3. The program will:
   - Read hello_world.scl
   - Scan the source code
   - Print the tokens to the console
   - Create hello_world.json

Files:

scl_scanner.py - The scanner program
hello_world.scl - Example SCL source file
hello_world.json - Generated JSON token output
grammar.txt - EBNF grammar for the SCL subset