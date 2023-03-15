import tkinter as tk
from tkinter import messagebox

class Cuenta:
    def init(self, numCuenta, titular, edad, saldo):
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
    def init(self):
        self.__cuentas = []
        self.__saldo = 0
