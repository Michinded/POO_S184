import hashlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import datetime
import ConectorBD
#import mysql.connector


#funcion para registar usuario
def registrar(username, fullname, email, password):
    fecha = datetime.datetime.now()
    if Duplicado(username, email):
        msgbox.showerror("Error", "El nombre de usuario o el email ya existe")
        return
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        sql = "INSERT INTO users (username, fullname, email, password, created_at) VALUES (%s, %s, %s, %s, %s)"
        val = (username, fullname, email, hashed_password, fecha)
        ConectorBD.cursor.execute(sql, val)
        ConectorBD.conn.commit()
        msgbox.showinfo("Informacion", "Registro exitoso")

#funcion para comprobar si el usuario ya existe
def Duplicado(username, email):
    sql = "SELECT * FROM users WHERE username = %s OR email = %s"
    val = (username, email)
    ConectorBD.cursor.execute(sql, val)
    result = ConectorBD.cursor.fetchall()
    if result:
        return True
    else:
        return False

#funcion para validar que no haya campos vacios
def validarCampos(username, email, fullname, password):
    if username == "" or email == "" or fullname == "" or password == "":
        return True
    else:
        return False

#validar que el email sea valido
def validarEmail(email):
    if "@" in email:
        return False
    else:
        return True

class SignupWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Signup")
        self.geometry("300x400")

        cbg = "#35D38B"
        clabel = "#35D38B"
        centry = "#65D1A0"

        # Widgets
        seccion1 = Frame(self, bg=cbg)
        seccion1.pack(expand=True, fill="both")

        username_lbl = tk.Label(seccion1, text="Username:", bg=cbg, fg="white", font=("Arial", 12))
        username_lbl.pack(pady=10)

        self.username_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.username_entry.pack()

        email_lbl = tk.Label(seccion1, text="Email:", bg=cbg, fg="white", font=("Arial", 12))
        email_lbl.pack(pady=10)

        self.email_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.email_entry.pack()

        fullname_lbl = tk.Label(seccion1, text="Full Name:", bg=cbg, fg="white", font=("Arial", 12))
        fullname_lbl.pack(pady=10)

        self.fullname_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.fullname_entry.pack()

        password_lbl = tk.Label(seccion1, text="Password (Minimo 8 carácteres):", bg=cbg, fg="white", font=("Arial", 12))
        password_lbl.pack(pady=10)

        self.password_entry = tk.Entry(seccion1, show="*", bg=centry, fg="white", font=("Arial", 12))
        self.password_entry.pack()

        signup_btn = tk.Button(seccion1, text="Signup", command=self.signup, bg="red", fg="white", font=("Arial", 12))
        signup_btn.pack(pady=10)

    def signup(self):
        # Obtener los datos del formulario
        username = self.username_entry.get()
        email = self.email_entry.get()
        fullname = self.fullname_entry.get()
        password = self.password_entry.get()
        # Convertir el email a minusculas
        email = email.lower()
        # Validar que no haya campos vacios
        if validarCampos(username, email, fullname, password):
            msgbox.showerror("Error", "Todos los campos son requeridos")
            return
        else:
            if len(password) < 8:
                msgbox.showerror("Error", "La contraseña debe tener al menos 8 caracteres")
                return
            if validarEmail(email):
                msgbox.showerror("Error", "Formato de Email invalido")
                return
            # Insertar el nuevo usuario en la tabla "users"
            registrar(username, fullname, email, password)
            # Cerrar ventana actual y volver a la ventana principal
            self.destroy()