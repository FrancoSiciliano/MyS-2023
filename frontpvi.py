import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sym
import tkinter as tk
from metodos.euler import AlgoritmoEuler
from metodos.euler_mejorado import AlgoritmoEulerMejorado


def validar_texto(texto):
    return (len(texto) <= 4 and texto.isnumeric()) or not texto


def validar_x0(texto):
    if not texto:
        return True

    try:
        float(texto)
        return True
    except ValueError:
        return False


class PlotWindow:
    def __init__(self, root):
        self.root = root
        self.canvas = None

        font = ('TkDefaultFont', 12)

        input_form = tk.Frame(root)
        input_form.pack()

        # elección de método
        method_input = tk.Frame(input_form)
        method_input.grid(row=0, column=0)
        self.opcion = tk.IntVar()

        label_method = tk.Label(method_input, text="Eliga el método de resolución: ", font=font)
        label_method.grid(row=0, column=0)

        rb_euler = tk.Radiobutton(method_input, text="Método de Euler", variable=self.opcion, value=1)
        rb_euler.grid(row=1, column=0)

        rb_euler_mejorado = tk.Radiobutton(method_input, text="Método de Euler mejorado", variable=self.opcion, value=2)
        rb_euler_mejorado.grid(row=2, column=0)

        # input de n
        input_frame = tk.Frame(input_form)
        input_frame.grid(row=1, column=0)

        label_n = tk.Label(input_frame, text="Número de intervalos: ", font=font)
        label_n.grid(row=0, column=0)

        self.entry_n = tk.Entry(input_frame, width=4, validate="key", validatecommand=(root.register(validar_texto), '%P'))
        self.entry_n.grid(row=0, column=1)

        # input de t
        input_frame_t = tk.Frame(input_form)
        input_frame_t.grid(row=2, column=0)

        label_b = tk.Label(input_frame_t, text="0 ≤ t ≤ ", font=font)
        label_b.grid(row=0, column=0)

        self.entry_b = tk.Entry(input_frame_t, width=4, validate="key", validatecommand=(root.register(validar_texto), '%P'))
        self.entry_b.grid(row=0, column=1)

        # input de x0
        input_frame_x0 = tk.Frame(input_form)
        input_frame_x0.grid(row=3, column=0)

        label_x0 = tk.Label(input_frame_x0, text="x(0) = ", font=font)
        label_x0.grid(row=0, column=0)

        self.entry_x0 = tk.Entry(input_frame_x0, validate="key", validatecommand=(root.register(validar_x0), '%P'))
        self.entry_x0.grid(row=0, column=1)

        # input ecuación
        equation_label = tk.Label(root, font=font, text="Ingrese la ecuación diferencial:")
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

        self.fig, self.ax = plt.subplots()
        self.ax.axis('off')
        self.ax.text(0.5, 0.5, "$f(x,t):$", fontsize=20, usetex=True, ha='center', va='center')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().config(width=600, height=50)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True, padx=10, pady=10)
        self.canvas.draw()

        #boton de calcular
        calcular_frame = tk.Frame(root)
        calcular_frame.pack()

        boton_calc = tk.Button(calcular_frame, text="Calcular", command=self.calcular)
        boton_calc.pack()

    def plot_equation(self, event=None):

        self.ax.cla()
        self.ax.axis('off')

        equation = self.equation_entry.get()

        if equation == '':
            self.ax.text(0.5, 0.5, "$f(x,t):$", fontsize=20, usetex=True, ha='center', va='center')
        else:
            try:
                expr = sym.sympify(equation)
            except sym.SympifyError:
                return

            self.ax.text(0.5, 0.5, f"$f(x,t): {sym.latex(expr)}$", fontsize=20, usetex=True, ha='center', va='center')

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

    def calcular(self):
        equation = self.equation_entry.get()
        metodo = self.opcion.get()
        x0 = self.entry_x0.get()
        b = self.entry_b.get()
        n = self.entry_n.get()

        if metodo == 1:
            euler = AlgoritmoEuler(equation, float(x0), int(b), int(n))
            euler.calcular()
            euler.graficar()
        else:
            euler_mejorado = AlgoritmoEulerMejorado(equation, float(x0), int(b), int(n))
            euler_mejorado.calcular()
            euler_mejorado.graficar()