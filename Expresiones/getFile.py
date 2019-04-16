from pila import *
from arbol import *

pila = Pila()
def run():
    archivo = open("./expresiones_in.txt", 'r')
    for linea in archivo.readlines():
        x = linea.split("\n")
        convertir(x[0].split(" "), pila)
        resultado = evaluar(pila.desapilar())
        print(str(resultado))
        writeResult(str(resultado)+"\n")
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
