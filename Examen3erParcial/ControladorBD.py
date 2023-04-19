import sqlite3
from tkinter import messagebox


class Conexion():
    def __init__(self):
        self.conexion_establecida = False
        # creamos la conexion
        # Usamos try except para manejar los errores de conexion
        try:
            self.conexion = sqlite3.connect("BD_Banco.db")
            self.cursor = self.conexion.cursor()
            self.conexion_establecida = True
        except:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            self.conexion_establecida = False

    def ingresar(self, no_cuenta, saldo):
        if (no_cuenta == "" or saldo == ""):
            messagebox.showerror("Error", "No se puede dejar campos vacios")
            return

        # Verificar que no exista la cuenta
        self.cursor.execute("SELECT * FROM TBCuentas WHERE NoCuenta = ?", (no_cuenta,))
        if self.cursor.fetchone() is not None:
            messagebox.showerror("Error", "El NoCuenta ya está registrado")
            return

        try:
            self.cursor.execute("INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)", (no_cuenta, saldo))
            self.conexion.commit()
            # Mostrar un mensaje de que se ingreso correctamente
            messagebox.showinfo("Informacion", "Cuenta ingresada correctamente")
        except:
            messagebox.showerror("Error", "No se pudo ingresar la cuenta")
            return

    def actualizar(self, no_cuenta, saldo):
        if (no_cuenta == "" or saldo == ""):
            messagebox.showerror("Error", "No se puede dejar campos vacios")
            return
        try:
            self.cursor.execute("SELECT * FROM TBCuentas WHERE NoCuenta = ?", (no_cuenta,))
            if (self.cursor.fetchone() == None):
                messagebox.showerror("Error", "No existe la cuenta")
                return
            self.cursor.execute("UPDATE TBCuentas SET Saldo = ? WHERE NoCuenta = ?", (saldo, no_cuenta))
            self.conexion.commit()
        except:
            messagebox.showerror("Error", "No se pudo actualizar la cuenta")
            return

    def consultar(self, no_cuenta):
        if (no_cuenta == ""):
            messagebox.showerror("Error", "Debe ingresar un numero de cuenta")
            return
        try:
            self.cursor.execute("SELECT * FROM TBCuentas WHERE no_cuenta = ?", (no_cuenta,))
            return self.cursor.fetchall()
        except:
            messagebox.showerror("Error", "No se pudo consultar la cuenta")
            return

    def cerrar_conexion(self):
        self.conexion.close()
