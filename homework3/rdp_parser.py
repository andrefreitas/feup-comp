class Parser:
    def __init__(self, tokens,grammar):
        self.grammar=grammar
        self.tokens=tokens
        
    def accept(self,token_stream):
        print token_stream
        self.token=0
        self.token_stream=token_stream
        starting_production=self.grammar[0][0]
        rdp=self.rdp(starting_production) and self.token_end()
        return rdp
        
    def is_terminal(self,production):
        return production in self.tokens
    
    def token_end(self):
        return self.token==len(self.token_stream)
    
    def expand_production(self,production):
        productions=[]
        for p in self.grammar:
            if(p[0]==production): productions.append(p[1:])
        return productions
    
    def rdp(self,production):
        # Is Empty
        if(production==""):
            return True
        # Is terminal
        if(not self.token_end() and self.is_terminal(production) and self.token_stream[self.token][0]==production):
            self.token+=1
            return True
        # Is non-terminal
        child_productions=self.expand_production(production)
        for child in child_productions:
            accept=True
            old_token=self.token
            for p in child:
                if(not self.rdp(p)):
                    accept=False
                    break
            if(accept): 
                return True
            else:
                self.token=old_token
        return False    