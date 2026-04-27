def input_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el campo no puede estar vacío.")


def input_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: debe ingresar un número válido.")