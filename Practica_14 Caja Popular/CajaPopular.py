import tkinter as tk
from tkinter import messagebox


class Cuenta:
    def __init__(self, numCuenta, titular, edad, saldo):
        self.__numCuenta = numCuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo

    def consultar(self):
        return self.__saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        else:
            return False

class Programa:
    def __init__(self):
        self.__cuentas = []
        self.__saldo = 0

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)
        self.__saldo += cuenta.consultar()

    def consultar_saldo_total(self):
        return self.__saldo

    def buscar_cuenta(self, numCuenta):
        for cuenta in self.__cuentas:
            if cuenta._Cuenta__numCuenta == numCuenta:
                return cuenta
        return None

    def transferir(self, origen, destino, monto):
        if origen.retirar(monto):
            destino.depositar(monto)
            return True
        else:
            return False

    def mostrar_mensaje(mensaje):
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("Mensaje")
        ventana_emergente.geometry("200x100")

        etiqueta_mensaje = tk.Label(ventana_emergente, text=mensaje)
        etiqueta_mensaje.pack(pady=20)

        boton_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=ventana_emergente.destroy)
        boton_aceptar.pack(pady=10)

    def consultar_saldo(numCuenta):
        cuenta = self.buscar_cuenta(numCuenta)
        if cuenta:
            saldo = cuenta.consultar()
            mostrar_mensaje(f"El saldo de la cuenta {numCuenta} es: {saldo}")
        else:
            mostrar_mensaje(f"No se encontró la cuenta {numCuenta}")

    def depositar(numCuenta, monto):
        cuenta = self.buscar_cuenta(numCuenta)
        if cuenta:
            cuenta.depositar(monto)
            self.__saldo += monto
            mostrar_mensaje(f"Depósito realizado con éxito en la cuenta {numCuenta}")
        else:
            mostrar_mensaje(f"No se encontró la cuenta {numCuenta}")

    def retirar(numCuenta, monto):
        cuenta = self.buscar_cuenta(numCuenta)
        if cuenta:
            if cuenta.retirar(monto):
                self.__saldo -= monto
                mostrar_mensaje(f"Retiro realizado con éxito en la cuenta {numCuenta}")
            else:
                mostrar_mensaje(f"Saldo insuficiente en la cuenta {numCuenta}")
        else:
            mostrar_mensaje(f"No se encontró la cuenta {numCuenta}")

    def transferir_cuenta(origen, destino, monto):
        cuenta_origen = self.buscar_cuenta(origen)
        cuenta_destino = self.buscar_cuenta(destino)
        if cuenta_origen and cuenta_destino:
            if self.transferir(cuenta_origen, cuenta_destino, monto):
                mostrar_mensaje(f"Transferencia realizada con éxito de la cuenta {origen} a la cuenta {destino}")
            else:
                mostrar_mensaje(f"Saldo insuficiente en la cuenta {origen}")
        else:
            mostrar_mensaje(f"No se encontró alguna de las cuentas {origen} o {destino}")
    def interfaz(self):
        ventana = tk.Tk()
        ventana.title("Administración de Cuentas de Caja Popular")
        ventana.geometry("400x300")

        # Widgets de la interfaz
        etiqueta_titulo = tk.Label(ventana, text="Bienvenido al Programa de Administración de Cuentas de Caja Popular")
        etiqueta_titulo.pack(pady=10)

        etiqueta_numCuenta = tk.Label(ventana, text="Número de cuenta:")
        etiqueta_numCuenta.pack()

        entrada_numCuenta = tk.Entry(ventana, width=30)
        entrada_numCuenta.pack()

        etiqueta_monto = tk.Label(ventana, text="Monto:")
        etiqueta_monto.pack()

        entrada_monto = tk.Entry(ventana, width=30)
        entrada_monto.pack()

        boton_consultar = tk.Button(ventana, text="Consultar saldo", command=lambda: self.consultar_saldo(entrada_numCuenta.get()))
        boton_consultar.pack(pady=10)

        boton_depositar = tk.Button(ventana, text="Depositar", command=lambda: self.depositar(entrada_numCuenta.get(), float(entrada_monto.get())))
        boton_depositar.pack(pady=10)

        boton_retirar = tk.Button(ventana, text="Retirar", command=lambda: self.retirar(entrada_numCuenta.get(), float(entrada_monto.get())))
        boton_retirar.pack(pady=10)

        etiqueta_transferir = tk.Label(ventana, text="Transferir a otra cuenta:")
        etiqueta_transferir.pack()

        etiqueta_destino = tk.Label(ventana, text="Cuenta de destino:")
        etiqueta_destino.pack()

        entrada_destino = tk.Entry(ventana, width=30)
        entrada_destino.pack()

        boton_transferir = tk.Button(ventana, text="Transferir", command=lambda: self.transferir_cuenta(entrada_numCuenta.get(), entrada_destino.get(), float(entrada_monto.get())))
        boton_transferir.pack(pady=10)

        #Funciones de la interfaz


        ventana.mainloop()

if __name__ == "__main__":
    app = Programa()
    app.interfaz()
