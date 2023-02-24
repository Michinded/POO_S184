class Personaje:
    # definimios el constructor del personaje
    def __init__(self, esp, nom, alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt

    # Métodos Personaje
    def correr(self, status):
        if status:
            print("El personaje " + self.nombre + " está corriendo")
        else:
            print("El personaje " + self.nombre + " se detuvo")

    def lanzarGranadas(self):
        print("El personaje " + self.nombre + " lanzó una granada")

    def recargarArma(self, municiones):
        cargador = 10
        cargador += municiones
        print("El arma tiene " + str(cargador) + " balas")