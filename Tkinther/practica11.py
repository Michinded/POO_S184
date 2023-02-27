from tkinter import Tk, Button, Frame, messagebox

#Funcion que se ejecuta al presionar el boton azul
def mostrarMensaje():
    messagebox.showinfo("Aviso", "Se ha presionado el boton azul")

#1. Instanciar la ventana
ventana = Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2. Crear los frames
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True, fill="both")

seccion2 = Frame(ventana, bg="blue")
seccion2.pack(expand=True, fill="both")

seccion3 = Frame(ventana, bg="black")
seccion3.pack(expand=True, fill="both")

#3. Crear los botones
botonAzul = Button(seccion1, text="Boton Azul", fg="white", bg="blue", command=mostrarMensaje)
botonAzul.place(x="60", y="60")


botonNegro = Button(seccion2, text="Boton Negro", fg="white", bg="black")
botonNegro.grid(row = 0, column = 0)

botonAmarrillo = Button(seccion2, text="Boton Amarillo", fg="black", bg="yellow")
botonAmarrillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text="Boton Verde", fg="black", bg="green")
botonVerde.configure(width=10, height=2)
botonVerde.pack()

#Llamamos a ejecutar el metodo mainloop
ventana.mainloop()