import lexer_rules
import parser_rules
import getFile

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
text = "2 3 + "
ast = parser.parse(text, lexer)
print(ast)
