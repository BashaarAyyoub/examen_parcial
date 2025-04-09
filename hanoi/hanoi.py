class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def agregar_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

    def mostrar_movimientos(self):
        for movimiento in self.movimientos:
            print(movimiento)

class Hanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.movimientos = ListaMovimientos()

    def mover(self, origen, destino):
        movimiento = f"Mover disco de {origen} a {destino}"
        self.movimientos.agregar_movimiento(movimiento)

    def resolver_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            self.mover(origen, destino)
        else:
            self.resolver_hanoi(n - 1, origen, destino, auxiliar)
            self.mover(origen, destino)
            self.resolver_hanoi(n - 1, auxiliar, origen, destino)

    def resolver(self):
        self.resolver_hanoi(self.num_discos, 'A', 'B', 'C')
        self.movimientos.mostrar_movimientos()

if __name__ == "__main__":
    num_discos = int(input("Introduce el número de discos: "))
    hanoi = Hanoi(num_discos)
    hanoi.resolver()



