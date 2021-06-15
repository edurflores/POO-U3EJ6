from claseVehiculo import Vehiculo
from claseVehiculoUsado import VehiculoUsado
from claseVehiculoNuevo import VehiculoNuevo
from claseLista import Lista

class ManejadorVehiculos:

    def __init__(self):
        ListaVehiculos = Lista() # Crea lista

    def CreaVehiculo(self):
        print('Carga de vehiculo.')
        mod = input('Ingrese modelo:')
        cpuer = int('Ingrese cantidad de puertas:')
        color = input('Ingrese color:')
        precio = float(input('Ingrese precio base:'))
        op = int(input('¿Es un vehiculo nuevo? 1- Si. 2- No.'))
        if op == 1:
            ver = input('Ingrese version: (Base/Full):')
            unVehiculo = VehiculoNuevo(mod,cpuer,color,precio,ver)
        elif op == 2:
            marc = input('Ingrese marca:')
            pat = input('Ingrese patente:')
            an = int(input('Ingrese anho:'))
            km = float(input('Ingrese kilometraje:'))
            unVehiculo = VehiculoUsado(mod,cpuer,color,precio,marc,pat,an,km)