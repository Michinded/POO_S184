import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ControladorBD import Conexion


# Funcion para ingresar una cuenta
def ingresar_cuenta():
    # Obtener los datos de los entry
    no_cuenta = num_cuenta_ingresar.get()
    saldo = saldo_ingresar.get()

    # Llamar al metodo ingresar de la clase conexion
    try:
        conexion.ingresar(no_cuenta, saldo)
        # Limpiar los entry
        num_cuenta_ingresar.set("")
        saldo_ingresar.set("")
    except:
        messagebox.showerror("Error", "No se pudo ingresar la cuenta")


# Funcion para actualizar una cuenta
def actualizar_cuenta():
    # Obtener los datos de los entry
    no_cuenta = num_cuenta_actualizar.get()
    saldo = saldo_actualizar.get()

    # Llamar al metodo actualizar de la clase conexion
    try:
        conexion.actualizar(no_cuenta, saldo)
        # Limpiar los entry
        num_cuenta_actualizar.set("")
        saldo_actualizar.set("")
    except:
        messagebox.showerror("Error", "No se pudo actualizar la cuenta")



# Crear un objeto de la clase conexion
conexion = Conexion()

Ventana = tk.Tk()
Ventana.title("Banco")
Ventana.geometry("400x400")

# Crear un objeto de la clase Notebook
notebook = ttk.Notebook(Ventana)
notebook.pack(fill="both", expand=True)

panel1 = ttk.Frame(notebook)
notebook.add(panel1, text="Insertar")

panel2 = ttk.Frame(notebook)
notebook.add(panel2, text="Actualizar")

panel3 = ttk.Frame(notebook)
notebook.add(panel3, text="Consultar")

# Crear los widgets para el panel 1
labelt1 = ttk.Label(panel1, text="Insertar").pack(pady=5)

label1 = ttk.Label(panel1, text="Numero de cuenta")
label1.pack(pady=5)
num_cuenta_ingresar = tk.StringVar()
entry1 = ttk.Entry(panel1, textvariable=num_cuenta_ingresar).pack(pady=5)

label2 = ttk.Label(panel1, text="Saldo")
label2.pack(pady=5)

saldo_ingresar = tk.StringVar()
entry2 = ttk.Entry(panel1, textvariable=saldo_ingresar).pack(pady=5)

btn_ingresar = ttk.Button(panel1, text="Ingresar", command=ingresar_cuenta).pack(pady=5)

# Crear los widgets para el panel 2
labelt2 = ttk.Label(panel2, text="Actualizar").pack(pady=5)

label3 = ttk.Label(panel2, text="Numero de cuenta")
label3.pack(pady=5)
num_cuenta_actualizar = tk.StringVar()
entry3 = ttk.Entry(panel2, textvariable=num_cuenta_actualizar).pack(pady=5)

label4 = ttk.Label(panel2, text="Saldo")
label4.pack(pady=5)

saldo_actualizar = tk.StringVar()
entry4 = ttk.Entry(panel2, textvariable=saldo_actualizar).pack(pady=5)

btn_actualizar = ttk.Button(panel2, text="Actualizar", command=actualizar_cuenta).pack(pady=5)



Ventana.mainloop()


