from pila import *
from arbol import *

pila = Pila()
def run():
    print ("\t\t*** EVALUADOR DE EXPRESIONES POSTFIJA ***\n")
    archivo = open("./expresiones_in.txt", 'r')
    print("las expresiones del archivo son: \n")
    i = 1
    for linea in archivo.readlines():
        x = linea.split("\n")        
        print("%d) " %i + x[0])
        convertir(x[0].split(" "), pila)
        resultado = evaluar(pila.desapilar())
        print("El valor de la expresion es: %s" % resultado + "\n")
        writeResult(str(resultado)+"\n")
        i += 1
    archivo.close()

    
def writeResult(res):
    archivo = open("./Expresiones_out.txt", "a")
    archivo.write(res)
    archivo.close()

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

if __name__ == '__main__':
    run()
