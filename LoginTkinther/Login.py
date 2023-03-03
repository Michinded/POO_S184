import hashlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
#import mysql.connector
import ConectorBD

# Establecer la conexión con la base de datos

# Obtener el cursor de la conexión
#ConectorBD.cursor
def comprobarData(username, password):
    # Comprobar si el usuario existe
    # Comprobar si la contraseña es correcta
    # Mostrar mensaje de bienvenida y datos del usuario
    # Cerrar ventana actual y volver a la ventana principal
    success = False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    query = "SELECT username, email, fullname, created_at FROM users WHERE (username = %s OR email = %s) AND password = %s"
    ConectorBD.cursor.execute(query, (username, username, hashed_password))
    result = ConectorBD.cursor.fetchone()
    if result:
        success = True
        msgbox.showinfo("Bienvenido", f"Bienvenido Usuario: {result[0]}!\nSu email registrado es: {result[1]}\nSu nombre completo es: {result[2]}\nUsted Creo su cuenta en: {result[3]}")
    else:
        msgbox.showerror("Error", "Usuario o contraseña incorrectos")
        success = False


class LoginWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        #colores
        cbg = "#306AD1"
        clabel = "#35D38B"
        centry = "#5A87D6"


        # Widgets
        seccion1 = Frame(self, bg=cbg)
        seccion1.pack(expand=True, fill="both")

        username_lbl = tk.Label(seccion1, text="Username or Email:", bg=cbg, fg="white", font=("Arial", 12))
        username_lbl.pack(pady=10)

        self.username_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.username_entry.pack()

        password_lbl = tk.Label(seccion1, text="Password:", bg=cbg, fg="white", font=("Arial", 12))
        password_lbl.pack(pady=10)

        self.password_entry = tk.Entry(seccion1, show="*", bg=centry, fg="white", font=("Arial", 12))
        self.password_entry.pack()

        login_btn = tk.Button(seccion1, text="Login", command=self.login, bg="blue", fg="white", font=("Arial", 12))
        login_btn.pack(pady=10)

    def login(self):
        # Implementar la funcionalidad de login
        # Consultar la tabla "users" y verificar si el usuario existe y la contraseña es correcta
        username = self.username_entry.get()
        password = self.password_entry.get()
        comprobarData(username, password)
        self.destroy()


