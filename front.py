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

        # Crear el botón para generar el gráfico
        plot_button = tk.Button(root, text="Generar gráfico", command=self.plot_equation)
        plot_button.pack()

    def plot_equation(self, event=None):
        # Solicitar la ecuación al usuario
        equation = self.equation_entry.get()

        # Convertir la ecuación en una expresión de sympy
        x = sym.symbols('x')  # Crear el símbolo 'x' para la variable independiente
        expr = sym.sympify(equation)  # Convertir la cadena de entrada en una expresión sympy

        # Convertir la expresión de sympy a una expresión de LaTeX
        latex_expression = sym.latex(expr)

        # Crear el gráfico de la ecuación
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${latex_expression}$", fontsize=30, usetex=True)
        ax.axis('off')

        # Crear un lienzo de Matplotlib en la ventana de Tkinter
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        else:
            self.canvas.figure = fig
            self.canvas.draw_idle()


# Crear la ventana principal
root = tk.Tk()
root.title("Gráfico de ecuación")

# Crear la ventana de gráfico
plot_window = PlotWindow(root)

# Iniciar la ventana principal
root.mainloop()
