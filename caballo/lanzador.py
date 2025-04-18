from caballos import Caballo

def pedir_vector():
    while True:
        try:
            x = int(input("Introduce la fila inicial (0-7): "))
            y = int(input("Introduce la columna inicial (0-7): "))
            if 0 <= x < 8 and 0 <= y < 8:
                return [x, y]
        except ValueError:
            pass
        print("Entrada no válida. Intenta de nuevo.")

def menu():
    print("Selecciona un juego:")
    print("1. Juego del Caballo")
    # Aquí puedes agregar más opciones para otros juegos
    print("0. Salir")
    while True:
        try:
            opcion = int(input("Introduce tu opción: "))
            if opcion in [0, 1]:  # Agregar más opciones según los juegos disponibles
                return opcion
        except ValueError:
            pass
        print("Opción no válida. Intenta de nuevo.")

def main():
    while True:
        opcion = menu()
        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            caballo = Caballo()
            inicio = pedir_vector()
            resultado = caballo.resolver(inicio)

            if resultado:
                print("Camino encontrado:")
                for i, pos in enumerate(resultado):
                    print(f"Paso {i + 1}: {pos}")
            else:
                print("No se encontró un camino válido.")
        # Aquí puedes agregar más elif para otros juegos

if __name__ == "__main__":
    main()
