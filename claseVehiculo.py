class Vehiculo:
    __modelo = ''
    __cantpuertas = 0
    __color = ''
    __precioBase = 0.0

    def __init__(self,mod,cpuer,color,precio,ver='',marc='',pat='',an=0,km=0.0):
        self.__modelo = mod
        self.__cantpuertas = cpuer
        self.__color = color
        self.__precioBase = precio

    def getModelo(self):
        return self.__modelo
    def getCantidadPuertas(self):
        return self.__cantpuertas
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__precioBase
    def getMarca(self):
        pass
    def getPatente(self):
        pass
    def getAnho(self):
        pass
    def getKilometraje(self):
        pass
    def setPrecioBase(self,precionuevo):
        if type(precionuevo) is float:
            self.__precioBase = precionuevo
            print('Se modifico el precio base.')
        else:
            print('Error. No se modifico el precio base.')
    def CalculaImporteVenta(self):
        pass

    def MuestraDatos(self):
        pass
