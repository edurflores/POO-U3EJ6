from claseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca = 'Lamborghini'
    __version = '' # Base o Full

    def __init__(self,mod,cpuer,color,precio,ver,marc,pat,an,km):
        super().__init__(mod,cpuer,color,precio,ver,marc,pat,an,km)
        self.__version = ver

    def getMarca(self): # Ojo posible metodo estatico
        return self.__marca

    def getVersion(self):
        return self.__version