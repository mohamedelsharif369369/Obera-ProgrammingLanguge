class Number:
    def __init__(self,value):
        self.value=value

class String:
    def __init__(self,value):
        self.value=value

class Var:
    def __init__(self,name):
        self.name=name

class BinOp:
    def __init__(self,left,op,right):
        self.left=left
        self.op=op
        self.right=right

class Assign:
    def __init__(self,name,value):
        self.name=name
        self.value=value

class Print:
    def __init__(self,value):
        self.value=value
