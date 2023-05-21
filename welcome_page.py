import tkinter as tk
from frontintegracion import Integracion
from frontpvi import PVI


class WelcomePage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title("Bienvenido")
        self.selection = tk.StringVar()
        font = ('TkDefaultFont', 12)

        self.a_label = tk.Label(self, text="Seleccione que tipo de problema desea resolver:", font=font)
        self.a_label.pack(pady=20, padx=15)

        self.rb1 = tk.Button(self, text="Integración Numérica", width=25, height=2, command=self.open_integracion, font=font)
        self.rb1.pack(pady=10, padx=10)

        self.rb2 = tk.Button(self, text="Problema de Valor Inicial", width=25, height=2, command=self.open_pvi, font=font)
        self.rb2.pack(pady=10, padx=10)

    def open_integracion(self):
        integracion_frame = Integracion(self.parent)
        self.parent.switch_frame(integracion_frame)

    def open_pvi(self):
        pvi_frame = PVI(self.parent)
        self.parent.switch_frame(pvi_frame)
