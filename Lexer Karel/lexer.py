import ply.lex as lex
import re

"""
Declaracion del programa
Declaracion de procedimiento
Expresion
Expresion llamada
ExpresionSi
ExpresionMientras
Expresion para
Expresion vacia
Termino
ClausulaY
ClausulaNo
ClausulaAtomica
Expresion entera
identificador
Decimal
Cadena
Funcion Booleana
Digito
Letra
EOF
@Link de documentacion de pascal para el lexer: https://omegaup.com/karel.js/manual/KarelSyntax_es.html#prod21
"""

tokens = ['declaracionPrograma','declaracionProcedimiento','CLSLN','DECIMAL','EXPRESION',"STRING","Funcion_Booleana","ClausulaY","ClausulaNo",
"ClausulaAtomica", "ExpresionSi","ExpresionMientras","ExpresionPara"]
t_ignore = ' \t'
def t_ExpresionPara(t):
    r'(repetir|veces)'
def t_ExpresionMientras(t):
    r'(mientras|hacer)'
    return t
def t_ExpresionSi(t):
    r'(si|entonces|sino)'
    return t
def t_ClausulaAtomica(t):
    r'si-es-cero'
    return t
def t_ClausulaNo(t):
    r'no '
    return t
def t_ClausulaY(t):
    r'y'
    return t

def t_Funcion_Booleana(t):
    r'(frente-libre|frente-bloqueado|izquierda-libre|izquierda-bloqueada|derecha-libre|derecha-bloqueada|junto-a-zumbador|no-junto-a-zumbador|algun-zumbador-en-la-mochila|ningun-zumbador-en-la-mochila|orientado-al-norte|orientado-al-sur|orientado-al-este|orientado-al-oeste|no-orientado-al-norte|no-orientado-al-sur|no-orientado-al-este|no-orientado-al-oeste)'
    return t

def t_EXPRESION(t):
    r'(gira-izquierda|coge-zumbador|deja-zumbador|sal-de-instruccion|apagate|avanza|inicio|fin;)'
    return t

def t_declaracionPrograma(t):
    r'(iniciar-programa|inicia-ejecucion|termina-ejecucion|finalizar-programa)' 
    return t

def t_declaracionProcedimiento(t):
    r'(define-nueva-instruccion|como)'
    return t

def t_CLSLN(t):
    r'\;'
    return t

def t_STRING(t):
    r'(\w+-\w+|w+)'
    return t

def t_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lista = []
lex.lex()
def tokens(expresion):
    #print(expresion)
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista