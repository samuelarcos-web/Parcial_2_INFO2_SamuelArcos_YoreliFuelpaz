import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import io
import os

def validar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido.")

class ArchivoCSV:
    def __init__(self, ruta):
        self.ruta = ruta
        self.df = pd.read_csv(ruta)