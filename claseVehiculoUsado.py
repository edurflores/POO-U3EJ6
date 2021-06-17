from claseVehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    __marca = ''
    __patente = ''
    __anho = 0
    __kilometraje = 0.0

    def __init__(self,mod,cpuer,color,precio,marc,pat,an,km):
        super().__init__(mod,cpuer,color,precio)
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
    def CalculaImporteVenta(self):
        antiguedad = 2021 - self.__anho
        importe = super().getPrecioBase() - (((super().getPrecioBase() * 1) / 100) * antiguedad)
        return importe
    def MuestraDatos(self):
        print('Marca:',self.__marca)
        print('Modelo:',super().getModelo())
        print('Anho:',self.__anho)
        print('Cantidad de puertas:',super().getCantidadPuertas())
        print('Color:',super().getColor())
        print('Patente:',self.__patente)
        print('Kilometraje:',self.__kilometraje)
        print('Precio base:',super().getPrecioBase())
        print('Importe final de venta:',self.CalculaImporteVenta())
