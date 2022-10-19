import Pokemon.funciones.funcionesPokedex as funciones

def menu():
    while True:
        print("Opcion a elegir.\n1.Jugar\n2.Pokedex\n3.Salir")
        opt = funciones.opciones(1,3)
        principal = True
        if opt == 1:
            #Las reglas pueden ser objetos por ejemplo
            principal = False
            while principal == False:
                print("1.Jugar un combate\n2.Modificar reglas del combate\n3.Atras")
                opt = funciones.opciones(1,3)
                if opt  == 1:
                    nRival = input("Como se llama tu rival? ")
                    funciones.empezarCombate()
                elif opt == 2:
                    funciones.modificarReglas()
                elif opt == 3:
                    principal = True
        elif opt == 2:
            principal = False
            while principal == False:
                print("1.Mirar los datos de un pokemon\n2.Modificar los datos de un pokemon\n3.Anadir un pokemon\n4.Eliminar un pokemon\n5.Atras")
                opt = funciones.opciones(1,5)

                if opt == 1:
                    funciones.verPokemon()
                elif opt == 2:
                    funciones.modPokemon()
                elif opt == 3:
                    funciones.anadirPokemon()
                elif opt == 4:
                    funciones.eliminarPokemon()
                elif opt == 5:
                    principal = True
        elif opt == 3:
            print("Gracias por jugar!")

menu()