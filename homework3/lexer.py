import re

class TokenError:
    pass

class Lexer:
    def __init__(self,tokens):
        self.tokens=tokens
        
    def scan(self,string):
        seq=[]
        while(string):
            if(string[0]==" "):
                string=string[1:]
            else:
                tokens=self.tokens.keys()
                found=False
                for token in tokens:
                    if(re.match(self.tokens[token],string)):
                        m=re.match(self.tokens[token],string).group(0)
                        seq.append((token,m))
                        string=string.partition(m)[2]
                        found=True
                        break
                if(not found):
                    raise TokenError
        return seq