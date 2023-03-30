import tkinter as tk
from tkinter import ttk, messagebox, BOTH, LEFT
from Logica import Logic


class GUI():
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Ventana con paneles")
        ventana.geometry("400x500")

        # Crea el notebook
        notebook = ttk.Notebook(ventana)

        # Crea el primer panel
        panel1 = ttk.Frame(notebook)
        notebook.add(panel1, text="Registrar usuario")

        # Crea el segundo panel
        panel2 = ttk.Frame(notebook)
        notebook.add(panel2, text="Buscar usuario")

        # Crea el tercer panel
        panel3 = ttk.Frame(notebook)
        notebook.add(panel3, text="Actualizar usuario")

        # Crea el cuarto panel
        panel4 = ttk.Frame(notebook)
        notebook.add(panel4, text="Eliminar usuario")

        # Agrega contenido a cada panel
        # Panel 1
        self.labelp1 = tk.Label(panel1, text="Registrar nuevo usuario")
        self.labelp1.pack(padx=10, pady=10)

        self.labelp1 = tk.Label(panel1, text="Nombre")
        self.labelp1.pack(padx=10, pady=10)

        self.nombre_entry_p1 = tk.Entry(panel1)
        self.nombre_entry_p1.pack(padx=10, pady=5)

        self.labelp1 = tk.Label(panel1, text="Email")
        self.labelp1.pack(padx=10, pady=10)

        self.email_entry_p1 = tk.Entry(panel1)
        self.email_entry_p1.pack(padx=10, pady=5)

        self.labelp1 = tk.Label(panel1, text="Contraseña")
        self.labelp1.pack(padx=10, pady=10)

        self.password_entry_p1 = tk.Entry(panel1)
        self.password_entry_p1.pack(padx=10, pady=5)

        self.boton = tk.Button(panel1, text="Registrar", command=self.agregar)
        self.boton.pack(padx=10, pady=10)

        # Panel 2
        self.label2 = tk.Label(panel2, text="Buscar usuario por email o id")
        self.label2.pack(padx=10, pady=10)

        self.label2 = tk.Label(panel2, text="Email o id del usuario a buscar")
        self.label2.pack(padx=10, pady=10)

        self.label_mail_p2 = tk.Label(panel2, text="Email")
        self.label_mail_p2.pack(padx=10, pady=10)

        self.data_email_entry_p2 = tk.Entry(panel2)
        self.data_email_entry_p2.pack(padx=10, pady=5)

        self.label_id_p2 = tk.Label(panel2, text="Id")
        self.label_id_p2.pack(padx=10, pady=10)

        self.data_id_entry_p2 = tk.Entry(panel2)
        self.data_id_entry_p2.pack(padx=10, pady=5)

        self.boton = tk.Button(panel2, text="Buscar", command=self.buscar)
        self.boton.pack(padx=10, pady=10)

        #Agregar textbox para mostrar los datos y hacer scrollable
        #Scrollbar
        self.scrollbar = tk.Scrollbar(panel2)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #Textbox
        self.textbox = tk.Text(panel2, yscrollcommand=self.scrollbar.set)
        self.textbox.pack(padx=10, fill=BOTH)
        self.scrollbar.config(command=self.textbox.yview)







        # Empaqueta el notebook
        notebook.pack(expand=True, fill="both")


    #Funciones para validar los datos
    def comproboar_ingreso_de_datos(self):
        if self.email_entry_p1.get() == "" or self.password_entry_p1.get() == "" or self.nombre_entry_p1.get() == "":
            return False
        else:
            return True

    def formato_email(self, email):
        if "@" in email:
            return True
        else:
            return False


    def limpiar_campos(self):
        self.email_entry_p1.delete(0, tk.END)
        self.email_entry_p1.delete(0, tk.END)
        self.password_entry_p1.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showwarning(titulo, mensaje)

    #Conjunto de funciones para comunicarse con la logica
    #Funcion para registrar un usuario
    def agregar(self):
        nombre = self.nombre_entry_p1.get()
        email = self.email_entry_p1.get()
        password = self.password_entry_p1.get()
        #Comprobar que los campos no esten vacios
        if self.comproboar_ingreso_de_datos() == False:
            self.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        #Comprobar que el formato del email sea correcto
        if self.formato_email(email) == False:
            self.mostrar_mensaje("Error", "El formato del email es incorrecto")
            return
        #Registrar el usuario
        logica = Logic()
        logica.registar(nombre, email, password)
        #Limpiar los campos
        self.limpiar_campos()

    #Funcion para buscar un usuario
    def buscar(self):
        email = self.data_email_entry_p2.get()
        id = self.data_id_entry_p2.get()
        #Comprobar que los campos no esten vacios
        if email == "" and id == "":
            self.mostrar_mensaje("Error", "Ambos campos no pueden estar vacios")
            return
        #Buscar el usuario
        logica = Logic()
        resultados_busqueda = logica.buscar(id, email)

        #Limpiamos el textbox para que no se acumulen los resultados
        self.textbox.delete(1.0, tk.END)

        # Damos formato a los resultados
        for resultado in resultados_busqueda:
            mensaje = "ID: " + str(resultado[0]) + "\n" + "NOMBRE: " + str(resultado[1]) + "\n" + "EMAIL: " + str(
                resultado[2]) + "\n" + "\n"
            self.textbox.insert(tk.END, mensaje)

        #Limpiar los campos de busqueda
        self.data_email_entry_p2
        self.data_id_entry_p2






#inicializa la ventana
if __name__ == "__main__":
    ventana = tk.Tk()
    app = GUI(ventana)
    ventana.mainloop()

