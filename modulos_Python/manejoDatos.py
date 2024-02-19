import json

ruta = "archivos_Json\\"

def cargarDatos(nombreJson):

    with open(ruta + str(nombreJson), "r") as file:
        respuesta = json.load(file)
        return respuesta


def guardarDatos(datos, nombreJson):
    with open(ruta+ str(nombreJson),"w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)
