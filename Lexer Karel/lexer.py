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
    'iniciar_programa',
    'inicia_ejecucion',
    'termina_ejecucion',
    'finalizar_programa',)
declaracionProcedimiento = ('define_nueva_instruccion',
    'como',)
expresion = ('LLAMADA','SI', 'MIENTRAS', 'PARA',
    'apagate',
    'gira_izquierda',
    'avanza',
    'coge_zumbador',
    'deja_zumbador',
    'sal_de_instruccion',
    'inicio',
    'fin', )
funcionBooleana = ('frente_libre',
    'frente_bloqueado',
    'izquierda_libre',
    'izquierda_bloqueada',
    'derecha_libre',
    'derecha_bloqueada',
    'junto_a_zumbador',
    'no_junto_a_zumbador',
    'algun_zumbador_en_la_mochila',
    'ningun_zumbador_en_la_mochila',
    'orientado_al_norte',
    'orientado_al_sur',
    'orientado_al_este',
    'orientado_al_oeste',
    'no_orientado_al_norte',
    'no_orientado_al_sur',
    'no_orientado_al_este',
    'no_orientado_al_oeste',)

tokens = declaracionPrograma + declaracionProcedimiento + expresion + funcionBooleana + ('IDENTIFICADOR','DECIMAL')
t_ignore = ' \t'
def t_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_IDENTIFICADOR(t):
    r'[a-zA-Z]'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lista = []
def getFile():
    file = open('codigo.in', 'r')
    filas = (file.read().splitlines())
    print(filas)
    for exp in filas:
        resultado = tokens(exp)
        setFile(resultado)
        lista = []
        print(exp)
    file.close()
def setFile(result):
    file = open('codigo.out', 'a')
    file.write(str(result) + '\n')
    file.close()

getFile()
lex.lex()

def tokens(expresion):
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista
