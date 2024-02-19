import manejoDatos

def verCampersIncritos():
    print("")
    print(".....Campers Inscritos.....")
    print("")

    campers = list(manejoDatos.cargarDatos("campersRegistradosBD.json"))

    for val in campers:
        for i in val.keys():
            print(i + " -> " + str(val[i]))
        print("\n")

def verTrainers():
    print("")
    print(".....Trainers Trabajando.....")
    print("")

    campers = list(manejoDatos.cargarDatos("trainersBD.json"))

    for val in campers:
        for i in val.keys():
            print(i + " -> " + str(val[i]))
        print("\n")

def verCampersAprobados():
    print("")
    print(".....Campers Aprobados.....")
    print("")

    campers = list(manejoDatos.cargarDatos("campersAprobadosBD.json"))

    for val in campers:
        if val["estado"] == "Aprobado":
            for i in val.keys():
                print(i + " -> " + str(val[i]))
            print("\n")

verCampersAprobados()