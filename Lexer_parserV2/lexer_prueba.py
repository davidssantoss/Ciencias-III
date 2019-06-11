import lexer_rules
from ply.lex import lex
import getFile
text = getFile.getFiles()
for x in text:
    lexer = lex(module=lexer_rules)
    lexer.input(x)
    token = lexer.token()
    while token is not None:
        print token.type, token.value
        token = lexer.token()
