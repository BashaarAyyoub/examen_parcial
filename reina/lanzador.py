from reinas import Tablero

def main():
    n = int(input("Introduce el número de reinas: "))
    tablero = Tablero(n)
    soluciones = tablero.resolver()

    print(f"\nSe encontraron {len(soluciones)} soluciones para un tablero de {n}x{n}:\n")
    for i, solucion in enumerate(soluciones, 1):
        print(f"Solución {i}:")
        tablero.mostrar_tablero(solucion)

if __name__ == "__main__":
    main()
