import manejoDatos

def verRutasCreadas():
    rutas = list(manejoDatos.cargarDatos("rutas.json"))

    print("")
    print(".....Rutas disponibles.....")
    print("")

    for val in rutas:
        print("\n\n")
        for i,j in enumerate(val.keys()):
            print(str(i+1) + ". " + j + "")
            
            if isinstance(val[j], str):
                print("    ->"  + " " + val[j])
            else:
                for k in val[j]:
                    print("    ->"  + " " + str(k))

    print("")

def verTrainersCreadas():
    rutas = list(manejoDatos.cargarDatos("trainersBD.json"))

    print("")
    print(".....Trainers disponibles.....")
    print("")

    for val in rutas:
        print("\n")
        print("-> " + val["nombre"])
    print("")

def verSalonesDisponibles():
    salones = list(manejoDatos.cargarDatos("salones.json"))

    print("")
    print(".....Trainers disponibles.....")
    print("")

    for val in salones:
        print("\n")
        if val["estado"] == "libre":
            for i in val:

                print("-> " + i + " : " +val[i])
    print("")

def verCampersSinGrupo():
    campers = list(manejoDatos.cargarDatos("campersAprobadosBD.json"))
    num = 0
    print("")
    print(".....Campers a Matricular.....")
    print("")

    for val in campers:
        print("\n")
        if val["estado"] == "Aprobado":
            print("-> " + "Identificacion " + " : " +val["id"])
            print("-> " + "Nombre " + " : " +val["nombres"])
        else:
            num = num + 1
    
    if num == len(campers):
        return False
    else:
        return True
    print("")


def verRuta(rutaSelec):
    rutas = list(manejoDatos.cargarDatos("rutas.json"))

    print("")
    print(".....Informacion de Ruta.....")
    print("")

    for val in rutas:
        if val["nombreRuta"] == rutaSelec:
            for i,j in enumerate(val.keys()):
                print(str(i+1) + ". " + j + "")
                
                if isinstance(val[j], str):
                    print("    ->"  + " " + val[j])
                else:
                    for k in val[j]:
                        print("    ->"  + " " + str(k))

    print("")

def obtenerModulosRuta(rutaSelec):
    rutas = list(manejoDatos.cargarDatos("rutas.json"))

    diccionario = {}

    for val in rutas:
        if val["nombreRuta"] == rutaSelec:
            for j in val.keys():
                if isinstance(val[j], str):
                    diccionario[val[j]] = ""
                else:
                    for k in val[j]:
                        diccionario[k] = ""

    return diccionario



def verificarExistenciaDatos(rutajson,texto,seccion):
    rutas = list(manejoDatos.cargarDatos(rutajson))
    coincidencia = False
    for val in rutas:
        if val[seccion] == texto:
            coincidencia = True
            return coincidencia

    return 

def verificarExistenciaCampers(rutajson,texto):
    rutas = list(manejoDatos.cargarDatos(rutajson))
    coincidencia = False
    for val in rutas:
        if val["estado"] == "Aprobado" and val["id"] == texto:
            coincidencia = True
            return coincidencia

    return coincidencia

def verificarExistenciaSalones(rutajson,texto1,texto2):
    rutas = list(manejoDatos.cargarDatos(rutajson))
    coincidencia = False
    for val in rutas:
        if val["nombre"] == texto1 and val["estado"] == "libre" and val["horaInicio"] == texto2:
            coincidencia = True
            return coincidencia

    return coincidencia

def crearGruposMatriculas():
    rutas = list(manejoDatos.cargarDatos("gruposMatriculados.json"))
    idCamper = []
    nombreGrupo = input("Por favor ingrese el nombre para asignar al nuevo grupo: ")
    
    while True:
        verRutasCreadas()
        print("")
        nombreRuta = input("Por favor ingrese el nombre de la ruta a asignar al grupo: ")


        if verificarExistenciaDatos("rutas.json", nombreRuta, "nombreRuta"):
            break
        else:
            print("")
            print("Error. Alguno de los modulos ingresados no se encuentran en la base de datos")
            print("")

    while True:
        verTrainersCreadas()
        print("")
        nombreTrainer = input("Por favor ingrese el nombre del trainer para asignar al grupo: ")


        if verificarExistenciaDatos("trainersBD.json", nombreTrainer, "nombre"):
            break
        else:
            print("")
            print("Error. Alguno de los modulos ingresados no se encuentran en la base de datos")
            print("")

    while True:
        verSalonesDisponibles()
        print("")

        nombreSalon = input("Por favor ingrese el nombre del salon para asignar al grupo: ")
        horaInicio = input("Por favor ingrese la hora de inicio de clases en el salon para asignar al grupo: ")


        if verificarExistenciaSalones("salones.json", nombreSalon, horaInicio):
            salones = list(manejoDatos.cargarDatos("salones.json"))
            for val in salones:
                if val["nombre"] == nombreSalon and val["estado"] == "libre" and val["horaInicio"] == horaInicio:
                    val["estado"] = "ocupado"

            manejoDatos.guardarDatos(salones, "salones.json")
            
            

            
            break
        else:
            print("")
            print("Error. Alguno de los modulos ingresados no se encuentran en la base de datos")
            print("")

    while True:
        vacio = verCampersSinGrupo()
        print("")
        camper = input("Por favor ingrese el id del camper para asignar a este grupo: ")

        if verificarExistenciaCampers("campersAprobadosBD.json", camper) and vacio == True:

            campers = list(manejoDatos.cargarDatos("campersAprobadosBD.json"))
            for val in campers:
                if val["id"] == camper and val["estado"] == "Aprobado":
                    val["estado"] = "Matriculado"
                    val["notas"] = obtenerModulosRuta(nombreRuta)
                    manejoDatos.guardarDatos(campers, "campersAprobadosBD.json")
            opc = input("\n¿Desea matricular otro camper a este grupo? Si(Y) No(N): ")
            if opc == "Y":
                input("Presione enter para continuar: ")
            else:
                break

        elif vacio == False:
            input("No hay campers sin grupo. Presione enter para continuar. ")
            break
        else:
            print("")
            print("Error. Alguno de los modulos ingresados no se encuentran en la base de datos")
            print("")


    nuevoGrupo = {
        "nombreGrupo":nombreGrupo,
        "ruta":nombreRuta,
        "trainer":nombreTrainer,
        "salon":[nombreSalon,horaInicio],
        "campers":camper,
        

    }
    rutas.append(nuevoGrupo)

    manejoDatos.guardarDatos(rutas, "gruposMatriculados.json")

