from .jugadorcampo import JugadorDeCampo

## Se utiliza el polimorfismo para mostrar la posicion del jugador
class Delantero(JugadorDeCampo):
    def posicion(self):
        return self.__class__.__name__