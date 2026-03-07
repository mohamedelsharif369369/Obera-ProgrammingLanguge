from obera.lexer import tokenize
from obera.ast import *

def parse(code):

    tokens=tokenize(code)

    i=0
    nodes=[]

    while i<len(tokens):

        t=tokens[i]

        if t.value=="print":

            val=tokens[i+1]

            if val.type=="NUMBER":
                nodes.append(Print(Number(val.value)))

            elif val.type=="STRING":
                nodes.append(Print(String(val.value)))

            elif val.type=="IDENT":
                nodes.append(Print(Var(val.value)))

            i+=2
            continue

        if t.type=="IDENT" and tokens[i+1].value=="=":

            name=t.value
            val=tokens[i+2]

            if val.type=="NUMBER":
                nodes.append(Assign(name,Number(val.value)))

            elif val.type=="STRING":
                nodes.append(Assign(name,String(val.value)))

            i+=3
            continue

        i+=1

    return nodes
