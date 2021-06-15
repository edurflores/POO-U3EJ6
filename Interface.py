from zope.interface import Interface

class IPrueba(Interface):
    def insertarElemento(elemento,posicion):
        pass
    
    def agregarElemento(elemento):
        pass
    
    def mostrarElemento(posicion):
        pass