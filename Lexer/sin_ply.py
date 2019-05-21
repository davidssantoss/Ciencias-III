import re
"""
@author: David S
"""

def validarExpresion():

    str = "5 5 & 9 * a"
    y = re.split("\s", str)

    for lista in y:
        print lista
        
        buscarDec(lista)
        buscarVar(lista)
        buscarOpe(lista)

def buscarDec(lista):
    values = "[0-9]"
    v = re.findall(values, lista)
    if (v):
        print ("El siguiente digito %s " %v + "es de tipo value")
    return v

def buscarVar(lista):
    variable = "[a-z]"
    var = re.findall(variable, lista)
    if (var):
        print ("El siguiente digito %s " %var + "es de tipo variable")
    return var

def buscarOpe(lista):
    operators = "[+,-,*,/]"
    op = re.findall(operators, lista)
    if (op):
        print ("El siguiente digito %s " %op + "es de tipo operator")
    return op

validarExpresion()
