class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = [-1] * n
        self.soluciones = []

    def resolver(self):
        self._colocar_reina(0)
        return self.soluciones

    def _colocar_reina(self, fila):
        if fila == self.n:
            self.soluciones.append(self.tablero[:])
            return

        for columna in range(self.n):
            if self._es_valido(fila, columna):
                self.tablero[fila] = columna
                self._colocar_reina(fila + 1)
                self.tablero[fila] = -1

    def _es_valido(self, fila, columna):
        for i in range(fila):
            if (self.tablero[i] == columna or
                abs(self.tablero[i] - columna) == abs(i - fila)):
                return False
        return True

    def mostrar_tablero(self, solucion):
        for fila in range(self.n):
            linea = ""
            for columna in range(self.n):
                if solucion[fila] == columna:
                    linea += "♛ "
                else:
                    linea += ". "
            print(linea)
        print()
