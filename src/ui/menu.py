from src.modules.arquero import Arquero
from src.modules.defensor import Defensor
from src.modules.central import Central
from src.modules.delantero import Delantero

def buscar_jugador(equipo, numero):
    """Busca un jugador por su número de camiseta y lo devuelve."""
    for jugador in equipo:
        if jugador.numeroCamiseta == numero:
            return jugador
    return None

def cargar_jugador(equipo):
    print("\n--- Cargar Nuevo Jugador ---")
    print("Seleccione la posición que desea cargar:")
    print("1. Arquero")
    print("2. Defensor")
    print("3. Central")
    print("4. Delantero")
    opcion_pos = input("Opción: ")
    
    if opcion_pos not in ['1', '2', '3', '4']:
        print("Posición no válida. Carga cancelada.")
        return

    apellido = input("Apellido del jugador: ")
    numero = int(input("Número de camiseta: "))
    
    # Se valida que no exista ya ese número
    if buscar_jugador(equipo, numero):
        print(f"Error: Ya existe un jugador con la camiseta {numero}.")
        return

    minutos = int(input("Minutos jugados inicialmente: "))
    
    if opcion_pos == '1':
        jugador = Arquero(numero, apellido, minutos)
    else:
        goles = int(input("Goles marcados inicialmente: "))
        if opcion_pos == '2':
            jugador = Defensor(numero, apellido, minutos, goles)
        elif opcion_pos == '3':
            jugador = Central(numero, apellido, minutos, goles)
        else:
            jugador = Delantero(numero, apellido, minutos, goles)

    equipo.append(jugador)
    print(f"\nJugador {apellido} {numero} cargado exitosamente como {jugador.posicion()}")

def actualizar_estadisticas_partido(equipo):
    print("\n--- Actualizar Estadísticas de Partido ---")
    numero = int(input("Ingrese el número de camiseta del jugador: "))
    jugador = buscar_jugador(equipo, numero)
    
    if not jugador:
        print("Jugador no encontrado.")
        return
        
    print(f"\nActualizando a: {jugador.apellido} ({jugador.posicion()})")
    
    # Sumar minutos
    minutos_extra = int(input(f"Minutos a sumar (actuales: {jugador.minutosJugados}): "))
    jugador.minutosJugados += minutos_extra
    
    # Sumar goles si no es arquero
    if not isinstance(jugador, Arquero):
        goles_extra = int(input(f"Goles a sumar (actuales: {jugador.goles}): "))
        jugador.goles += goles_extra
        
    print("\nEstadísticas actualizadas correctamente")

def gestionar_jugador(equipo):
    print("\n--- Gestionar Jugador ---")
    numero = int(input("Ingrese el número de camiseta del jugador a gestionar: "))
    jugador = buscar_jugador(equipo, numero)
    
    if not jugador:
        print("Jugador no encontrado.")
        return
        
    print(f"\nOpciones para {jugador.apellido}:")
    print("1. Modificar Apellido")
    print("2. Modificar Número de Camiseta")
    print("3. Eliminar Jugador")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        nuevo_apellido = input("Nuevo apellido: ")
        jugador.apellido = nuevo_apellido
        print("Apellido actualizado.")
        
    elif opcion == '2':
        nuevo_numero = int(input("Nuevo número de camiseta: "))
        if buscar_jugador(equipo, nuevo_numero):
            print("Error: Ese número ya está en uso por otro jugador.")
        else:
            jugador.numeroCamiseta = nuevo_numero
            print("Número de camiseta actualizado.")
            
    elif opcion == '3':
        confirmacion = input(f"¿Estás seguro de eliminar a {jugador.apellido}? (s/n): ")
        if confirmacion.lower() == 's':
            equipo.remove(jugador)
            print("Jugador eliminado del equipo.")
        else:
            print("Operación cancelada.")
    else:
        print("Opción no válida.")

def mostrar_estadisticas(equipo):
    print("\n--- Estadísticas del Equipo ---")
    if not equipo:
        print("Todavía no hay jugadores cargados.")
        return
        
    for jugador in equipo:
        print("-" * 20)
        jugador.mostrar()
    print("-" * 20)

def iniciar_menu():
    equipo = [] 
    opcion = ""
    
    while opcion != '5':
        print("\n" + "="*35)
        print("   SISTEMA DE GESTIÓN DE EQUIPO")
        print("="*35)
        print("1. Cargar nuevo jugador")
        print("2. Consultar estadísticas de todos")
        print("3. Actualizar rendimiento (Minutos/Goles)")
        print("4. Gestionar jugador (Editar/Eliminar)")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == '1':
            cargar_jugador(equipo)
        elif opcion == '2':
            mostrar_estadisticas(equipo)
        elif opcion == '3':
            actualizar_estadisticas_partido(equipo)
        elif opcion == '4':
            gestionar_jugador(equipo)
        elif opcion == '5':
            print("\nCerrando el sistema.")
        else:
            print("\nOpción incorrecta. Por favor, intenta de nuevo.")
