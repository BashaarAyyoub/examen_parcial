from hanoi.hanoi import Hanoi
# ...importar módulos necesarios para Caballo y Reina...

def main():
    print("Seleccione el juego que desea jugar:")
    print("1. Caballo")
    print("2. Torres de Hanoi")
    print("3. Reina")
    opcion = input("Ingrese el número de su elección: ")

    if opcion == "1":
        # Lógica para el juego del Caballo
        print("Juego del Caballo seleccionado.")
        # ...código para inicializar y resolver el juego del Caballo...
    elif opcion == "2":
        num_discos = int(input("Ingrese el número de discos: "))
        juego = Hanoi(num_discos)
        juego.resolver()
    elif opcion == "3":
        # Lógica para el juego de la Reina
        print("Juego de la Reina seleccionado.")
        # ...código para inicializar y resolver el juego de la Reina...
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
