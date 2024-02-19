
import os, funcionesCamper, funcionesRuta, funcionesMatricula, funcionesReportes

def menuCoordinador():

    menu=["Aprobar Campers","Crear Rutas","Crear Modulos","Gestionar Matricula","Reportes","Salir"]
    while(True):
        os.system('cls')
        print(""""
        ..............................
                .:CAMPUSLANDS:.
        ..........COORDINADOR..........
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    funcionesCamper.aprobarCamper()
                if opc == 2:
                    funcionesRuta.crearRuta()
                if opc == 3:
                    funcionesRuta.crearModulos()
                if opc == 4:
                    funcionesMatricula.crearGruposMatriculas()
                if opc == 5:
                    menuReportes()
                if opc == 6:
                    break
        except ValueError:
            print()

def menuReportes():

    menu=["Ver Campers Incritos","Ver Campers Aprobados","Ver Trainers Trabajando","Salir"]
    while(True):
        os.system('cls')
        print(""""
        ..............................
                .:CAMPUSLANDS:.
        ..........COORDINADOR..........
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    funcionesReportes.verCampersIncritos()
                if opc == 2:
                    funcionesReportes.verCampersAprobados()
                if opc == 3:
                    funcionesReportes.verTrainers()
                if opc == 4:
                    break
        except ValueError:
            print()

def menuCamper():

    menu=["Registrarse","Salir"]
    while(True):
        os.system('cls')
        print(""""
        ..............................
                .:CAMPUSLANDS:.
        ............CAMPER............
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    funcionesCamper.crearCamper()
                if opc == 2:
                    break
        except ValueError:
            print("Usuario no *** no recibime numero")

def menuCamper():

    menu=["Calificar Modulo Camper","Salir"]
    while(True):
        os.system('cls')
        print(""""
        ..............................
                .:CAMPUSLANDS:.
        ............CAMPER............
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    funcionesCamper.crearCamper()
                if opc == 2:
                    break
        except ValueError:
            print("Usuario no *** no recibime numero")


def menuPrincipal():

    menu=["Coordinador","Trainer","Camper","Salir"]
    while(True):
        os.system('cls')
        print(""""
        ..............................
               .:CAMPUSLANDS:.
        ........MENU PRINCIPAL........
        
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(">>")
                if opc == 1:
                    menuCoordinador()
                if opc == 3:
                    menuCamper()
                if opc == 4:
                    break
        except ValueError:
            print("Usuario no *** no recibime numero")

        

