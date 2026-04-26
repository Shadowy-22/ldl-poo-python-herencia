## TODO: - Adaptar esta lógica al proyecto actual (usar clases de src/modules)
## - Mover la ejecución a main.py
## - Eliminar este archivo una vez integrada la funcionalidad
class Jugador:
    def __init__(self, nro_camiseta, apellido, posicion):
        self.nro_camiseta = nro_camiseta
        self.apellido = apellido
        self.posicion = posicion
        self.minutos_jugados = 0

    def cargar_minutos(self, minutos):
        self.minutos_jugados = self.minutos_jugados + minutos

class Arquero(Jugador):
    def __init__(self, nro_camiseta, apellido):
        # El arquero hereda de Jugador y su posición es fija 
        super().__init__(nro_camiseta, apellido, "Arquero")

class JugadorCampo(Jugador):
    def __init__(self, nro_camiseta, apellido, posicion):
        super().__init__(nro_camiseta, apellido, posicion)
        self.goles = 0 # Atributo propio de esta clase 

    def cargar_goles(self, cantidad):
        self.goles = self.goles + cantidad

# --- Gestión del Sistema (Menú) ---
plantel = []

def menu():
    while True:
        print("\n--- GESTIÓN DE EQUIPO DE FÚTBOL ---")
        print("1. Cargar nuevo jugador")
        print("2. Ver estadísticas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            apellido = input("Apellido del jugador: ")
            nro = int(input("Número de camiseta: "))
            pos = input("Posición (Arquero, Defensor, Central, Delantero): ").capitalize()
            
            if pos == "Arquero":
                nuevo_jugador = Arquero(nro, apellido)
            else:
                nuevo_jugador = JugadorCampo(nro, apellido, pos)
                g = int(input("Goles marcados: "))
                nuevo_jugador.cargar_goles(g)
            
            m = int(input("Minutos jugados: "))
            nuevo_jugador.cargar_minutos(m)
            plantel.append(nuevo_jugador)
            print("Jugador registrado correctamente.")

        elif opcion == "2":
            print("\n--- ESTADÍSTICAS DEL EQUIPO ---")
            for j in plantel:
                datos = f"#{j.nro_camiseta} {j.apellido} ({j.posicion}) | Minutos: {j.minutos_jugados}"
                if isinstance(j, JugadorCampo):
                    datos = datos + f" | Goles: {j.goles}"
                print(datos)
        
        elif opcion == "3":
            print("Cerrando sistema...")
            break

if __name__ == "__main__":
    menu()