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

def main():
    caballo = Caballo()
    inicio = pedir_vector()
    resultado = caballo.resolver(inicio)

    if resultado:
        print("Camino encontrado:")
        for i, pos in enumerate(resultado):
            print(f"Paso {i + 1}: {pos}")
    else:
        print("No se encontró un camino válido.")

if __name__ == "__main__":
    main()
