"""
@author: David
"""
def getFiles():
    archivo = open('./expresiones.in','r')
    filas = (archivo.read().splitlines())
    return filas

if __name__  == '__main__':
    getFiles()