from .jugador import Jugador

## Especializacion para aquellos jugadores que marcan goles

class JugadorDeCampo(Jugador):
    def __init__(self, numeroCamiseta, apellido, minutosJugados, goles):
        super().__init__(numeroCamiseta, apellido, minutosJugados)
        self.goles = goles

    def mostrar(self):
        super().mostrar()
        print(f"Goles: {self.goles}")