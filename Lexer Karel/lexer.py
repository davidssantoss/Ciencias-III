import ply.lex as lex
import re

"""
Declaracion del programa
Declaracion de procedimiento
Expresion general
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

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()