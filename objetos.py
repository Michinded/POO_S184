from Personaje import *

#1.Solicitar datos
print("Ingrese los datos del personaje")
print("##### datos personaje #####")
especieH = input("Escribe la especie del heroe: ")
nombreH = input("Escribe el nombre del heroe: ")
alturaH = float(input("Escribe la altura del heroe: "))
recargarH = int(input("Escribe la cantidad de municiones a recargar al heroe: "))

print("")
print("##### datos villano #####")
especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
alturaV = float(input("Escribe la altura del villano: "))
recargarV = int(input("Escribe la cantidad de municiones a recargar al villano: "))

# 2. Crear un objeto de la clase Personaje
heroe = Personaje(especieH, nombreH, alturaH)
villano = Personaje(especieV, nombreV, alturaV)


# 3. Usar atributos

print("")
print("##### objeto heroe #####")
print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie: " + heroe.especie)
print("Y tiene una altura de: " + str(heroe.altura))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(87)

print("")
print("##### objeto villano #####")
print("El personaje se llama: " + villano.nombre)
print("Pertenece a la especie: " + villano.especie)
print("Y tiene una altura de: " + str( villano.altura))

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargarV)