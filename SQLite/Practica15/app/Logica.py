#Aqui se reciben los datos de la ventana y se llama a RegistrarEnBD.py para que los guarde en la base de datos
#Importamos la clase Conexion
from RegistrarEnBD import Conexion
#importamos el messagebox de tkinter
from tkinter import messagebox
#importamos bdcrypt para encriptar la contraseña
import bcrypt
class Logic():
    def registar(self, nombre, email, password):
        conexion = Conexion()
        #encriptamos la contraseña
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        #el id se autoincrementa
        consulta = "INSERT INTO TBRegistros (nombre, email, password) VALUES (?, ?, ?)"
        valores = (nombre, email, password)
        conexion.ejecutar_consulta(consulta, valores)
        conexion.cerrar_conexion()
        messagebox.showinfo("Registro", "Registro exitoso")

    def buscar(self, id, email):
        conexion = Conexion()
        if id == "":
            consulta_tipo_1 = "SELECT * FROM TBRegistros WHERE email = ?"
            valores = (email,)
        elif email == "":
            consulta_tipo_1 = "SELECT * FROM TBRegistros WHERE id = ?"
            valores = (id,)
        else:
            consulta_tipo_1 = "SELECT * FROM TBRegistros WHERE id = ? OR email = ?"
            valores = (id, email)

        cursor = conexion.cursor
        cursor.execute(consulta_tipo_1, valores)
        resultados = cursor.fetchall()
        conexion.cerrar_conexion()

        if len(resultados) == 0:
            messagebox.showerror("Error", "No se encontró ningún usuario con los datos especificados")
            return

        mensaje = ""
        for fila in resultados:
            mensaje += f"ID: {fila[0]}\n"
            mensaje += f"Nombre: {fila[1]}\n"
            mensaje += f"Email: {fila[2]}\n"

        messagebox.showinfo("Resultados", mensaje)

    def actualizar(self, id, nombre, email, password):
        conexion = Conexion()
        consulta = "UPDATE TBRegistros SET nombre = ?, email = ?, password = ? WHERE id = ?"
        valores = (nombre, email, password, id)
        conexion.ejecutar_consulta(consulta, valores)
        conexion.cerrar_conexion()

    def eliminar(self, id):
        conexion = Conexion()
        consulta = "DELETE FROM TBRegistros WHERE id = ?"
        valores = (id,)
        conexion.ejecutar_consulta(consulta, valores)
        conexion.cerrar_conexion()

    #def enviar_dato_a_ventana(self, valores=()):

