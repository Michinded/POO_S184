import tkinter as tk
from tkinter import ttk, messagebox, BOTH, LEFT
from Logica import Logic


class GUI():
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Ventana con paneles")
        ventana.geometry("550x450")

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

        # Crea el quinto panel
        panel5 = ttk.Frame(notebook)
        notebook.add(panel5, text="Listar todos los usuarios")

        # Agrega contenido a cada panel
        # Panel 1 Registrar nuevo usuario
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

        #La contraseña no se muestra en pantalla
        self.labelp1 = tk.Label(panel1, text="Contraseña")
        self.labelp1.pack(padx=10, pady=10)

        #Ocultamos la contraseña
        self.password_entry_p1 = tk.Entry(panel1, show="*")
        self.password_entry_p1.pack(padx=10, pady=5)

        #Confirmamos la contraseña
        self.labelp1 = tk.Label(panel1, text="Confirmar contraseña")
        self.labelp1.pack(padx=10, pady=10)

        #Ocultamos la contraseña
        self.password_entry_p1_2 = tk.Entry(panel1, show="*")
        self.password_entry_p1_2.pack(padx=10, pady=5)

        #Checkbutton para mostrar la contraseña
        self.mostrar = tk.IntVar()
        self.check = tk.Checkbutton(panel1, text="Mostrar contraseña", variable=self.mostrar, command=self.mostrar_contrasena)
        self.check.pack(padx=10, pady=10)

        self.boton = tk.Button(panel1, text="Registrar", command=self.agregar)
        self.boton.pack(padx=10, pady=10)

        # Panel 2 Buscar usuario
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
        self.textbox.pack(padx=10, pady=10, fill=BOTH)
        self.scrollbar.config(command=self.textbox.yview)

        # Panel 3 Actualizar usuario
        self.label3 = tk.Label(panel3, text="Actualizar usuario")
        self.label3.pack(padx=10, pady=10)

        self.label3 = tk.Label(panel3, text="Id del usuario a actualizar")
        self.label3.pack(padx=10, pady=10)

        self.data_id_entry_p3 = tk.Entry(panel3)
        self.data_id_entry_p3.pack(padx=10, pady=5)

        self.label3 = tk.Label(panel3, text="Nuevo nombre")
        self.label3.pack(padx=10, pady=10)

        self.new_name_entry_p3 = tk.Entry(panel3)
        self.new_name_entry_p3.pack(padx=10, pady=5)

        self.label3 = tk.Label(panel3, text="Nuevo email")
        self.label3.pack(padx=10, pady=10)

        self.new_email_entry_p3 = tk.Entry(panel3)
        self.new_email_entry_p3.pack(padx=10, pady=5)

        self.label3 = tk.Label(panel3, text="Nueva contraseña")
        self.label3.pack(padx=10, pady=10)

        self.new_password_entry_p3 = tk.Entry(panel3)
        self.new_password_entry_p3.pack(padx=10, pady=5)

        self.label3 = tk.Label(panel3, text="Nota: Si no desea actualizar algun campo, deje el campo en blanco.")
        self.label3.pack(padx=10, pady=10)

        #Boton
        self.boton = tk.Button(panel3, text="Actualizar", command=self.actualizar)
        self.boton.pack(padx=10, pady=10)

        # Panel 4 Eliminar usuario
        self.label4 = tk.Label(panel4, text="Eliminar usuario")
        self.label4.pack(padx=10, pady=10)

        self.label4 = tk.Label(panel4, text="Id del usuario a eliminar")
        self.label4.pack(padx=10, pady=10)

        self.data_id_entry_p4 = tk.Entry(panel4)
        self.data_id_entry_p4.pack(padx=10, pady=5)

        #Mostar casilla de confirmacion
        self.confirmacion = tk.IntVar()
        self.check = tk.Checkbutton(panel4, text="Confirmar eliminación", variable=self.confirmacion)
        self.check.pack(padx=10, pady=10)

        self.boton = tk.Button(panel4, text="Eliminar", command=self.eliminar)
        self.boton.pack(padx=10, pady=10)

        # Panel 5 Listar usuarios
        self.label5 = tk.Label(panel5, text="Listar usuarios")
        self.label5.pack(padx=10, pady=10)

        self.boton = tk.Button(panel5, text="Listar", command=self.listar)
        self.boton.pack(padx=10, pady=10)

        # Crear Treeview
        self.treeview = ttk.Treeview(panel5, columns=('id', 'nombre', 'email'), show='headings')
        self.treeview.heading('id', text='ID')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('email', text='Email')
        self.treeview.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Scrollbar
        self.scrollbar2 = tk.Scrollbar(panel5)
        self.scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.treeview.yview)

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
        self.nombre_entry_p1.delete(0, tk.END)
        self.email_entry_p1.delete(0, tk.END)
        self.email_entry_p1.delete(0, tk.END)
        self.password_entry_p1.delete(0, tk.END)
        self.password_entry_p1_2.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showwarning(titulo, mensaje)

    #Conjunto de funciones para comunicarse con la logica
    #Funcion para registrar un usuario
    def agregar(self):
        nombre = self.nombre_entry_p1.get()
        email = self.email_entry_p1.get()
        password = self.password_entry_p1.get()
        password2 = self.password_entry_p1_2.get()
        #Comprobar que los campos no esten vacios
        if self.comproboar_ingreso_de_datos() == False:
            self.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        #Comprobar que el formato del email sea correcto
        if self.formato_email(email) == False:
            self.mostrar_mensaje("Error", "El formato del email es incorrecto")
            return
        #Comprobar que las contraseñas coincidan
        if password != password2:
            self.mostrar_mensaje("Error", "Las contraseñas no coinciden")
            return
        #castear el email a minusculas
        email = email.lower()
        #Registrar el usuario
        logica = Logic()
        logica.registar(nombre, email, password)
        #Limpiar los campos
        self.limpiar_campos()

    #Funcion para mostrar la contraseña
    def mostrar_contrasena(self):
        if self.password_entry_p1["show"] == "*" and self.password_entry_p1_2["show"] == "*":
            self.password_entry_p1["show"] = ""
            self.password_entry_p1_2["show"] = ""
        else:
            self.password_entry_p1["show"] = "*"
            self.password_entry_p1_2["show"] = "*"

    #Funcion para buscar un usuario
    def buscar(self):
        email = self.data_email_entry_p2.get()
        id = self.data_id_entry_p2.get()

        #Comprobar que los campos no esten vacios
        if email == "" and id == "":
            self.mostrar_mensaje("Error", "Ambos campos no pueden estar vacios")
            return

        # Limpiamos el textbox para que no se acumulen los resultados
        self.textbox.delete(1.0, tk.END)
        #Buscar el usuario
        logica = Logic()
        if logica.buscar(id, email) != None:
            resultados = logica.buscar(id, email)
            # Damos formato a los resultados
            contador = 0
            for resultado in resultados:
                mensaje = "ID: " + str(resultado[0]) + "\n" + "NOMBRE: " + str(resultado[1]) + "\n" + "EMAIL: " + str(
                    resultado[2]) + "\n" + "\n"
                contador += 1
                self.textbox.insert(tk.END, f"Coincidencias #{contador}\n" + mensaje)
        else:
            self.mostrar_mensaje("Error", "No se encontro ningun usuario con esos datos")
            return


        #Limpiar los campos de busqueda
        self.data_email_entry_p2
        self.data_id_entry_p2

    #Funciones para actualizar un usuario
    def actualizar(self):
        id = self.data_id_entry_p3.get()
        new_name = self.new_name_entry_p3.get()
        new_email = self.new_email_entry_p3.get()
        new_password = self.new_password_entry_p3.get()
        #Comprobar que todos los campos no esten vacios
        if id == "" and new_name == "" and new_email == "" and new_password == "":
            self.mostrar_mensaje("Error", "Debe ingresar el id y al menos un dato para actualizar")
            return

        #Comprobar que el id no este vacio
        if id == "":
            self.mostrar_mensaje("Error", "El id es obligatorio")
            return
        if new_name == "" and new_email == "" and new_password == "":
            self.mostrar_mensaje("Error", "Debe ingresar al menos un dato para actualizar")
            return

        #Comprobar que el formato del email sea correcto
        if self.formato_email(new_email) == False and new_email != "":
            self.mostrar_mensaje("Error", "El formato del email es incorrecto")
            return
        #Comprobar que el id sea un numero
        try:
            id = int(id)
        except:
            self.mostrar_mensaje("Error", "El id debe ser un numero")
            return

        if new_name != "" and new_email != "" and new_password != "":
            # Castear el email a minusculas
            new_email = new_email.lower()
            #Actualizar nombre email y contraseña
            self.mostrar_mensaje("Advertencia", "Se actualizara el nombre, email y contraseña")
            logica = Logic()
            logica.actualizar(id, new_name, new_email, new_password)

        elif new_name != "" and new_email == "" and new_password == "":
            #Actualizar solo el nombre
            self.mostrar_mensaje("Advertencia", "Se actualizara el nombre")
            logica = Logic()
            new_email = ""
            new_password = ""
            logica.actualizar(id, new_name, new_email, new_password)
        elif new_name == "" and new_email != "" and new_password == "":
            #Castear el email a minusculas
            new_email.lower()
            new_name = ""
            new_password = ""
            #Actualizar solo el email
            self.mostrar_mensaje("Advertencia", "Se actualizara el email")
            logic = Logic()
            logic.actualizar(id, new_name, new_email, new_password)

        elif new_name == "" and new_email == "" and new_password != "":
            #Actualizar solo la contraseña
            self.mostrar_mensaje("Advertencia", "Se actualizara la contraseña")
            new_name = ""
            new_email = ""
            logica = Logic()
            logica.actualizar(id, new_name, new_email, new_password)
        else:
            #Actualizar nombre y email
            self.mostrar_mensaje("Advertencia", "Se actualizara el nombre y el email")
            new_password = ""
            new_email = new_email.lower()
            logica = Logic()
            logica.actualizar(id, new_name, new_email, new_password)




        #Limpiar los campos
        self.data_id_entry_p3.delete(0, tk.END)
        self.new_name_entry_p3.delete(0, tk.END)
        self.new_email_entry_p3.delete(0, tk.END)
        self.new_password_entry_p3.delete(0, tk.END)

    #Funcion para eliminar un usuario
    def eliminar(self):
        id = self.data_id_entry_p4.get()
        #Comprobar que el id no este vacio
        if id == "":
            self.mostrar_mensaje("Error", "El id es obligatorio")
            return
        #Comprobar que el id sea un numero
        try:
            id = int(id)
        except:
            self.mostrar_mensaje("Error", "El id debe ser un numero")
            return
        #Comprobar que se haya confirmado la eliminacion
        if self.confirmacion.get() == 0:
            self.mostrar_mensaje("Error", "Debe confirmar la eliminacion")
            return

        #Eliminar el usuario
        logica = Logic()
        logica.eliminar(id)

        #Limpiar los campos
        self.data_id_entry_p4.delete(0, tk.END)
        self.confirmacion.set(0)

    #Funcion para mostrar todos los usuarios
    def listar(self):
        logica = Logic()
        if logica.listar() == None:
            self.mostrar_mensaje("Error", "No hay usuarios registrados")
            return
        resultados = logica.listar()

        # Borrar todos los datos del Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Agregar resultados al Treeview
        for resultado in resultados:
            self.treeview.insert('', 'end', values=(resultado[0], resultado[1], resultado[2]))





#inicializa la ventana
if __name__ == "__main__":
    ventana = tk.Tk()
    app = GUI(ventana)
    ventana.mainloop()

