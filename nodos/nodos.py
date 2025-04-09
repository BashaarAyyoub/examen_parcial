import tkinter as tk
from hanoi.hanoi import Hanoi
from caballo.caballos import Caballo
from reina.reinas import Tablero

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

    def mostrar_en_tkinter(self):
        """Display the list of movements in a Tkinter window."""
        root = tk.Tk()
        root.title("Lista de Movimientos")
        
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        label = tk.Label(frame, text="Movimientos:", font=("Arial", 14))
        label.pack()

        actual = self.cabeza
        while actual:
            movimiento_label = tk.Label(frame, text=actual.movimiento, font=("Arial", 12))
            movimiento_label.pack(anchor="w")
            actual = actual.siguiente

        close_button = tk.Button(root, text="Cerrar", command=root.destroy)
        close_button.pack(pady=10)

        root.mainloop()

def juego_caballos_tkinter():
    root = tk.Tk()
    root.title("Juego del Caballo")

    label = tk.Label(root, text="Introduce la posición inicial (fila, columna):", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def resolver_caballo():
        try:
            pos = list(map(int, entry.get().split(',')))
            if len(pos) == 2 and 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                caballo = Caballo()
                resultado = caballo.resolver(pos)
                if resultado:
                    result_label.config(text=f"Camino encontrado:\n{resultado}")
                else:
                    result_label.config(text="No se encontró un camino válido.")
            else:
                result_label.config(text="Posición no válida. Debe estar entre 0 y 7.")
        except ValueError:
            result_label.config(text="Entrada no válida. Usa el formato: fila,columna")

    button = tk.Button(root, text="Resolver", command=resolver_caballo)
    button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)

    root.mainloop()

def juego_hanoi_tkinter():
    root = tk.Tk()
    root.title("Juego de las Torres de Hanoi")

    label = tk.Label(root, text="Introduce el número de discos:", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def resolver_hanoi():
        try:
            num_discos = int(entry.get())
            if num_discos > 0:
                hanoi = Hanoi(num_discos)
                hanoi.resolver()
                result_label.config(text="Resolución completada. Revisa la consola para los movimientos.")
            else:
                result_label.config(text="El número de discos debe ser mayor que 0.")
        except ValueError:
            result_label.config(text="Entrada no válida. Introduce un número entero.")

    button = tk.Button(root, text="Resolver", command=resolver_hanoi)
    button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)

    root.mainloop()

def juego_reina_tkinter():
    root = tk.Tk()
    root.title("Juego de las N-Reinas")

    label = tk.Label(root, text="Introduce el tamaño del tablero (n):", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def resolver_reinas():
        try:
            n = int(entry.get())
            if n > 0:
                tablero = Tablero(n)
                soluciones = tablero.resolver()
                result_label.config(text=f"Se encontraron {len(soluciones)} soluciones. Revisa la consola para los detalles.")
                for i, solucion in enumerate(soluciones, 1):
                    print(f"Solución {i}:")
                    tablero.mostrar_tablero(solucion)
            else:
                result_label.config(text="El tamaño del tablero debe ser mayor que 0.")
        except ValueError:
            result_label.config(text="Entrada no válida. Introduce un número entero.")

    button = tk.Button(root, text="Resolver", command=resolver_reinas)
    button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)

    root.mainloop()

def mostrar_menu_juegos():
    """Muestra un menú en Tkinter para elegir un juego."""
    root = tk.Tk()
    root.title("Seleccionar Juego")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Seleccione un juego:", font=("Arial", 14))
    label.pack()

    juegos = [
        ("Juego del Caballo", juego_caballos_tkinter),
        ("Juego de las Torres de Hanoi", juego_hanoi_tkinter),
        ("Juego de las N-Reinas", juego_reina_tkinter),
    ]

    for nombre, funcion in juegos:
        boton = tk.Button(frame, text=nombre, font=("Arial", 12), command=lambda f=funcion: [f(), root.destroy()])
        boton.pack(fill="x", pady=5)

    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)

    root.mainloop()

def main():
    print("Mostrando menú de juegos en ventana Tkinter...")
    mostrar_menu_juegos()

if __name__ == "__main__":
    main()