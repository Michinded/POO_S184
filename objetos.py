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

#defnie un nuevo nombre
#heroe.setNombre("PEPE")
print("")
print("##### objeto heroe #####")
print("El personaje se llama: " + heroe.getNombre())
print("Pertenece a la especie: " + heroe.getEspecie())
print("Y tiene una altura de: " + str(heroe.getAltura()))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargarH)
#Ejemplo de metodo privado
#heroe.__pensar()

print("")
print("##### objeto villano #####")
print("El personaje se llama: " + villano.getNombre())
print("Pertenece a la especie: " + villano.getEspecie())
print("Y tiene una altura de: " + str( villano.getAltura()))

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargarV)