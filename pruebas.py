import sympy as sp
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy.printing import latex
import matplotlib.pyplot as plt

# Crear una ventana de GUI
ventana = tk.Tk()

# Establecer el tamaño de la ventana y centrarla en la pantalla
ventana.geometry('800x600+{}+{}'.format(int(ventana.winfo_screenwidth() / 2 - 800 / 2),
                                        int(ventana.winfo_screenheight() / 2 - 600 / 2)))

# Establecer el título de la ventana
ventana.title('Modelado y simulación')

# Pedir al usuario que ingrese la función
etiqueta = tk.Label(ventana, text="Ingrese una función matemática", font=("Arial", 16))
etiqueta.pack()

# Crear un campo de entrada con un tamaño de fuente grande
entrada_funcion = tk.Entry(ventana, font=("Arial", 14))
entrada_funcion.pack()


# Función para mostrar la función ingresada en la ventana
def mostrar_funcion():
    # Obtener la función ingresada por el usuario
    funcion = entrada_funcion.get()

    # Convertir la entrada del usuario en una expresión simbólica
    expr = sp.simplify(funcion)

    # Convertir la expresión simbólica en una cadena LaTeX
    cadena_funcion = r"${}$".format(latex(expr))

    # Crear una figura de matplotlib con la fórmula
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, cadena_funcion, fontsize=20, ha='center', va='center')
    ax.axis('off')

    # Mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Botón para mostrar la función ingresada por el usuario
boton_mostrar = tk.Button(ventana, text="Mostrar función", command=mostrar_funcion)
boton_mostrar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
