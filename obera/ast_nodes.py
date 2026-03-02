# obera/ast_nodes.py

# ===== Base Node =====

class Node:
    pass


# ===== Program =====

class Program(Node):
    def __init__(self, statements):
        self.statements = statements


# ===== Statements =====

class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Print(Node):
    def __init__(self, expression):
        self.expression = expression


class If(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


# ===== Expressions =====

class Number(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinOp(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Compare(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
