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
declaracionPrograma = ('PROGRAMA',
    'iniciar-programa',
    'inicia-ejecucion',
    'termina-ejecucion',
    'finalizar-programa',)
declaracionProcedimiento = ('define-nueva-instruccion',
    'como',)
expresion = ('LLAMADA','SI', 'MIENTRAS', 'PARA',
    'apagate',
    'gira-izquierda',
    'avanza',
    'coge-zumbador',
    'deja-zumbador',
    'sal-de-instruccion',
    'inicio',
    'fin', )
funcionBooleana = ('frente-libre',
    'frente-bloqueado',
    'izquierda-libre',
    'izquierda-bloqueada',
    'derecha-libre',
    'derecha-bloqueada',
    'junto-a-zumbador',
    'no-junto-a-zumbador',
    'algun-zumbador-en-la-mochila',
    'ningun-zumbador-en-la-mochila',
    'orientado-al-norte',
    'orientado-al-sur',
    'orientado-al-este',
    'orientado-al-oeste',
    'no-orientado-al-norte',
    'no-orientado-al-sur',
    'no-orientado-al-este',
    'no-orientado-al-oeste',)

tokens = declaracionPrograma + declaracionProcedimiento + expresion + funcionBooleana + ('IDENTIFICADOR')

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()