import lexer

def getFile():
    file = open(input("Digite la ruta del archivo a procesar: "), 'r')
    filas = (file.read().splitlines())   
    clearFile('codigo.out')     
    for exp in filas:      
        resultado = lexer.tokens(exp)
        setFile(resultado)
        lexer.lista = []
        print(exp)     
    file.close()
    
def setFile(result):
    file = open('codigo.out', 'a')
    file.write(str(result) + '\n')
    file.close()
def clearFile(archivo):
    file = open(archivo, 'w').close()

def run():
    getFile()

if __name__ == '__main__':
    run()
