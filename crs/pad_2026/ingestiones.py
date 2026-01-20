import json



class Ingestiones():
    def __init__(self):
        self.ruta_static="C:/Proyecto_repositorio/ubert_toro/crs/pad_2026/stactic/"
    def leer_json(self):
        # r read w write
        ruta_json = "{}json/datos_personas.json".format(self.ruta_static)
        with open(ruta_json, "r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos
        

        
        
inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)

