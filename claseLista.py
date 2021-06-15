from classNodo import Nodo

class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            vehiculo = self.__actual.getVehiculo()
            self.__actual = self.__actual.getSiguiente()
            return vehiculo
    def AgregarVehiculo(self,unVehiculo):
        nodo = Nodo(unVehiculo)
        nodo.setSiguiente(self.__comienzo) # Insercion por cabeza de la lista
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
