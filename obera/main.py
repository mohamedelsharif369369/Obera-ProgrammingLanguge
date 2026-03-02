# obera/main.py

import sys
from obera.lexer import Lexer
from obera.parser import Parser
from obera.interpreter import Interpreter


def run_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    # 1️⃣ Lexer
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # 2️⃣ Parser
    parser = Parser(tokens)
    ast = parser.parse()

    # 3️⃣ Interpreter
    interpreter = Interpreter()
    interpreter.visit(ast)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python -m obera.main <file.obr>")
        sys.exit(1)

    run_file(sys.argv[1])
