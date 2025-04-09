class Nodo:
    def __init__(self, movimiento):
        self.movimiento = movimiento
        self.siguiente = None

class ListaMovimientos:
    def __init__(self):
        self.cabeza = None

    def agregar_movimiento(self, movimiento):
        nuevo_nodo = Nodo(movimiento)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_movimientos(self):
        actual = self.cabeza
        while actual:
            print(actual.movimiento)
            actual = actual.siguiente

def main():
    lista = ListaMovimientos()
    lista.agregar_movimiento("Movimiento 1")
    lista.agregar_movimiento("Movimiento 2")
    lista.agregar_movimiento("Movimiento 3")
    print("Lista de movimientos:")
    lista.mostrar_movimientos()

if __name__ == "__main__":
    main()