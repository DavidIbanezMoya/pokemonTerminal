# import Pokemon.functions.funcionesPokedex as functions
#
# def menu():
#     while True:
#         print("Opcion a elegir.\n1.Jugar\n2.Pokedex\n3.Salir")
#         opt = functions.opciones(1,3)
#         principal = True
#         if opt == 1:
#             #Las reglas pueden ser objetos por ejemplo
#             principal = False
#             while principal == False:
#                 print("1.Jugar un combate\n2.Modificar reglas del combate\n3.Atras")
#                 opt = functions.opciones(1,3)
#                 if opt  == 1:
#                     nRival = input("Como se llama tu rival? ")
#                     functions.empezarCombate()
#                 elif opt == 2:
#                     functions.modificarReglas()
#                 elif opt == 3:
#                     principal = True
#         elif opt == 2:
#             principal = False
#             while principal == False:
#                 print("1.Mirar los datos de un pokemon\n2.Modificar los datos de un pokemon\n3.Anadir un pokemon\n4.Eliminar un pokemon\n5.Atras")
#                 opt = functions.opciones(1,5)
#
#                 if opt == 1:
#                     functions.verPokemon()
#                 elif opt == 2:
#                     functions.modPokemon()
#                 elif opt == 3:
#                     functions.anadirPokemon()
#                 elif opt == 4:
#                     functions.eliminarPokemon()
#                 elif opt == 5:
#                     principal = True
#         elif opt == 3:
#             print("Gracias por jugar!")
#
# menu()

import Pokemon.functions.pokedex_functions as functions

def menu():
    while True:
        print("Choose an option.\n1. Play\n2. Pokedex\n3. Quit")
        option = functions.get_option(1, 3)
        main_menu = True
        if option == 1:
            main_menu = False
            while not main_menu:
                print("1. Start a battle\n2. Modify battle rules\n3. Go back")
                option = functions.get_option(1, 3)
                if option == 1:
                    rival_name = input("What's your rival's name? ")
                    functions.start_Battle()
                elif option == 2:
                    functions.modify_Rules()
                elif option == 3:
                    main_menu = True
        elif option == 2:
            main_menu = False
            while not main_menu:
                print("1. View Pokemon data\n2. Modify Pokemon data\n3. Add a Pokemon\n4. Delete a Pokemon\n5. Go back")
                option = functions.get_option(1, 5)
                if option == 1:
                    functions.view_Pokemon()
                elif option == 2:
                    functions.modify_Pokemon()
                elif option == 3:
                    functions.add_Pokemon()
                elif option == 4:
                    functions.delete_Pokemon()
                elif option == 5:
                    main_menu = True
        elif option == 3:
            print("Thank you for playing!")
            break;

menu()
