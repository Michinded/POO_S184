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
        #Verificamos que el correo no este registrado
        consulta_tipo_1 = "SELECT * FROM TBRegistros WHERE email = ?"
        valores = (email,)
        cursor = conexion.cursor
        cursor.execute(consulta_tipo_1, valores)
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            messagebox.showerror("Error", "El correo ya esta registrado")
            return
        #insertamos los datos en la base de datos
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
        try:
            cursor = conexion.cursor
            cursor.execute(consulta_tipo_1, valores)
            resultados = cursor.fetchall()
            conexion.cerrar_conexion()
        except:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos o error en la consulta")
            return

        if len(resultados) != 0:
            return resultados

        #enviamos los datos a la ventana retornando una lista con los datos


    def actualizar(self, id, nombre, email):
        conexion = Conexion()
        # Validar que el correo no este registrado en otro usuario
        consulta_tipo_1 = "SELECT * FROM TBRegistros WHERE email = ? AND id != ?"
        valores1 = (email, id)
        cursor = conexion.cursor
        cursor.execute(consulta_tipo_1, valores1)
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            messagebox.showerror("Error", "El correo ya esta registrado para otro usuario")
            return
        else:
            # Validar que se ejecute la consulta
            #Validar si solo se actualizo el nombre o el correo
            if nombre == "" and email != "":
                #Si solo se actualizo el correo
                consulta_tipo_2 = "UPDATE TBRegistros SET email = ? WHERE id = ?"
                valores2 = (email, id)
            elif nombre != "" and email == "":
                #Si solo se actualizo el nombre
                consulta_tipo_2 = "UPDATE TBRegistros SET nombre = ? WHERE id = ?"
                valores2 = (nombre, id)
            else:
                #Si se tienen los dos datos se actualizan los dos
                consulta_tipo_2 = "UPDATE TBRegistros SET nombre = ?, email = ? WHERE id = ?"
                valores2 = (nombre, email, id)
            try:
                conexion.ejecutar_consulta(consulta_tipo_2, valores2)
                if cursor.rowcount == 0:
                    messagebox.showinfo("Actualización", "No se realizó ningún cambio en el registro")
                else:
                    messagebox.showinfo("Actualización", "Actualización exitosa")
            except:
                messagebox.showerror("Error", "No se pudo actualizar el registro")
        conexion.cerrar_conexion()

    def eliminar(self, id):
        conexion = Conexion()
        try:
            consulta = "DELETE FROM TBRegistros WHERE id = ?"
            valores = (id,)
            conexion.ejecutar_consulta(consulta, valores)
            conexion.cerrar_conexion()
            messagebox.showinfo("Eliminación", "Eliminación exitosa")
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro o no existe")

    #def enviar_dato_a_ventana(self, valores=()):

    #Listar todos los usuarios
    def listar(self):
        conexion = Conexion()
        consulta = "SELECT * FROM TBRegistros"
        try:
            cursor = conexion.cursor
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            conexion.cerrar_conexion()
        except:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos o error en la consulta")
            return
        if len(resultados) != 0:
            return resultados


