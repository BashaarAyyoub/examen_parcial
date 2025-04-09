from hanoi.hanoi import Hanoi

def main():
    print("Seleccione el juego que desea jugar:")
    print("1. Torres de Hanoi")
    # Add more games here as needed
    opcion = input("Ingrese el número de su elección: ")

    if opcion == "1":
        num_discos = int(input("Ingrese el número de discos: "))
        juego = Hanoi(num_discos)
        juego.resolver()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
