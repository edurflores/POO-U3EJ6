from claseLista import Lista

if __name__ == '__main__':
    Lista = Lista()
    print('Menu')
    print('1- Registra vehiculo manualmente.\n2- \n4- Modificar precio base de vehiculo usado (Consigna 4).\n5- Mostrar datos de vehiculo mas economico.\n6- Mostrar todos los vehiculos a la venta.\n7- Almacenar objetos de la lista en archivo JSON.')
    op = int(input('Seleccione opcion:'))
    while op != 0:
        if op == 1:
            Lista.CreaVehiculo()
        elif op == 4:
            pat = input('Ingrese patente a buscar:')
            Lista.ModPrecioVehiculoUsado(pat)
        elif op == 5:
            Lista.DatosMasEconomico()
        elif op == 6:
            Lista.MuestraTodos()
        op = int(input('Seleccione opcion:'))
