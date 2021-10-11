from inspect import stack


class AP:
    def __init__(self, entry_symbols, stack_symbols, init_config):
        self.entry_symbols = entry_symbols
        self.stack_symbols = stack_symbols
        self.init_stack = init_config
        self.stack = init_config
        self.grammar = []
        self.current_entry = ''

    def UnstackThenNext(self):
        self.stack = self.stack[:-1]
        self.grammar = self.grammar[1:]
        self.current_entry = self.grammar[0]

    def UnstackThenHold(self):
        self.stack = self.stack[:-1]

    def ReplaceThenNext(self, symbols):
        self.stack = self.stack[:-1] + symbols[1:]
        self.grammar = self.grammar[1:]
        self.current_entry = self.grammar[0]

    def ReplaceThenHold(self, symbols):
        self.stack = self.stack[:-1] + symbols

    def Analize(self):
        i = 0
        while len(self.grammar):
            if(self.current_entry.value in self.stack[-1].relations.keys()):
                if(self.stack[-1].relations[self.current_entry.value] == "Unstack Next"):
                    self.UnstackThenNext()
                elif(self.stack[-1].relations[self.current_entry.value] == "Unstack Hold"):
                    self.UnstackThenHold()
                elif(self.stack[-1].relations[self.current_entry.value] == "Accept"):
                    return True
                elif("a" in self.stack[-1].relations[self.current_entry.value]):
                    self.ReplaceThenNext(self.stack[-1].relations[self.current_entry.value])
                else:
                    self.ReplaceThenHold(self.stack[-1].relations[self.current_entry.value])
            elif(self.current_entry.name in self.stack[-1].relations.keys()):
                if(self.stack[-1].relations[self.current_entry.name] == "Unstack Next"):
                    self.UnstackThenNext()
                elif(self.stack[-1].relations[self.current_entry.name] == "Unstack Hold"):
                    self.UnstackThenHold()
                elif(self.stack[-1].relations[self.current_entry.name] == "Accept"):
                    return True
                elif("a" in self.stack[-1].relations[self.current_entry.name]):
                    self.ReplaceThenNext(self.stack[-1].relations[self.current_entry.name])
                else:
                    self.ReplaceThenHold(self.stack[-1].relations[self.current_entry.name])
            else:
                return False
        i += 1
        print(i)