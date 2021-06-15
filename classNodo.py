from claseVehiculo import Vehiculo
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado

class Nodo:
    __vehiculo = None
    __siguiente = None

    def __init__(self,unVehiculo):
        self.__vehiculo = unVehiculo
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    def getVehiculo(self):
        return self.__vehiculo
    def setSiguiente(self,sig):
        self.__siguiente = sig
