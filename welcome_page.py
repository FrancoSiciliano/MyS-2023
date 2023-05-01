import tkinter as tk
from frontpvi import PlotWindow as pvi
from frontintegracion import PlotWindow as integracion


class RadioButtonsGUI:

    def __init__(self, master):
        self.master = master
        master.title("Bienvenido")

        self.selection = tk.StringVar()

        self.a_label = tk.Label(master, text="Seleccione que tipo de problema desea resolver:")
        self.a_label.pack(pady=20)

        self.rb1 = tk.Button(master, text="Integración Numerica", width=25, height=2, command=self.integracion_numerica)
        self.rb1.pack(pady=10)

        self.rb2 = tk.Button(master, text="Problema de Valor Inicial", width=25, height=2, command=self.pvi)
        self.rb2.pack(pady=10)

    def pvi(self):
        pvi_window = tk.Tk()
        pvi_window.title("PVI")
        pvi_window.geometry("600x800")
        pvi(pvi_window)
        pvi_window.mainloop()


    def integracion_numerica(self):
        integracion_window = tk.Tk()
        integracion_window.title("Integración")
        integracion_window.geometry("600x400")
        integracion(integracion_window)
        integracion_window.mainloop()

root = tk.Tk()
app = RadioButtonsGUI(root)
root.geometry("300x250")
root.mainloop()
