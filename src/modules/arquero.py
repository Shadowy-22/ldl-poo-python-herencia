from .jugador import Jugador

class Arquero(Jugador):
    def __init__(self, numeroCamiseta, apellido, minutosJugados):
        super().__init__(numeroCamiseta, apellido, minutosJugados)


