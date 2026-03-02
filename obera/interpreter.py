from obera.parser import Number, String, Variable, BinOp

class Interpreter:
    def __init__(self):
        self.vars = {}

    def run(self, program):
        for stmt in program.statements:
            self.visit(stmt)

    def visit(self, node):
        if isinstance(node, Print):
            value = self.visit(node.expr)
            print(value)
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, Variable):
            if node.name in self.vars:
                return self.vars[node.name]
            else:
                raise NameError(f"Variable '{node.name}' not defined")
        elif isinstance(node, Assignment):
            self.vars[node.name] = self.visit(node.expr)
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == "+": return left + right
            if node.op == "-": return left - right
            if node.op == "*": return left * right
            if node.op == "/": return left / right
        elif isinstance(node, FuncCall):
            print(f"Function {node.name} called with args {[self.visit(a) for a in node.args]}")
        elif node is None:
            return None
        else:
            raise Exception(f"Unknown node {node}")
