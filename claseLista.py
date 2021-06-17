from classNodo import Nodo
from claseVehiculoUsado import VehiculoUsado
from claseVehiculoNuevo import VehiculoNuevo

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

    def CreaVehiculo(self):
        print('Carga de vehiculo.')
        mod = input('Ingrese modelo:')
        cpuer = int(input('Ingrese cantidad de puertas:'))
        color = input('Ingrese color:')
        precio = float(input('Ingrese precio base:'))
        op = int(input('¿Es un vehiculo nuevo? 1- Si. 2- No.'))
        if op == 1:
            ver = input('Ingrese version: (Base/Full):')
            unVehiculo = VehiculoNuevo(mod,cpuer,color,precio,ver)
            self.AgregarVehiculo(unVehiculo)
            print('Se ha registrado el vehiculo.')
        elif op == 2:
            marc = input('Ingrese marca:')
            pat = input('Ingrese patente:')
            an = int(input('Ingrese anho:'))
            km: float = float(input('Ingrese kilometraje:'))
            unVehiculo = VehiculoUsado(mod,cpuer,color,precio,marc,pat,an,km)
            self.AgregarVehiculo(unVehiculo)
            print('Se ha registrado el vehiculo.')

    def ModPrecioVehiculoUsado(self,pat): # Consigna 4
        for vehiculo in self:
            ban = False
            if isinstance(vehiculo,VehiculoUsado):
                if vehiculo.getPatente() == pat:
                    ban = True
                    print('Modificar precio de vehiculo usado.')
                    nuevopre = float(input('Ingrese nuevo precio base:'))
                    vehiculo.setPrecioBase(nuevopre)
                    print('Nuevo importe de venta:',vehiculo.CalculaImporteVenta())
                    print('------------------------------------')
                    break
        if ban == False:
            print('Error. No se encontro vehiculo usado con la patente proporcionada.')
            print('------------------------------------')

    def DatosMasEconomico(self): # Consigna 5 (Economico segun el precio base)
        print('Datos del vehiculo mas economico.')
        minprecio = self.__comienzo.getVehiculo().getPrecioBase() # Precio minimo registrado, lo inicializa con el primero
        vehiculominimo = self.__comienzo.getVehiculo()
        for vehiculo in self:
            if vehiculo.getPrecioBase() < minprecio:
                minprecio = vehiculo.getPrecioBase()
                vehiculominimo = vehiculo
        vehiculominimo.MuestraDatosBasicos()
        if isinstance(vehiculominimo,VehiculoUsado):
            print('Tipo de vehiculo: Usado.')
            vehiculominimo.MuestraDatos()
        elif isinstance(vehiculominimo,VehiculoNuevo):
            print('Tipo de vehiculo: Nuevo')
            vehiculominimo.MuestraDatos()

    def MuestraTodos(self): # Consigna 6
        print('Vehiculos a la venta.')
        print('------------------------------------')
        for vehiculo in self:
            if isinstance(vehiculo,VehiculoNuevo):
                print('Tipo de vehiculo: Nuevo')
            else:
                print('Tipo de vehiculo: Usado')
            print('Modelo:',vehiculo.getModelo())
            print('Cantidad de puertas:',vehiculo.getCantidadPuertas())
            print('Importe de venta:',vehiculo.CalculaImporteVenta())
            print('------------------------------------')

