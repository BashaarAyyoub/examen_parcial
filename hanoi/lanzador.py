from hanoi import Hanoi

def main():
    n = int(input("Introduce el número de discos: "))
    juego = Hanoi(n)
    print("\nResolviendo Torres de Hanoi...\n")
    juego.resolver()

    print(f"Total de movimientos: {len(juego.movimientos)}")
    for i, mov in enumerate(juego.movimientos, 1):
        print(f"Movimiento {i}: {mov[0]} → {mov[1]}")

if __name__ == "__main__":
    main()
