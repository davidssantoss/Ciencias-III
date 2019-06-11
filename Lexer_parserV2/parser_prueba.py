import lexer_rules
import parser_rules
import getFile

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
text = getFile.getFiles()
print(text[0])
ast = parser.parse(text[0], lexer)
print ast
