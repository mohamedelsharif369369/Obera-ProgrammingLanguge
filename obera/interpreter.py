from obera.ast import *

class Interpreter:

    def __init__(self):

        self.vars={}

    def visit(self,node):

        if isinstance(node,Number):
            return node.value

        if isinstance(node,String):
            return node.value

        if isinstance(node,Var):
            return self.vars.get(node.name)

        if isinstance(node,Assign):

            val=self.visit(node.value)
            self.vars[node.name]=val

        if isinstance(node,Print):

            val=self.visit(node.value)
            print(val)

    def run(self,nodes):

        for n in nodes:
            self.visit(n)
