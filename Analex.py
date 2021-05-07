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
        self.MakeTransitionMatrix()

    def MakeTransitionMatrix(self):
        for i in range(len(self.states)):
            for j in range(len(self.entries)):
                self.transitions[i] = self.transitions[i] + [self.states[i].entries[self.entries[j]]] if self.entries[j] in self.states[i].entries.keys() else self.transitions[i] + [None]

    def EvaluateRegularExpression(self, re):
        self.currentState = self.states[0]
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

identify = TokenIdentifier("Identify", Stuff.states_1, Stuff.entry_1)

reserved = TokenIdentifier("Reserved", Stuff.states_2 , Stuff.entry_2)

operators = TokenIdentifier("Operator", Stuff.states_3, Stuff.entry_3)

ints = TokenIdentifier("Int", Stuff.states_4, Stuff.entry_4)

floats = TokenIdentifier("Float", Stuff.states_5, Stuff.entry_5)

strings = TokenIdentifier("String", Stuff.states_6, Stuff.entry_6)

separators = TokenIdentifier("Separator", Stuff.states_7, Stuff.entrry_7)

identifiers = [reserved, identify, operators, ints, floats, strings, separators]
    
class LexicalAnalizer:
    def __init__(self, finiteAutomates = identifiers):
        self.finiteAutomates = finiteAutomates
        self.tokenList = []

    def AnalyzeCode(self, code):
        multiCode = self.SplitCode(code.split("\n"))
        newCode = " "
        newCode = newCode.join(multiCode)
        newCode = newCode.split(" ")
        noneString = ""
        newCode = list(filter(lambda val: val != noneString, newCode))
        i = 0
        while i < len(newCode):
            indexControl = i
            if((newCode[i][0] == '"' and newCode[i][-1] != '"') or (newCode[i][0] == "'" and newCode[i][-1] != "'")):
                indexControl = self.VerifyString(newCode, i)
                if indexControl == i:
                    print("Invalid Expression")
                    return
            hasToken = False
            for j in range(len(self.finiteAutomates)):
                if self.finiteAutomates[j].EvaluateRegularExpression(newCode[i]):
                    self.tokenList = self.tokenList + [Token(newCode[i], self.finiteAutomates[j].tokenType)]
                    hasToken = True
                    break
            if  not hasToken:
                self.tokenList = self.tokenList + [Token(newCode[i], "Invalid Expression")] 
            i = indexControl
            i += 1
        return self.tokenList
    
    def VerifyString(self, code, ind):
        beginSymbol = code[ind][0]
        lastIndex = ind
        for k in range(ind + 1, len(code)):
            code[ind] = code[ind] + code[k]
            if code[k][-1] == beginSymbol:
                lastIndex = k
                break
        return lastIndex
    
    def SplitCode(self, code):
        seps = ["(", ")", "{", "}", ";"]
        newCode = []
        hasOp = False
        open = False
        i = 0
        while i < len(code):
            j = 0
            while j < len(code[i]):
                if(code[i][j] != "'" and code[i][j] != '"' and not open):
                    if(code[i][j] in seps):
                        hasOp = True
                        newCode = newCode + [code[i][0:j]] + [code[i][j]] if j != 0 else newCode + [code[i][0]]
                        code[i] = code[i][j+1:]
                        j = -1
                elif((code[i][j] == "'" or code[i][j] == '"') and not open):
                    open = True
                elif((code[i][j] == "'" or code[i][j] == '"') and open):
                    open = False
                j += 1
            newCode = newCode + [code[i]] if len(code[i]) > 0 else newCode
            i += 1
        return newCode

    def GetTokensValue(self):
        a=[]
        for i in self.tokenList:
            a = a + [i.value + ": " + i.name]
        return a
    