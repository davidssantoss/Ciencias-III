import re

def validarExpresion():
    operators = "[+,-,*,/]"
    values = "[0-9]"
    var = "[a-z]"
    str = "5 5 + 9 *"    
    y = re.split("\s", str)
    print(y)
    for lista in y:
        print('El siguiente digito %s' % lista, 'es de tipo')
    
    
validarExpresion()
