#primero dejamos que el usuario meta su mierda
codigo = input("Ingrese el código pai: ")
#tokenList = []
import Stuff

class Token:

    def __init__(self, value, name):
        self.value = value
        self.name = name
        
class TokenIdentifier:

    def __init__(self, tokenType, states, entries):
        self.entries = entries
        self.states = states
        self.tokenType = tokenType
        self.transitions = []
        for i in range(len(states)):
            self.transitions = self.transitions + [[]]
        self.currentState = self.states[0]

    def MakeTransitionMatrix(self):
        for i in range(len(self.states)):
            for j in range(len(self.entries)):
                self.transitions[i] = self.transitions[i] + [self.states[i].entries[self.entries[j]]] if self.entries[j] in self.states[i].entries.keys() else self.transitions[i] + [None]

    def EvaluateRegularExpression(self, re):
        self.currentState = self.states[0]
        self.MakeTransitionMatrix()
        for i in range(len(re)):
            if re[i] in self.entries and self.currentState is not None:
                row = self.states.index(self.currentState)
                column = self.entries.index(re[i])
                self.currentState = self.transitions[row][column]
            else:
                return False
        if self.currentState is None:
            return False
        return self.currentState.accept
    
class LexicalAnalizer:
    def __init__(self, code, tokenList):
        self.code = code
        self.tokenList = tokenList

    def AnalyzeCode(self):
        newCode = self.code.split(" ")
        i = 0
        while i < len(newCode):
            indexControl = i
            if((newCode[i][0] == '"' and newCode[i][-1] != '"') or (newCode[i][0] == "'" and newCode[i][-1] != "'")):
                indexControl = self.VerifyString(newCode, i)
                if indexControl == i:
                    print("Invalid Expression Here")
                    return
            hasToken = False
            for j in range(len(self.tokenList)):
                if self.tokenList[j].EvaluateRegularExpression(newCode[i]):
                    print(self.tokenList[j].tokenType)
                    j = len(self.tokenList)
                    hasToken = True
            if  not hasToken:
                print("Invalid Expression")
            i = indexControl
            i += 1
    
    def VerifyString(self, code, ind):
        beginSymbol = code[ind][0]
        lastIndex = ind
        for k in range(ind + 1, len(code)):
            code[ind] = code[ind] + code[k]
            if code[k][-1] == beginSymbol:
                lastIndex = k
                break
        return lastIndex
    

identify = TokenIdentifier("Identify", Stuff.states, Stuff.entry)
#print(identify.EvaluateRegularExpression(codigo))

reserved = TokenIdentifier("Reserved", Stuff.states_2 , Stuff.entry_2)
#print(reserved.EvaluateRegularExpression(codigo))

operators = TokenIdentifier("Operator", Stuff.states_3, Stuff.entry_3)
#print(operators.EvaluateRegularExpression(codigo))

ints = TokenIdentifier("Int", Stuff.states_4, Stuff.entry_4)

floats = TokenIdentifier("Float", Stuff.states_5, Stuff.entry_5)

strings = TokenIdentifier("String", Stuff.states_6, Stuff.entry_6)
                    
identifiers = [identify, reserved, operators, ints, floats, strings]
codeAnalyzer = LexicalAnalizer(codigo, identifiers)
codeAnalyzer.AnalyzeCode() 
    