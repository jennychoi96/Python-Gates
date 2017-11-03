import types

def getLocalMethods(clss):
    # helper function for the test function below.
    # returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

class Gate(object):
    def __init__(self):
        self.inputVal = None
    def __str__(self):
        name = type(self).__name__ 
        if (type(self) == AndGate) or (type(self) == OrGate):
            return name[:-4] + "(%s,%s)" %(self.inputVal[0],self.inputVal[1])
        else: 
            return name[:-4] + "(%s)" %self.inputVal[0]
    def numberOfInputs(self):
        return 2
    def setInput(self, key, value):
        self.key = key
        if self.inputVal == None:
            self.inputVal = { key : value }
        else: 
            self.inputVal[key] = value

class AndGate(Gate):
    def getOutput(self):
        return self.inputVal[0] and  self.inputVal[1]

class OrGate(Gate):
    def getOutput(self):
        return self.inputVal[0] or self.inputVal[1]

class NotGate(Gate):
    def getOutput(self):
        return not self.inputVal[0]
    def numberOfInputs(self):
        return 1
        
def testGateClasses():
    print("Testing Gate Classes... ", end="")

    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    # print(and1.numberOfInputs())
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)

    assert(str(and1) == "And(True,False)")
    # print(and1.getOutput())
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    # print(and1.getOutput())
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False)
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

class ComplexNumber:
    def __init__(self, x=None, y=None):
        # self.zero = None
        if isinstance(x, ComplexNumber):
            self.x = x.realPart()
            self.y = x.imaginaryPart()
        else: 
            if x == None: self.x = 0
            else: self.x = x

            if y == None: self.y = 0
            else: self.y = y

    def __str__(self): 
        return "%d+%di" % (self.x, self.y)

    def getHashables(self):
        return (self.x, ) # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        if isinstance(other, ComplexNumber): return self.x == other.x
        elif isinstance(other, int): return self.x == other
        # elif isinstance(other, getZero()): return self == other
        else: return False

    def realPart(self):
        return self.x
    def imaginaryPart(self):
        return self.y

    zero = None
    @staticmethod
    def getZero():
        if ComplexNumber.zero == None: 
            ComplexNumber.zero = ComplexNumber()
        return ComplexNumber.zero

def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)
    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) 
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())

    print("Passed!")

def main():
    testGateClasses()
    testComplexNumberClass()


if (__name__ == '__main__'):
    main()