from cola import *
from operator import itemgetter, attrgetter

cola = Cola()

def mostrarRes(lista):
    print("Libros: ")
    for item in lista:
        print("--> {}".format(item))
    print("")

def getInfoFile():    
    lista = [x.split(", ") for x in open("./Libros.txt").readlines()]
    for i in range(len(lista)):
        miLista = lista[i]
        for j in range(len(miLista)):
            lst = [j, j ,j]            
        lst[0] = miLista[0]
        lst[1] = miLista[1]        
        lt2 = miLista[2].split(" \n")
        autor = lst[0]
        titulo = lst[1]
        tema = lt2[0]        
        libro = {
            'Titulo': titulo,
            'Autor': autor,
            'Tema': tema
        }        
        cola.encolar(libro)                    
        clave = libro.keys()        
        valor = libro.values()
        cantidad_datos = libro.items()
        """
        for clave in cola.items:
            print(clave[1])
            #if(clave == 'Titulo'):
                #print (clave + valor)
        #ordena por valores
            
        for key, value in sorted(libro.iteritems(), key = itemgetter(1), reverse = False):
            print(key, value)
        """
def buscar(key, value):
    cola_res = Cola()
    for item in cola.items:
        if value == item[key]:
            cola_res.encolar(item)    
    putInfoFile(cola_res.items)
    mostrarRes(cola_res.items)

def putInfoFile(lista):    
    archivo = open("./librosOrdenados.txt", "w")
    archivo.write(str(lista))
    archivo.close()

def ordenar(llave, value):
    cola_ord = Cola()
    for item in cola.items:
        if value == item[llave]:
            cola_ord.encolar(item)            
            #sorted(cola_ord.items, key=attrgetter('Titulo'))
    mostrarRes(cola_ord.items)

def sortedDictValues(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

def run():
    getInfoFile()
    print("*** Ordenar por cola los libros ***")
    tipos = "1) Consultar libro por autor \n2) Consultar libro por tema \n3) Consultar libro por titulo \n4) Mostrar libros \n5)Terminar"
    
    opcion = int(raw_input("Seleccione el numero de la opcion a consultar: \n{}:\n".format(tipos)))
        
    if opcion == 1:
        print("\t\t Consultar libros por autor")
        busqueda = raw_input ("Ingrese el nombre del autor del libro: ")
        buscar('Autor', busqueda)
        print("ordenar por titulo")
        ordenar('Autor', busqueda)
        
    elif opcion == 2:
        print("\t\t Consultar libros por tema")
        busqueda = raw_input ("Ingrese el tema del libro: ")
        buscar('Tema', busqueda)
    elif opcion == 3:
        print("\t\t Consultar libros por titulo")
        busqueda = raw_input ("Ingrese el titulo del libro: ")
        buscar('Titulo', busqueda)
    elif opcion == 4:            
        mostrarRes(cola.items)
    elif opcion == 5:
        exit()
    else:
        print("Opcion no valida, vuelva a digitar una opcion")
        
    
if __name__ == '__main__':
    run()
