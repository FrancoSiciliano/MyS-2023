import tkinter as tk

ventana = tk.Tk()
ventana.title("Seleccione un metodo")
def boton_clicado():
    print("¡El botón ha sido clicado!")

boton1 = tk.Button(ventana, text="Botón 1", command=boton_clicado)
boton2 = tk.Button(ventana, text="Botón 2", command=boton_clicado)
boton3 = tk.Button(ventana, text="Botón 3", command=boton_clicado)
boton4 = tk.Button(ventana, text="Botón 4", command=boton_clicado)
boton5 = tk.Button(ventana, text="Botón 5", command=boton_clicado)

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=1, column=0)
boton4.grid(row=1, column=1)
boton5.grid(row=2, column=0, columnspan=2)

ventana.mainloop()