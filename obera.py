# src/obera.py
import sys
from obera.parser import parse_lines
from obera.interpreter import Interpreter

def run_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read()
    program = parse_lines(lines)
    vm = Interpreter()
    vm.run(program)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python obera.py <file.obr>")
    else:
        run_file(sys.argv[1])
