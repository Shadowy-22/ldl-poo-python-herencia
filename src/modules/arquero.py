from .jugador import Jugador

class Arquero(Jugador):
    def __init__(self, goles: int):
        self.goles: int = goles