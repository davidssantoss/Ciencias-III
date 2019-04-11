def run():
    archivo = open("./expresiones_in.txt", 'r')
    getInfo = archivo.read().splitlines()
    print(getInfo)



if __name__ == '__main__':
    run()
