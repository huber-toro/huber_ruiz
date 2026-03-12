
# Evidencia de aprendizaje: Estructuración y transformación básica de datos en Python
# Ubert Toro - IUDIGITAL

import csv
import json
import os

class Actividad1CSV:
    def __init__(self):
        # Usamos la ruta vieja que ya tenías
        self.ruta_static = "src/evidencias/actividad_1/json"
        os.makedirs(self.ruta_static, exist_ok=True)

    def leer_csv(self, archivo="src/personas.csv"):
        """Lee el archivo CSV y devuelve lista de diccionarios"""
        personas = []
        with open(archivo, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                personas.append({
                    "nombre": fila["nombre"],
                    "edad": int(fila["edad"]),
                    "ciudad": fila["ciudad"]
                })
        return personas

    def transformar(self, personas):
        """Aplica transformaciones básicas"""
        promedio = sum(p["edad"] for p in personas) / len(personas)
        # contar por ciudad
        por_ciudad = {}
        for p in personas:
            por_ciudad[p["ciudad"]] = por_ciudad.get(p["ciudad"], 0) + 1
        # mayores de 22
        mayores = [p["nombre"] for p in personas if p["edad"] > 22]

        return {
            "promedio_edad": promedio,
            "personas_por_ciudad": por_ciudad,
            "mayores_22": mayores
        }

    def exportar_json(self, datos, nombre="Actividad_1.json"):
        """Exporta resultados a JSON"""
        ruta_json = os.path.join(self.ruta_static, nombre)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Archivo JSON creado en: {ruta_json}")

if __name__ == "__main__":
    act1 = Actividad1CSV()
    personas = act1.leer_csv("src/personas.csv")
    resultados = act1.transformar(personas)
    act1.exportar_json(resultados)

    # Evidencia conceptual:
    # 1. Un objeto en Python es una instancia de una clase que combina atributos (datos) y métodos (comportamientos).
    # 2. Una función es independiente, mientras que un método está asociado a un objeto o clase.
    # 3. Las listas no son ideales para análisis masivo porque no están optimizadas para cálculos vectorizados ni grandes volúmenes de datos.
