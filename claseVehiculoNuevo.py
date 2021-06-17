from claseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca = 'Lamborghini'
    __version = '' # Base o Full

    def __init__(self,mod,cpuer,color,precio,ver):
        super().__init__(mod,cpuer,color,precio)
        self.__version = ver

    def getMarca(self): # Ojo posible metodo estatico
        return self.__marca

    def getVersion(self):
        return self.__version

    def CalculaImporteVenta(self):
        patentamiento = ((10 * super().getPrecioBase()) / 100) # Gastos de patentamiento
        costofull = ((2 * super().getPrecioBase()) / 100) # 2% si es full
        if self.getVersion() == 'Full':
            importe = super().getPrecioBase() + patentamiento + costofull
        else:
            importe = super().getPrecioBase() + patentamiento
        return importe

    def MuestraDatos(self):
        print('Marca:', self.__marca)
        print('Modelo:', super().getModelo())
        print('Version:',self.__version)
        print('Cantidad de puertas:', super().getCantidadPuertas())
        print('Color:', super().getColor())
        print('Precio base:', super().getPrecioBase())
        print('Importe final de venta:', self.CalculaImporteVenta())
