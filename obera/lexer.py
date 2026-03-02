import re

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    KEYWORDS = {"print", "func", "class", "import", "from"}
    OPERATORS = {"+", "-", "*", "/", "=", "==", ">", "<", ">=", "<="}

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        lines = self.code.split("\n")
        for line in lines:
            line = line.split("#")[0].strip()
            if not line:
                continue
            parts = line.split()
            for p in parts:
                if p.isdigit():
                    self.tokens.append(Token("NUMBER", int(p)))
                elif p in self.KEYWORDS:
                    self.tokens.append(Token("KEYWORD", p))
                elif p in self.OPERATORS:
                    self.tokens.append(Token("OPERATOR", p))
                elif p.startswith('"') and p.endswith('"'):
                    self.tokens.append(Token("STRING", p.strip('"')))
                else:
                    self.tokens.append(Token("IDENTIFIER", p))
        return self.tokens
