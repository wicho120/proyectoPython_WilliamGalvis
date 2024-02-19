import manejoDatos, verificarDatos

def crearCamper():
    campers = list(manejoDatos.cargarDatos("campersRegistradosBD.json"))

    identificacion = input("Por favor ingrese la identificacion del camper: ")
    nombres = input("Por favor ingrese los nombres del camper: ")
    apellidos = input("Por favor ingrese los apellidos del camper: ")
    direccion = input("Por favor ingrese la direccion del camper: ")
    acudiente = input("Por favor ingrese el nombre completo del acudiente del camper: ")
    numCelular = input("Por favor ingrese el numero de celular del camper: ")
    #estado = input("Por favor ingrese el estado del camper(Proceso Ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")
    

    camperNuevo = {"id":identificacion, "nombres":nombres, "apellidos": apellidos, 
                   "direccion": direccion, "acudiente":acudiente, "numero celular":numCelular, "estado":"Proceso Ingreso", "riesgo":"No"}
    
    campers.append(camperNuevo)
    manejoDatos.guardarDatos(campers, "campersRegistradosBD.json")
    print("Felicitaciones se ha registrado con exito!")
    input("Presione enter para continuar ")
    

def aprobarCamper():
    
    campersInscritos = list(manejoDatos.cargarDatos("campersRegistradosBD.json"))
    campersAprobados = list(manejoDatos.cargarDatos("campersAprobadosBD.json"))
    salir = 0

    while salir == 0:  
        id = input("Por favor ingrese el id del camper a calificar: ")

        for i in campersInscritos:

            if id== i["id"]:
                while True:
                    notaTeorica = verificarDatos.verificarNota("Por favor ingrese la nota teorica: ")
                    notaPractica = verificarDatos.verificarNota("Por favor ingrese la nota practica: ")
                    notaTotal = (notaTeorica+notaPractica)/2
                    confirmar = input("¿Las notas registradas son correctas? Se haran cambios irreversibles Si(Y) No(N): ")
                    if confirmar == "Y":
                        break
                
                if notaTotal >= 60:
                    i["estado"] = "Aprobado"
                    campersAprobados.append(i)
                    manejoDatos.guardarDatos(campersAprobados, "campersAprobadosBD.json")
                    print("El camper ha sido aprobado.")
                    input("Presione enter para continuar ")
                    campersInscritos.remove(i)
                    manejoDatos.guardarDatos(campersInscritos, "campersRegistradosBD.json")
                    salir = 1

                else:

                    campersInscritos.remove(i)
                    manejoDatos.guardarDatos(campersInscritos, "campersRegistradosBD.json")
                    print("El camper no paso la prueba filtro inicial. No ha sido aprobado")
                    print("Presione enter para continuar ")

        if salir == 0:
            print("")
            print("No se encontro ningun camper asociado al id ingresado")
            print("")
            input("Presione enter para continuar ")
            salir = 1

        

            
        



 
