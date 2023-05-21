import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sym
import tkinter as tk
from metodos.rectangulos import AlgoritmoRectangulos
from metodos.trapecios import AlgoritmoTrapecios
from metodos.montecarlo import AlgoritmoMontecarlo
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


class Integracion(tk.Frame):
    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent
        self.parent.title("Integracion")

        self.canvas = None

        font = ('TkDefaultFont', 12)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        self.input_form = tk.Frame(self.main_frame)
        self.input_form.pack()

        def update_label_text():
            if self.opcion.get() == 3:
                label_n.config(text="Cantidad de puntos:    ")
            else:
                label_n.config(text="Número de intervalos: ")

        # elección de método
        method_input = tk.Frame(self.input_form)
        method_input.grid(row=0, column=0, sticky="w")
        self.opcion = tk.IntVar()

        label_method = tk.Label(method_input, text="Eliga el método de resolución: ", font=font)
        label_method.grid(row=0, column=0)

        rb_rectangulos = tk.Radiobutton(method_input, text="Método de los rectangulos", variable=self.opcion, value=1,command=update_label_text)
        rb_rectangulos.grid(row=1, column=0,sticky="w")

        rb_trapecios = tk.Radiobutton(method_input, text="Método de los trapecios", variable=self.opcion, value=2,command=update_label_text)
        rb_trapecios.grid(row=2, column=0,sticky="w")

        rb_montecarlo = tk.Radiobutton(method_input, text="Método de montecarlo", variable=self.opcion, value=3,command=update_label_text)
        rb_montecarlo.grid(row=3, column=0,sticky="w")


        # input de n
        input_frame = tk.Frame(self.input_form)
        input_frame.grid(row=1, column=0,sticky="w")

        label_n = tk.Label(input_frame, text="Número de intervalos: ", font=font)
        label_n.grid(row=0, column=0)

        self.entry_n = tk.Entry(input_frame, width=8, validate="key", validatecommand=(self.parent.register(validar_texto), '%P'))
        self.entry_n.grid(row=0, column=5,padx=20)

        # input de b
        input_frame_b = tk.Frame(self.input_form)
        input_frame_b.grid(row=2, column=0,sticky="w")

        label_b = tk.Label(input_frame_b, text="Límite superior b (hasta):", font=font)
        label_b.grid(row=0, column=0,sticky="w")

        self.entry_b = tk.Entry(input_frame_b, width=8, validate="key", validatecommand=(self.parent.register(validar_texto), '%P'))
        self.entry_b.grid(row=0, column=2,padx=3)

        # input de a
        input_frame_a = tk.Frame(self.input_form)
        input_frame_a.grid(row=3, column=0,sticky="w")

        label_a = tk.Label(input_frame_a, text="Límite inferior a (desde):", font=font)
        label_a.grid(row=0, column=0,sticky="w")

        self.entry_a = tk.Entry(input_frame_a, width=8, validate="key", validatecommand=(self.parent.register(validar_x0), '%P'))
        self.entry_a.grid(row=0, column=2,padx=6)

        # input ecuación
        equation_label = tk.Label(self.main_frame, font=font, text="Ingrese la funcion f(x):")
        equation_label.pack(anchor='w', padx=146)

        self.equation_entry = tk.Entry(self.main_frame, width=50)
        self.equation_entry.pack()
        self.equation_entry.bind('<KeyRelease>', self.plot_equation)

        # Botones para agregar funciones
        function_frame = tk.Frame(self.main_frame)
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
        self.ax.text(0.5, 0.5, "$f(x):$", fontsize=20, usetex=True, ha='center', va='center')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.get_tk_widget().config(width=600, height=50)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas.draw()

        #boton de calcular
        calcular_frame = tk.Frame(self.main_frame)
        calcular_frame.pack(pady=10)

        boton_calc = tk.Button(calcular_frame, text="Calcular", command=self.calcular, font=font)
        boton_calc.pack()

        boton_atras = tk.Button(calcular_frame, text="Atras", command=self.go_back, font=font)
        boton_atras.pack(pady=10)

    def go_back(self):
        self.main_frame.destroy()
        self.parent.go_back()

    def plot_equation(self, event=None):

        self.ax.cla()
        self.ax.axis('off')

        equation = self.equation_entry.get()

        if equation == '':
            self.ax.text(0.5, 0.5, "$f(x):$", fontsize=20, usetex=True, ha='center', va='center')
        else:
            try:
                expr = sym.sympify(equation)
            except sym.SympifyError:
                return

            self.ax.text(0.5, 0.5, f"$f(x): {sym.latex(expr)}$", fontsize=20, usetex=True, ha='center', va='center')

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
        a = self.entry_a.get()
        b = self.entry_b.get()
        n = self.entry_n.get()

        if metodo == 1:
            rectangulos = AlgoritmoRectangulos(equation, int(a), int(b), int(n))
            rectangulos.calcular_graficar()
        elif metodo == 2:
            trapecios = AlgoritmoTrapecios(equation, int(a), int(b), int(n))
            trapecios.calcular()
            trapecios.graficar()
        else:
            montecarlo = AlgoritmoMontecarlo(equation, int(a), int(b), int(n))
            montecarlo.calcular()
            montecarlo.graficar()

