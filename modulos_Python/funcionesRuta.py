import manejoDatos, os

############################################## FUNCION MOSTRAR EN CONSOLA TODOS LOS MODULOS DISPONIBLES ####################################################################

def verModulosDisponibles():
    rutas = list(manejoDatos.cargarDatos("modulosRutas.json"))

    print("")
    print(".....Modulos disponibles.....")
    print("")

    for val in rutas:
        for i,j in enumerate(val.keys()):
            print(str(i+1) + ". Los modulos actuales para "+ str(j) +" son: ")
            for k,l in enumerate(val[j]):
                print("    " + str(k+1) + ". " + l)

    print("")


############################################## FUNCION VERIFICAR SI UN MODULO EXISTE EN BD ####################################################################


def verificarExistenciaModulos(clave, texto):
    rutas = list(manejoDatos.cargarDatos("modulosRutas.json"))
    coincidencia = False
    
    for i in rutas:
        for j in i[clave]:
            if texto == j:
                return texto
    
    return coincidencia

############################################## FUNCION CREAR NUEVOS MODULOS PARA LAS RUTAS ####################################################################


def crearModulos():
    rutas = list(manejoDatos.cargarDatos("modulosRutas.json"))

    print("")
    print(".....Bienvenido a la creacion de modulos.....")
    print("")

    

    menu=["Fundamentos","ProgWeb","ProgFormal","Base Datos", "Backend","Salir"]

    while(True):
        os.system("cls")
        verModulosDisponibles()
        print(""""
        ..............................
                .:CAMPUSLANDS:.
        ...........CREACION...........
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    nuevoModulo = input("Por favor ingrese el nombre del nuevo modulo para Fundamentos: ")
                    rutas[0]["fundamentos"].append(nuevoModulo)
                if opc == 2:
                    nuevoModulo = input("Por favor ingrese el nombre del nuevo modulo para ProgWeb: " )
                    rutas[0]["progWeb"].append(nuevoModulo)
                if opc == 3:
                    nuevoModulo = input("Por favor ingrese el nombre del nuevo modulo para ProgFormal: ")
                    rutas[0]["progFormal"].append(nuevoModulo)
                if opc == 4:
                    nuevoModulo = input("Por favor ingrese el nombre del nuevo modulo para Base Datos: ")
                    rutas[0]["baseDatos"].append(nuevoModulo)
                if opc == 5:    
                    nuevoModulo = input("Por favor ingrese el nombre del nuevo modulo para Backend: ")
                    rutas[0]["backend"].append(nuevoModulo)
                if opc == 6:
                    break
            manejoDatos.guardarDatos(rutas,"modulosRutas.json")
        except ValueError:
            print("Usuario no *** no recibime numero")
        else:
            input("Se guardo el nuevo modulo con exito. \nPresione enter para continuar")
        

############################################## FUNCION CREAR NUEVA RUTA ####################################################################


def crearRuta():
    rutas = list(manejoDatos.cargarDatos("rutas.json"))

    print(".....Bienvenido a la creacion de rutas.....")
    print("")
    print("""Nota: Para la creacion de rutas se debe tener en cuenta la siguientes indicaciones:
    1. Fundamentos siempre tiene (Introduccion, PseInt y Python) modulos
    2. Prog. Web debe tener obligatoriamente HTML y CSS ademas de otro modulo adicional
    3. Prog. Formal debe tener solo un modulo principal
    4. Base de datos debe tener un SGBD principal y otro secundario
    5. Backend debe tener un modulo u dos acorde a las tecnologias de la ruta
    6. Los modulos solo se pueden añadir si ya existen en BD
          
          """)
    
    verModulosDisponibles()
    
    nombreRuta = input("Por favor ingrese el nombre de la ruta a crear: ")
    while True:

        progWeb = input("Por favor ingrese el nombre del modulo para programacion web: ")
        if verificarExistenciaModulos("progWeb", progWeb):
            break
        else:
            print("")
            print("Error. El modulo ingresado no se encuentra en la base de datos")
            print("")

    while True:
        progFormal = input("Por favor ingrese el nombre del modulo para programacion formal: ")
        if verificarExistenciaModulos("progFormal", progFormal):
            break
        else:
            print("")
            print("Error. El modulo ingresado no se encuentra en la base de datos")
            print("")

    while True:
        baseDatos1 = input("Por favor ingrese el nombre del modulo principal para BD: ")
        baseDatos2 = input("Por favor ingrese el nombre del modulo alternativo para BD: ")

        if verificarExistenciaModulos("baseDatos", baseDatos1) and verificarExistenciaModulos("baseDatos", baseDatos2):
            break
        else:
            print("")
            print("Error. Alguno de los modulos ingresados no se encuentran en la base de datos")
            print("")

    while True:      
        backend = input("Por favor ingrese el nombre del modulo para el backend: ")
        if verificarExistenciaModulos("backend", backend):
            break
        else:
            print("")
            print("Error. El modulo ingresado no se encuentra en la base de datos")
            print("")

    ruta ={
    "nombreRuta":nombreRuta,
    "fundamentos": ["Introduccion", "PseInt", "Python"],
    "progWeb":["HTML","CSS",progWeb],
    "progFormal":progFormal,
    "baseDatos":[baseDatos1,baseDatos2],
    "backend":backend
    } 

    rutas.append(ruta)
    manejoDatos.guardarDatos(rutas,"rutas.json")
    

