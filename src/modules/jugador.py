## Clase mas general
class Jugador:
    def __init__(self, numeroCamiseta: int, apellido: str, minutosJugados: int):
        self.numeroCamiseta: int = numeroCamiseta
        self.apellido: str = apellido
        self.minutosJugados: int = minutosJugados

    def posicion(self):
        return self.__class__.__name__

    def mostrar(self):
        print(f"Número: {self.numeroCamiseta}")
        print(f"Apellido: {self.apellido}")
        print(f"Posición: {self.posicion()}")
        print(f"Minutos: {self.minutosJugados}")