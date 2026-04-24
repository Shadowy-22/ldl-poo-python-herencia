from .jugador import Jugador

## Especializacion para aquellos jugadores que marcan goles
class JugadorDeCampo(Jugador):
    def __init__(self, numero, apellido, minutos, goles):
        super().__init__(numero, apellido, minutos)
        self.goles = goles