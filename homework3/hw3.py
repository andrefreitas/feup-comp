from lexer import Lexer
from rdp_parser import Parser
tokens={
        "INT":"[0-9]+",
        "ADD":"\+",
        "SUB":"-",
        "MUL":"\*",
        "DIV":"/"
        }

language=[("Start","Expr"),
          ("Expr","Term","ExprP"),
          ("ExprP","ADD","Term","ExprP"),
          ("ExprP","SUB","Term","ExprP"),
          ("ExprP",""),
          ("Term","INT","TermP"),
          ("TermP","MUL","INT","TermP"),
          ("TermP","DIV","INT","TermP"),
          ("TermP","")
          ]

l=Lexer(tokens)
p=Parser(tokens,language)

while(True):
    string=raw_input("> ")
    tokens_stream=l.scan(string)
    if(p.accept(tokens_stream)):
        print "Accepted"
    else:
        print "Rejected"
