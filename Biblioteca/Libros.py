from cola import *
from operator import itemgetter, attrgetter

cola = Cola()

def mostrarRes(lista):
    print("Libros en cola: ")
    for item in lista:
        print("--> {}".format(item))
    print("")

def getInfoFile():    
    lista = [x.split(", ") for x in open("./Libros.txt").readlines()]    
    for i in range(len(lista)):
        miLista = lista[i]
        for j in range(len(miLista)):
            lst = [j, j ,j, j]            
        lst[0] = miLista[0]
        lst[1] = miLista[1]
        lt = miLista[2]
        lt2 = miLista[3].split(" \n")
        autor = lst[0]
        titulo = lst[1]
        tema = lt
        paginas = lt2[0]
        listaTotal = (autor, titulo, tema, paginas)        
        cola.encolar(listaTotal)
        print(listaTotal)
    print("\n *** ordenar por autor y despues por titulo ***\n")    
    busqueda = raw_input("Digite el nombre del autor: ")
    cola_ord = Cola()
    for item in cola.items:
        if busqueda == item[0]:            
            cola_ord.encolar(item)
    mostrarRes(cola_ord.items)
    burbuja(cola_ord.items)
    organizado = cola_ord.items
    mostrarRes(organizado)  
        
def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def putInfoFile(lista):    
    archivo = open("./librosOrdenados.txt", "w")
    archivo.write(str(lista))
    archivo.close()


def run():
    print("\t ***Lista de libros del archivo***\n")
    getInfoFile()        
    
if __name__ == '__main__':
    run()
