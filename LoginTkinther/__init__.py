import datetime
import mysql.connector
from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
import Login
import SigIn

# Establecer la conexión con la base de datos
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="progpoo"
)

# Obtener el cursor de la conexión
cursor = conn.cursor()

#Crear la ventana
class LoginSignupWindow(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Login/Signup")
    self.geometry("300x200")
    seccion1 = Frame(self, bg="blue")
    seccion1.pack(expand=True, fill="both")

    # Widgets
    #Inicio Label
    welcome_label = tk.Label(seccion1, text="Bienvenido elija una opcion: Login/Signup", bg="blue", fg="white", font=("Arial", 12))
    welcome_label.pack(pady=10)

    #Login Button
    login_btn = tk.Button(seccion1, text="Login", command=self.show_login_form,bg="green", fg="white", font=("Arial", 12))
    login_btn.pack(pady=10)

    #Signup Button
    signup_btn = tk.Button(seccion1, text="Signup", command=self.show_signup_form, bg="red", fg="white", font=("Arial", 12))
    signup_btn.pack(pady=10)

  def show_login_form(self):
    # Implementar la ventana para el Login
    login_window = Login.LoginWindow()
    login_window.transient(self)
    login_window.grab_set()
    self.wait_window(login_window)


  def show_signup_form(self):
    # Implementar la ventana para el SignUp
    signup_window = SigIn.SignupWindow()
    signup_window.transient(self)
    signup_window.grab_set()
    self.wait_window(signup_window)


if __name__ == "__main__":
  app = LoginSignupWindow()
  app.mainloop()