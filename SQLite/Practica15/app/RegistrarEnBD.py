import sqlite3
import tkinter as ttk
from tkinter import messagebox

import fuckit
class Conexion():
    def __init__(self):
        self.conexion_establecida = False
        #creamos la conexion
        #Usamos try except para manejar los errores si no se puede conectar a la base de datos
        try:
            self.conexion = sqlite3.connect("db_practica15.db")
            self.cursor = self.conexion.cursor()
            self.conexion_establecida = True
        except:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            self.conexion_establecida = False

    def comprobar_tabla(self):
        self.existe = False
        #comprobamos si la tabla existe
        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='TBRegistros'")
        if self.cursor.fetchone()[0] == 1:
            self.existe = True
        else:
            self.existe = False

        # creamos la tabla si no existe
        if self.existe == False:
            self.crearTabla = "CREATE TABLE IF NOT EXISTS TBRegistros (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL)"
            self.cursor.execute(self.crearTabla)
            self.conexion.commit()
            self.existe = True
        return self.existe

    def ejecutar_consulta(self, consulta, valores=()):
        if (self.comprobar_tabla() == False):
            messagebox.showerror("Error", "No se pudo encontrar la tabla")
        else:
            self.cursor.execute(consulta, valores)
            self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()


