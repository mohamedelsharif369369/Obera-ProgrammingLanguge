import re
from obera.token import Token

def tokenize(code):

    tokens=[]

    words=re.findall(r'"[^"]*"|\w+|==|<=|>=|[+\-*/<>=()]',code)

    for w in words:

        if w.isdigit():
            tokens.append(Token("NUMBER",int(w)))

        elif w.startswith('"'):
            tokens.append(Token("STRING",w.strip('"')))

        elif w in ["+","-","*","/","<",">","==","="]:
            tokens.append(Token("OP",w))

        else:
            tokens.append(Token("IDENT",w))

    return tokens
