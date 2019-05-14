import ply.lex as lex
import re

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
def getFile():
    archivo = open("./expresiones_in.txt", 'r')
    print("las expresiones del archivo son: \n")
    
    for linea in archivo.readlines():               
        x = re.split("\s", linea)            
    return x

def validarExpresion():
    exp = getFile()
    for lista in exp:
        lex.input(lista)
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
        
validarExpresion()


    
