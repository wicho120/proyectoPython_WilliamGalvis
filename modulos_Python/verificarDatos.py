def verificarNota(texto):
    while True:    
        nota = input(texto)

        if nota.isdigit() == True:
            nota = int(nota)
            if nota >= 0 and nota < 101:
                return nota
            else:
                print("La nota no cumple con las normas basicas")
        else:
            print("La nota no cumple con las normas basicas")