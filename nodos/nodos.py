import tkinter as tk

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

def juego_1():
    print("Ejecutando Juego 1...")
    # Aquí iría la lógica del Juego 1

def juego_2():
    print("Ejecutando Juego 2...")
    # Aquí iría la lógica del Juego 2

def juego_3():
    print("Ejecutando Juego 3...")
    # Aquí iría la lógica del Juego 3

def mostrar_menu_juegos():
    """Muestra un menú en Tkinter para elegir un juego."""
    root = tk.Tk()
    root.title("Seleccionar Juego")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Seleccione un juego:", font=("Arial", 14))
    label.pack()

    juegos = [
        ("Juego 1", juego_1),
        ("Juego 2", juego_2),
        ("Juego 3", juego_3),
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