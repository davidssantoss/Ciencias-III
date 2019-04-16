class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si esta vacia. """
 
    def __init__(self):
        """ Crea una pila vacia. """
        # La pila vacia se representa con una lista vacia
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila esta vacia levanta una excepcion. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")

    def es_vacia(self):
        """ Devuelve True si la lista esta vacia, False si no. """
        return self.items == []
