# src/obera/parser.py
from obera.lexer import Lexer, Token

# ===== AST Nodes =====
class Number:
    def __init__(self, value): self.value = value
class String:
    def __init__(self, value): self.value = value
class Variable:
    def __init__(self, name): self.name = name
class BinOp:
    def __init__(self, left, op, right): self.left = left; self.op = op; self.right = right

# ===== Parser =====
def parse_expression(tokens):
    if len(tokens) == 1:
        t = tokens[0]
        if t.type == "NUMBER": return Number(t.value)
        if t.type == "STRING": return String(t.value)
        if t.type == "IDENTIFIER": return Variable(t.value)
    left = parse_expression([tokens[0]])
    i = 1
    while i < len(tokens):
        op = tokens[i].value
        right = parse_expression([tokens[i+1]])
        left = BinOp(left, op, right)
        i += 2
    return left

def parse_line(tokens):
    if not tokens: return None
    tokens = [t for t in tokens if t.type != "NEWLINE"]
    if not tokens: return None
    return parse_expression(tokens)

# ✅ هذه هي الدالة التي يجب استيرادها في obera.py
def parse_lines(code):
    lexer = Lexer(code)
    toks = lexer.tokenize()
    lines = []
    current = []
    for t in toks:
        if t.type == "NEWLINE":
            node = parse_line(current)
            if node: lines.append(node)
            current = []
        else:
            current.append(t)
    if current:
        node = parse_line(current)
        if node: lines.append(node)
    return lines
