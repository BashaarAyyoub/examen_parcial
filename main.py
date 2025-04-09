import tkinter as tk
from hanoi.hanoi import Hanoi
from caballo.caballos import Caballo
from reina.reinas import Tablero

def juego_caballos_tkinter():
    root = tk.Tk()
    root.title("Juego del Caballo")

    label = tk.Label(root, text="Introduce la posición inicial (fila, columna):", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=10)

    def dibujar_tablero():
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "gray"
                canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

    def dibujar_camino(camino):
        for paso, (fila, columna) in enumerate(camino):
            x, y = columna * 50 + 25, fila * 50 + 25
            canvas.create_text(x, y, text=str(paso + 1), fill="red", font=("Arial", 12))

    def resolver_caballo():
        try:
            pos = list(map(int, entry.get().split(',')))
            if len(pos) == 2 and 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                caballo = Caballo()
                resultado = caballo.resolver(pos)
                if resultado:
                    result_label.config(text="Camino encontrado.")
                    dibujar_tablero()
                    dibujar_camino(resultado)
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

    dibujar_tablero()
    root.mainloop()

def juego_hanoi_tkinter():
    root = tk.Tk()
    root.title("Juego de las Torres de Hanoi")

    label = tk.Label(root, text="Introduce el número de discos:", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack(pady=10)

    def dibujar_torres(discos):
        canvas.delete("all")
        for i in range(3):
            canvas.create_rectangle(100 + i * 100, 50, 120 + i * 100, 250, fill="black")
        for torre, pila in enumerate(discos):
            for nivel, disco in enumerate(pila):
                x1 = 100 + torre * 100 - disco * 10
                x2 = 120 + torre * 100 + disco * 10
                y1 = 250 - nivel * 20
                y2 = 250 - (nivel + 1) * 20
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

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

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=10)

    def dibujar_tablero(n, solucion):
        canvas.delete("all")
        for i in range(n):
            for j in range(n):
                color = "white" if (i + j) % 2 == 0 else "gray"
                canvas.create_rectangle(j * 400 // n, i * 400 // n, (j + 1) * 400 // n, (i + 1) * 400 // n, fill=color)
                if solucion[i] == j:
                    canvas.create_text(j * 400 // n + 200 // n, i * 400 // n + 200 // n, text="♛", fill="red", font=("Arial", 16))

    def resolver_reinas():
        try:
            n = int(entry.get())
            if n > 0:
                tablero = Tablero(n)
                soluciones = tablero.resolver()
                if soluciones:
                    result_label.config(text=f"Se encontró una solución. Mostrando la primera.")
                    dibujar_tablero(n, soluciones[0])
                else:
                    result_label.config(text="No se encontraron soluciones.")
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

def mostrar_menu_principal():
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

if __name__ == "__main__":
    mostrar_menu_principal()
