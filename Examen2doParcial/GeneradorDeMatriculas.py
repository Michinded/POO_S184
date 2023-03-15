import random
from tkinter import *
import datetime
from tkinter import messagebox


class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Menú")
        master.geometry("400x600")

        self.label = Label(master, text="Programa generador de matrículas")
        self.label.pack(pady=10)

        self.label_Info = Label(master, text="Imgrese los datos para generar su matrícula")
        self.label_Info.pack(pady=5)

        self.label_Name = Label(master, text="Nombre:")
        self.label_Name.pack(pady=10)

        self.entry_Name = Entry(master, width=50)
        self.entry_Name.pack(pady=5)

        self.label_ApellidoPaterno = Label(master, text="Apellido Paterno:")
        self.label_ApellidoPaterno.pack(pady=10)

        self.entry_AppellidoPaterno = Entry(master, width=50)
        self.entry_AppellidoPaterno.pack(pady=5)

        self.label_ApellidoMaterno = Label(master, text="Apellido Materno:")
        self.label_ApellidoMaterno.pack(pady=10)

        self.entry_AppellidoMaterno = Entry(master, width=50)
        self.entry_AppellidoMaterno.pack(pady=5)

        self.label_anioNacimiento = Label(master, text="Año de nacimiento:")
        self.label_anioNacimiento.pack(pady=10)

        self.entry_anioNacimiento = Entry(master, width=50)
        self.entry_anioNacimiento.pack(pady=5)

        self.label_Carrera = Label(master, text="Carrera:")
        self.label_Carrera.pack(pady=10)

        self.entry_Carrera = Entry(master, width=50)
        self.entry_Carrera.pack(pady=5)

        self.label = Label(master, text="Presiona Generar para generar tu matricula")
        self.label.pack(pady=10)

        self.Label_Matricula = Entry(master, text="", width=50)
        self.Label_Matricula.pack(pady=10)

        self.open_button = Button(master, text="Generar", command=self.generarMatricula)
        self.open_button.pack(pady=5)

        self.quit_button = Button(master, text="Salir", command=master.quit)
        self.quit_button.pack(pady=15)


    def generarMatricula(self):
        #Obtener datos
        anioActual = datetime.datetime.now().year
        anioNacimiento = (self.entry_anioNacimiento.get())
        nombre = self.entry_Name.get()
        apellidoPaterno = self.entry_AppellidoPaterno.get()
        apellidoMaterno = self.entry_AppellidoMaterno.get()
        carrera = self.entry_Carrera.get()

        #comprombar que los datos no esten vacios
        if anioNacimiento == "" or nombre == "" or apellidoPaterno == "" or apellidoMaterno == "" or carrera == "":
            messagebox.showerror("Error", "Favor de llenar todos los campos")
            return

        #tomar ultimos dos digitos del año actual
        anioActual = str(anioActual)
        anioActual = anioActual[-2:]
        #tomar ultimos dos digitos del año de nacimiento
        anioNacimiento = anioNacimiento[-2:]
        #tomar primera letra del nombre
        nombre = nombre[0]
        nombre = nombre.upper()
        #tomar primeras 3 letras del apellido paterno
        apellidoPaterno = apellidoPaterno[0:3]
        apellidoPaterno = apellidoPaterno.upper()
        #tomar primeras 3 letras del apellido materno
        apellidoMaterno = apellidoMaterno[0:3]
        apellidoMaterno = apellidoMaterno.upper()
        #tomar primeras 3 letras de la carrera
        carrera = carrera[0:3]
        carrera = carrera.upper()
        #Generar 3 numeros aleatorios
        numerosAleatorios = random.randint(100, 999)


        #Concatenar datos [carrera][anioActual][anioNacimiento][nombre][apellidoPaterno][apellidoMaterno][numerosAleatorios]
        matricula = carrera + anioActual + anioNacimiento + nombre + apellidoPaterno + apellidoMaterno + str(numerosAleatorios)

        #Mostrar matricula
        messagebox.showinfo("Matricula", f"Su matrícula es \n{matricula}")
        self.Label_Matricula.delete(0, END)
        self.Label_Matricula.insert(0, matricula)

if __name__ == '__main__':
    root = Tk()
    my_menu = Menu(root)
    root.mainloop()
