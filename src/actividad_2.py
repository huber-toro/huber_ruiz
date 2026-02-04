# Evidencia de aprendizaje 2
# Ubert Toro - IUDIGITAL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 22)] 
        self.df= pd.DataFrame(data=datos,columns=["#ejercicio", "valor"])
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_Actividad2 =  f"{self.ruta_raiz}/src/evidencias/actividad_2/"


    def ejercicio1(self):

        # Generar un array con valores desde 10 hasta 29
        array_10_29 = np.arange(10,30)
        #self.df["#ejercicio"]=1
        #self.df["valor"]=str(array_10_29)
        self.df.iloc[0, 1] = ', '.join(map(str, array_10_29.tolist()))
        #self.df.to_excel("Actividad_2.xlsx")

    def ejercicio2(self):

        # 2. Suma de una matriz 10x10 de unos.
        array2 = np.ones((10, 10))
        suma = np.sum(array2)
        self.df.iloc[1,1]=str(suma)
        print("ejercicio2", suma)
        
    def ejercicio3(self):

        # Generar dos arrays de tamaño 5 con números aleatorios entre 1 y 10
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        # Realizar el producto elemento a elemento
        producto = array1 * array2
        self.df.iloc[2,1]=str(producto)
        print("Array 1:", array1)
        print("Array 2:", array2)
        print("ejercicio3", producto)

    def ejercicio4(self):
        # Crear una matriz diagonal dominante para garantizar que sea invertible
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
        #Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.
        array6 = np.arange(3).reshape(3, 1)
        array7 = np.arange(3).reshape(1, 3)
        resultado = array6 + array7
        self.df.iloc[5, 1] = f"Array 3x1:\n{np.array_str(array6)}\n\nArray 1x3:\n{np.array_str(array7)}\n\nSuma (3x3):\n{np.array_str(resultado)}" 
        print("ejercicio6", resultado)

    def ejercicio7(self):
        #De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
        matriz5x5 = np.random.randint(1, 10, (5, 5))
        submatriz = matriz5x5[1:3, 1:3]
        self.df.iloc[6, 1] = f"Matriz 5x5:\n{np.array_str(matriz5x5)}\n\nSubmatriz 2x2:\n{np.array_str(submatriz)}"
        print("ejercicio7", submatriz)
    
    def ejercicio8(self):
        #Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5
        array8 = np.zeros(10)
        array8[3:7] = 5
        self.df.iloc[7, 1] = str(array8)
        print("ejercicio8", array8)

    def ejercicio9(self):
        #Dada una matriz de 3x3, invierte el orden de sus filas
        matriz = np.random.randint(1, 10, (3, 3))
        matriz_invertida = matriz[::-1]
        self.df.iloc[8, 1] = f"Matriz original:\n{str(matriz.tolist())}\n\nMatriz invertida:\n{str(matriz_invertida.tolist())}"
        print("ejercicio9", matriz_invertida)

    def ejercicio10(self):
        #Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
        array10 = np.random.rand(10)
        mayores_05 = array10[array10 > 0.5]
        self.df.iloc[9, 1] = f"Array:\n{str(array10)}\n\nMayores a 0.5:\n{str(mayores_05)}"
        print("ejercicio10", mayores_05)

    #Gráficos de dispersión, densidad y contorno:
    def ejercicio11(self):
        #Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
        X = np.random.rand(100)
        Y = np.random.rand(100)
        plt.figure() 
        plt.scatter(X, Y)
        plt.title("Gráfico de dispersión")
        plt.xlabel("X")
        plt.ylabel("Y")
        ruta = "{}ejercicio_11.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[10, 1] = "Gráfico de dispersión"
        print("ejercicio11", "Gráfico de dispersión")
        

    def ejercicio12(self):
        #Genera un gráfico de dispersión las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)
        plt.figure()
        plt.scatter(x, y, label="sin(x) + ruido")
        plt.plot(x, np.sin(x), label="sin(x)", color="red")
        plt.legend()
        plt.title("Gráfico de dispersión con ruido")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta = "{}ejercicio_12.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[11, 1] = "Gráfico de dispersión con ruido"
        print("ejercicio12", "Gráfico de dispersión con ruido")

    def ejercicio13(self):
        #Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.linspace(-2*np.pi, 2*np.pi, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.cos(X) + np.sin(Y)
        plt.figure()
        plt.contourf(X, Y, Z)
        plt.colorbar()
        plt.title("Gráfico de contorno")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta= "{}ejercicio_13.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[12, 1] = "Gráfico de contorno"
        print("ejercicio13", "Gráfico de contorno")

    def ejercicio14(self):
        #Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.
        x = np.random.rand(1000)
        y = np.random.rand(1000)
        plt.figure()
        plt.scatter(x, y, c=x, cmap="viridis")
        plt.colorbar()
        plt.title("Gráfico de dispersión con densidad de puntos")
        plt.xlabel("x")
        plt.ylabel("y")
        rura= "{}ejercicio_14.png".format(self.ruta_Actividad2)
        plt.savefig(rura)
        plt.close()
        #plt.show()
        self.df.iloc[13, 1] = "Gráfico de dispersión con densidad de puntos"
        print("ejercicio14", "Gráfico de dispersión con densidad de puntos")

    def ejercicio15(self):
        #A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.linspace(-2*np.pi, 2*np.pi, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.cos(X) + np.sin(Y)
        plt.figure()
        plt.contourf(X, Y, Z)
        plt.colorbar()
        plt.title("Gráfico de contorno lleno")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta= "{}ejercicio_15.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[14, 1] = "Gráfico de contorno lleno"
        print("ejercicio15", "Gráfico de contorno lleno")

    def ejercicio16(self):
        #Añade etiquetas para el eje X (‘Eje X’), eje Y (‘Eje Y’) y un título (‘Gráfico de Dispersión’) a tu gráfico de dispersión del ejercicio 12 y crea leyendas para cada gráfico usando código LaTex
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)   
        plt.figure()
        plt.scatter(x, y, label=r"$\sin(x) + ruido$")
        plt.plot(x, np.sin(x), label=r"$\sin(x)$", color="red")
        plt.legend()
        plt.title("Gráfico de dispersión")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        ruta= "{}ejercicio_16.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[15, 1] = "Gráfico de dispersión con etiquetas"
        print("ejercicio16", "Gráfico de dispersión con etiquetas")

     #Histogramas
    def ejercicio17(self):
        #Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal.
        array17 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array17, bins=30)
        plt.title("Histograma")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_17.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[16, 1] = "Histograma"
        print("ejercicio17", "Histograma")

    def ejercicio18(self):
        #Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma.
        array18_1 = np.random.normal(0, 1, 1000)
        array18_2 = np.random.normal(2, 1, 1000)
        plt.figure()
        plt.hist(array18_1, bins=30, alpha=0.5, label="Array 1")
        plt.hist(array18_2, bins=30, alpha=0.5, label="Array 2")
        plt.legend()
        plt.title("Histograma con dos distribuciones")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_18.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[17, 1] = "Histograma con dos distribuciones"
        print("ejercicio18", "Histograma con dos distribuciones")

    def ejercicio19(self):
        #Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.
        array19 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array19, bins=10, alpha=0.5, label="Bins 10")
        plt.hist(array19, bins=30, alpha=0.5, label="Bins 30")
        plt.hist(array19, bins=50, alpha=0.5, label="Bins 50")
        plt.legend()
        plt.title("Histograma con diferentes bins")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_19.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[18, 1] = "Histograma con diferentes bins"
        print("ejercicio19", "Histograma con diferentes bins")

    def ejercicio20(self):
        #Añade una línea vertical que indique la media de los datos en el histograma.
        array20 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array20, bins=30, alpha=0.5)
        plt.axvline(np.mean(array20), color="red", linestyle="--", label="Media")
        plt.legend()
        plt.title("Histograma con media")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_20.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[19, 1] = "Histograma con media"
        print("ejercicio20", "Histograma con media")

    def ejercicio21(self):
        #Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos.
        array21_1 = np.random.normal(0, 1, 1000)
        array21_2 = np.random.normal(2, 1, 1000)
        plt.figure()
        plt.hist(array21_1, bins=30, alpha=0.5, color="blue", label="Array 1")
        plt.hist(array21_2, bins=30, alpha=0.5, color="red", label="Array 2")
        plt.legend()
        plt.title("Histograma con dos distribuciones")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_21.png".format(self.ruta_Actividad2)
        plt.savefig(ruta)
        plt.close()
        #plt.show()
        self.df.iloc[20, 1] = "Histograma con dos distribuciones superpuestas"
        print("ejercicio21", "Histograma con dos distribuciones superpuestas")


        #print(array_10_29)
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
        self.ejercicio14()
        self.ejercicio15()
        self.ejercicio16()
        self.ejercicio17()
        self.ejercicio18()
        self.ejercicio19()
        self.ejercicio20()
        self.ejercicio21()
        
        self.df.to_csv(f"{self.ruta_Actividad2}/Actividad_2.csv", index=False)
ene= Ejercicios()
ene.ejecutar()

        # Prueba workflow en Ubuntu