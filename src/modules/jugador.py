## Clase mas general
class Jugador:
    def __init__(self, numeroCamiseta: int, apellido: str, minutosJugados: int):
        self.numeroCamiseta: int = numeroCamiseta
        self.apellido: str = apellido
        self.minutosJugados: int = minutosJugados
