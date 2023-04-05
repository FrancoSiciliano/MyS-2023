import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sym
import tkinter as tk

class PlotWindow:
    def __init__(self, root):
        self.root = root
        self.canvas = None

        font = ('TkDefaultFont', 12)
        equation_label = tk.Label(root, font=font, text="Ingrese la integral :")
        equation_label.pack()

        self.equation_entry = tk.Entry(root, width=50)
        self.equation_entry.pack()
        self.equation_entry.bind('<KeyRelease>', self.plot_equation)

        # Botones para agregar funciones
        function_frame = tk.Frame(root)
        function_frame.pack(pady=10)

        plus_button = tk.Button(function_frame, text='+', font=font, command=lambda: self.add_function('+'))
        plus_button.pack(side=tk.LEFT, padx=5)

        minus_button = tk.Button(function_frame, text='-', font=font, command=lambda: self.add_function('-'))
        minus_button.pack(side=tk.LEFT, padx=5)

        multiply_button = tk.Button(function_frame, text='*', font=font, command=lambda: self.add_function('*'))
        multiply_button.pack(side=tk.LEFT, padx=5)

        divide_button = tk.Button(function_frame, text='/', font=font, command=lambda: self.add_function('/'))
        divide_button.pack(side=tk.LEFT, padx=5)

        pow_button = tk.Button(function_frame, text='^', font=font, command=lambda: self.add_function('^'))
        pow_button.pack(side=tk.LEFT, padx=5)

        sqrt_button = tk.Button(function_frame, text='√x', font=font, command=lambda: self.add_function('sqrt(x)'))
        sqrt_button.pack(side=tk.LEFT, padx=5)

        cubic_button = tk.Button(function_frame, text='∛x', font=font, command=lambda: self.add_function('x^(1/3)'))
        cubic_button.pack(side=tk.LEFT, padx=5)

        sin_button = tk.Button(function_frame, text='sin(x)', font=font, command=lambda: self.add_function('sin(x)'))
        sin_button.pack(side=tk.LEFT, padx=5)

        cos_button = tk.Button(function_frame, text='cos(x)', font=font, command=lambda: self.add_function('cos(x)'))
        cos_button.pack(side=tk.LEFT, padx=5)

        tg_button = tk.Button(function_frame, text='tan(x)', font=font, command=lambda: self.add_function('tan(x)'))
        tg_button.pack(side=tk.LEFT, padx=5)

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

    def add_function(self, function):
        current_equation = self.equation_entry.get()
        if current_equation == '':
            self.equation_entry.insert(tk.END, function)
        else:
            self.equation_entry.delete(0, tk.END)
            self.equation_entry.insert(tk.END, current_equation + function)
        self.plot_equation()


