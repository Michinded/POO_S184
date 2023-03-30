import tkinter as tk
import tkinter.ttk as ttk
from app import Ventana

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Ventana.GUI(ventana)
    ventana.mainloop()
