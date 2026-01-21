import json



class Ingestiones():
    def __init__(self):
        self.ruta_static = "C:/Proyecto_repositorio/ubert_toro/crs/pad_2026/static/"
    def leer_json(self):
        # r read w write
        ruta_json = f"{self.ruta_static}json/datos_personas.json"
        with open(ruta_json, "r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos
        
    def leer_txt(self):
        # r read w write
        ruta_txt = f"{self.ruta_static}/txt/info.txt"
        with open(ruta_txt, "r",encoding="utf-8") as f:
            datos = f.read()
        return datos

              
inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)
print("************************************************************************************************************")
print("************************************************************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)



