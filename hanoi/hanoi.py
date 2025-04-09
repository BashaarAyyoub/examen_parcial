class Hanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.movimientos = []
        self.torres = {
            'A': list(reversed(range(1, num_discos + 1))),
            'B': [],
            'C': []
        }

    def resolver(self):
        self._mover(self.num_discos, 'A', 'C', 'B')

    def _mover(self, n, origen, destino, auxiliar):
        if n == 1:
            self._registrar_movimiento(origen, destino)
        else:
            self._mover(n - 1, origen, auxiliar, destino)
            self._registrar_movimiento(origen, destino)
            self._mover(n - 1, auxiliar, destino, origen)

    def _registrar_movimiento(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos.append((origen, destino))
        self.mostrar_torres()

    def mostrar_torres(self):
        print("Estado actual:")
        for torre in ['A', 'B', 'C']:
            print(f"{torre}: {self.torres[torre]}")
        print()



