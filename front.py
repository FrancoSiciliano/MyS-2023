import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sym
import tkinter as tk


class PlotWindow:
    def __init__(self, root):
        self.root = root
        self.canvas = None

        # Crear la entrada de texto para la ecuación
        equation_label = tk.Label(root, text="Ingrese la ecuación:")
        equation_label.pack()

        self.equation_entry = tk.Entry(root, width=50)
        self.equation_entry.pack()
        self.equation_entry.bind('<KeyRelease>', self.plot_equation)

        # Crear el lienzo de Matplotlib en la ventana de Tkinter
        self.fig, self.ax = plt.subplots()
        self.ax.axis('off')
        self.ax.text(0.5, 0.5, "$f(x):$", fontsize=20, usetex=True, ha='center', va='center')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas.draw()

    def plot_equation(self, event=None):

        self.ax.cla()
        self.ax.axis('off')

        # Solicitar la ecuación al usuario
        equation = self.equation_entry.get()

        if equation == '':
            self.ax.text(0.5, 0.5, "$f(x):$", fontsize=20, usetex=True, ha='center', va='center')
        else:
            try:
                expr = sym.sympify(equation)  # Convertir la cadena de entrada en una expresión sympy
            except sym.SympifyError:
                return

            self.ax.text(0.5, 0.5, f"$f(x): {sym.latex(expr)}$", fontsize=20, usetex=True, ha='center', va='center')

        # Actualizar el lienzo de Matplotlib en la ventana de Tkinter
        self.canvas.figure = self.fig
        self.canvas.draw()


# Crear la ventana principal
root = tk.Tk()
root.title("Gráfico de ecuación")
root.geometry("600x400")

# Crear la ventana de gráfico
plot_window = PlotWindow(root)

# Iniciar la ventana principal
root.mainloop()
