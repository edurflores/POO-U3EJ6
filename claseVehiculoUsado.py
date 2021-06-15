from claseVehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    __marca = ''
    __patente = ''
    __anho = 0
    __kilometraje = 0.0

    def __init__(self,mod,cpuer,color,precio,ver,marc,pat,an,km):
        super().__init__(mod,cpuer,color,precio,ver,marc,pat,an,km)
        self.__marca = marc
        self.__patente = pat
        self.__anho = an
        self.__kilometraje = km

    def getPatente(self):
        return self.__patente
    def getAnho(self):
        return self.__anho
    def getKilometraje(self):
        return self.__kilometraje
