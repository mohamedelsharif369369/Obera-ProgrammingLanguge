import sys

from obera.parser import parse
from obera.interpreter import Interpreter


def run_file(file):

    with open(file) as f:
        code=f.read()

    ast=parse(code)

    vm=Interpreter()

    vm.run(ast)


if __name__=="__main__":

    run_file(sys.argv[1])
