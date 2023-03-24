import tkinter as tk
import tkinter.ttk as ttk
from SQLite.Practica15.app.Ventana import Ventana
from SQLite.Practica15.app import Logica

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Ventana(ventana)
    ventana.mainloop()
