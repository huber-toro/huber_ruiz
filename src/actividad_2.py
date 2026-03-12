# Evidencia de aprendizaje 2: uso de Python para análisis de datos, haciendo uso de arrays de NumPy

# Ubert Toro - IUDIGITAL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 14)] 
        self.df= pd.DataFrame(data=datos,columns=["#ejercicio", "valor"])
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_Actividad2 =  f"{self.ruta_raiz}/src/evidencias/actividad_2/"

        #Introducción y cálculos con los arrays de NumPy:
    def ejercicio1(self):
        # Generar un array con valores desde 10 hasta 29
        array_10_29 = np.arange(10,30)
        #self.df["#ejercicio"]=1
        #self.df["valor"]=str(array_10_29)
        self.df.iloc[0, 1] = ', '.join(map(str, array_10_29.tolist()))
        #self.df.to_excel("Actividad_2.xlsx")

    def ejercicio2(self):
        # Crear un array 10x10 con valores aleatorios
        array2 = np.random.randint(1, 10, (10, 10))
        suma = np.sum(array2)
        self.df.iloc[1, 1] = f"Suma: {suma}\nArray:\n{np.array_str(array2)}"
        print("ejercicio2", suma)

        
    def ejercicio3(self):
        # Generar dos arrays de tamaño 5 con números aleatorios entre 1 y 10
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        # Multiplicación elemento a elemento
        resultado = array1 * array2
        self.df.iloc[2, 1] = f"Array1: {array1}\nArray2: {array2}\nResultado: {resultado}"
        print("ejercicio3", resultado)


    def ejercicio4(self):
        # Crear una matriz 4x4 diagonal dominante y calcula su inversa
        matriz = np.fromfunction(lambda i, j: np.where(i == j, i + j + 10, i + j), (4, 4), dtype=int)
        # Calcular la inversa
        inversa = np.linalg.inv(matriz)
        self.df.iloc[3, 1] = str(inversa)
        print("\nMatriz inversa:\n", inversa)

    def ejercicio5(self):
        #Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices.
        array5 = np.random.rand(100)
        max_val = np.max(array5)
        min_val = np.min(array5)
        indice_max = np.argmax(array5)
        indice_min = np.argmin(array5)
        self.df.iloc[4, 1] = f"Max: {max_val}, IndMax: {indice_max}, Min: {min_val}, IndMin: {indice_min}"
        print(f'Máximo: {max_val} en índice {indice_max}')
        print(f'Mínimo: {min_val} en índice {indice_min}')

        #Broadcasting e indexado de Arrays:        
    def ejercicio6(self):
        # De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
        matriz5x5 = np.random.randint(1, 10, (5, 5))
        submatriz = matriz5x5[1:3, 1:3]
        self.df.iloc[5, 1] = f"Matriz 5x5:\n{np.array_str(matriz5x5)}\n\nSubmatriz 2x2:\n{np.array_str(submatriz)}"
        print("ejercicio6", submatriz)

    def ejercicio7(self):
        # Crea un array de ceros de tamaño 10 y cambia los valores en índices 3 a 6 a 5.
        array7 = np.zeros(10)
        array7[3:7] = 5
        self.df.iloc[6, 1] = str(array7)
        print("ejercicio7", array7)

    def ejercicio8(self):
        # Dada una matriz de 3x3, invierte el orden de sus filas.
        matriz = np.random.randint(1, 10, (3, 3))
        matriz_invertida = matriz[::-1]
        self.df.iloc[7, 1] = f"Matriz original:\n{matriz}\n\nMatriz invertida:\n{matriz_invertida}"
        print("ejercicio8", matriz_invertida)

    def ejercicio9(self):
        # Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos mayores a 0.5.
        array9 = np.random.rand(10)
        mayores_05 = array9[array9 > 0.5]
        self.df.iloc[8, 1] = f"Array:\n{array9}\n\nMayores a 0.5:\n{mayores_05}"
        print("ejercicio9", mayores_05)

        #Gráficos de dispersión, densidad y contorno:
    def ejercicio10(self):
        # Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
        X = np.random.rand(100)
        Y = np.random.rand(100)
        plt.figure()
        plt.scatter(X, Y)
        plt.title("Gráfico de dispersión")
        plt.xlabel("X")
        plt.ylabel("Y")
        ruta = f"{self.ruta_Actividad2}/ejercicio_10.png"
        plt.savefig(ruta)
        plt.close()
        self.df.iloc[9, 1] = "Gráfico de dispersión"
        print("ejercicio10", "Gráfico de dispersión")

    def ejercicio11(self):
        # Crear datos periódicos (sin(x)) y añadir ruido 
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y_ruido = np.sin(x) + np.random.normal(0, 0.1, 100)
        self.df.iloc[10, 1] = "Datos periódicos con ruido"
        print("ejercicio11", "Datos periódicos con ruido")
        return x, y_ruido

    def ejercicio12(self):
        # Representar en un mismo gráfico los datos con ruido y la curva de referencia
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y_ruido = np.sin(x) + np.random.normal(0, 0.1, 100)
        plt.figure()
        plt.scatter(x, y_ruido, label="sin(x) + ruido")
        plt.plot(x, np.sin(x), color="red", label="sin(x)")
        plt.legend()
        plt.title("Gráfico con ruido y referencia")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta = f"{self.ruta_Actividad2}/ejercicio_12.png"
        plt.savefig(ruta)
        plt.close()
        self.df.iloc[11, 1] = "Gráfico con ruido y referencia"
        print("ejercicio12", "Gráfico con ruido y referencia")

    def ejercicio13(self):
        # Mejorar el gráfico del ejercicio 12 con etiquetas y título
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y_ruido = np.sin(x) + np.random.normal(0, 0.1, 100)
        plt.figure()
        plt.scatter(x, y_ruido, label=r"$\sin(x) + ruido$")
        plt.plot(x, np.sin(x), color="red", label=r"$\sin(x)$")
        plt.legend()
        plt.title("Gráfico de Dispersión")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        ruta = f"{self.ruta_Actividad2}/ejercicio_13.png"
        plt.savefig(ruta)
        plt.close()
        self.df.iloc[12, 1] = "Gráfico mejorado con etiquetas"
        print("ejercicio13", "Gráfico mejorado con etiquetas")

            
    def ejecutar(self):
        self.ejercicio1()
        self.ejercicio2()
        self.ejercicio3()
        self.ejercicio4()
        self.ejercicio5()
        self.ejercicio6()
        self.ejercicio7()
        self.ejercicio8()
        self.ejercicio9()
        self.ejercicio10()
        self.ejercicio11()
        self.ejercicio12()
        self.ejercicio13()             
        self.df.to_csv(f"{self.ruta_Actividad2}/Actividad_2.csv", index=False)

ene= Ejercicios()
ene.ejecutar()

        