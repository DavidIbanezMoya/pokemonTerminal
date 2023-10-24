from Pokemon.classPokemon import Pokemon


# def opciones(min,max):
#     while True:
#         opt = input("Opcion: ")
#         if opt.isdigit() == False:
#             print("Tiene que ser un numero!")
#         else:
#             if int(opt) < min or int(opt) > max:
#                 print("El numero esta fuera del rango!")
#             else:
#                 return int(opt)
# #---------------------------COMBATE--------------------------------------------------------------------------
#
# def empezarCombate():
#     print("Con cuantos Pokemon quieres combatir?(1-6)")
#     cantidad = opciones(1,6)
#     equipo = []
#     equipoRival = []
#     print("1.Elegir los Pokemon\n2.Jugar con equipos aleatorios\n3.Volver Atras")
#     opt = opciones(1,3)
#     if opt != 3:
#         for i in range (cantidad):
#             newPoke = Pokemon()
#             if opt == 1:
#                 while True:
#                     print("Que ID quieres? (0 para ver la Pokedex) ")
#                     f = open("pokedex.txt", "r+")
#                     listapokemon = f.readlines()
#
#                     id = opciones(0,(len(listapokemon) - 1))
#                     if id == 0:
#                         for i in listapokemon:
#                             print(i)
#                     if id > 0:
#                         newPoke.generarPokemon(id)
#                         break
#             elif opt == 2:
#                 newPoke.generarPokemon(newPoke.idAleatorio())
#
#             equipo.append(newPoke)
#
#         for i in range (cantidad):
#
#             PokeRival = Pokemon()
#             PokeRival.generarPokemon(PokeRival.idAleatorio())
#             equipoRival.append(PokeRival)
#
#         for i in equipo:
#             print(i)
#
#
#         while True:
#             print("\nQue quieres hacer?\n1.Combatir\n2.Observar Pokemon Rival\n3.Modificar movimientos\n4.Abandonar")
#             opt = opciones(1, 4)
#             if opt == 1:
#                 combate(equipo,equipoRival)
#             elif opt == 2:
#                 print("\n\n")
#                 for i in equipoRival:
#                     print(i)
#             #todo End this
#             elif opt == 3:
#                 print("De que Pokemon quieres ver los movimientos?")
#                 for i in equipo:
#                     print(i+1,")",i.nombre)
#             elif opt == 4:
#                 principal = True
#     else:
#         return
#
# def combate(equipo,equipoRival):
#     #Se necesita saber cual es el Pokemon que se tiene seleccionado en todo momento
#     activePokemon = equipo[0]
#
#     while True:
#         print("1.Movimientos\n2.Objetos\n3.Cambiar Pokemon\n4.Abandonar Combate")
#
#         opt = opciones(1, 4)
#         if opt != 4:
#             if opt == 1:
#                 print(activePokemon)
#
#
#             elif opt == 2:
#                 print("Still need to implement objects in battle")
#
#             elif opt == 3:
#                 while True:
#                     for i in range (len(equipo)):
#                         print(i+1,") ",equipo[i].nombre,"Vida:",equipo[i].vidaActual,"/",equipo[i].vida)
#                         #todo Change the active Pokemon, and warn when swapping to the same Poke
#                     print(len(equipo)+1,")Atras ")
#                     opt = opciones(1, len(equipo)+1)
#                     if opt == len(equipo)+1:
#                         break
#
#                     if (equipo[opt-1].nombre == activePokemon.nombre):
#                         print("Este Pokemon ya esta en uso!")
#                     else:
#                         activePokemon = equipo[opt-1]
#                         break
#
#         else:
#             principal = True
#             break
#
# def modificarReglas():
#     print("Que quieres modificar?\n1.Uso de objetos\n2.Modificadores de dano\n3.Nada")
#     opt = opciones(1,3)
#     objetos = True
#     tipos = True
#
#     if opt == 1:
#         print("Quieres permitir el uso de objetos?\n1.Si\n2.No")
#         opt = opciones(1,2)
#         if opt == 1:
#             return objetos
#         elif opt == 2:
#             objetos = False
#             return objetos
#     elif opt == 2:
#         print("Quieres que la tabla de tipos influya en el dano ocasionado?\n1.Si\n2.No")
#         opt = opciones(1,2)
#         if opt == 1:
#             return tipos
#         elif opt == 2:
#             tipos = False
#             return tipos
#
# # --------------------------POKEDEX--------------------------------------------------------------------------
#
# #todo Implementar una opcion para ver todos los Pokemon listados
# def anadirPokemon():
#     f = open("pokedex.txt","r+")
#     pokemon = f.readlines()
#     nID = len(pokemon)+1
#     nombre = input("Cual es el nombre del Pokemon?")
#     print("Cuantos tipos va a tener tu Pokemon (1 o 2)?")
#     cTipos = opciones(1,2)
#     f.write(f"\n{nID}#{nombre}#")
#     lista_Tipos = ["Fuego", "Agua", "Planta","Normal","Lucha","Bicho","Dragon","Electrico","Fantasma","Hielo",
#                    "Psiquico","Roca","Tierra","Veneno","Volador","Hada"]
#
#     for i in range (cTipos):
#         print(f"Tipo {i+1}\n")
#         for j in range (len(lista_Tipos)):
#             print(f"{j+1}){lista_Tipos[j]}")
#         opt = opciones(1,len(lista_Tipos))
#
#         tipo = lista_Tipos[opt-1]
#
#         #Eliminar el tipo seleccionado
#         del lista_Tipos[opt-1]
#
#         if i>0:
#             f.write("/")
#         f.write(tipo)
#
# def modPokemon():
#     #todo TENGO QUE TERMINAR ESTE MODULO
#     f = open("pokedex.txt","r+")
#     pokemon = f.readlines()
#     print(f"Que Pokemon quieres modificar? Total {len(pokemon)}")
#     num = opciones(1,len(pokemon))-1
#     for i in range(len(pokemon)):
#         if i == num:
#             print(pokemon[num])
#             print("Que campo quieres modificar\n1.ID\n2.Nombre\n3.Tipos\n4.Nada")
#             opt = opciones(1,4)
#             if opt == 1:
#                 nuevaID = input("Que numero quieres que sea la nueva ID?")
#             elif opt == 2:
#                 nuevoNombre = input("Nuevo nombre: ")
#                 linea = pokemon[num]
#                 print(f"El nuevo nombre sera {pokemon[num].split('#')[1]} -> {nuevoNombre}")
#                 print(linea.split("#")[1])
#                 linea.split("#")[1] = nuevoNombre
#                 print(linea.split("#")[1])
#
#                 print(linea)
#             elif opt == 3:
#                 print("Cuantos tipos tiene el Pokemon? 1 o 2")
#                 opt = opciones(1,2)
#             elif opt == 4:
#                 return
#
# def verPokemon():
#     f = open("pokedex.txt","r+")
#     pokemon = f.readlines()
#     print(f"Hay un total de {len(pokemon)} Pokemon.\nCual quieres ver?")
#     nID = opciones(1,len(pokemon))
#     for i in range (len(pokemon)):
#         segundoT = False
#         if i+1 == nID:
#             print("="*40+"\n"+"ID".ljust(5)+"Nombre".ljust(15)+"Tipo 1".ljust(10),end="")
#             try:
#                 if pokemon[i].split("#")[2].split("/")[1]:
#                     print("Tipo 2".ljust(10),end="")
#                     segundoT = True
#             except:
#                 print(end="")
#             print("\n"+"="*40)
#             if segundoT == True:
#                 print(pokemon[i].split("#")[0].ljust(5)+pokemon[i].split("#")[1].ljust(15)+pokemon[i].split("#")[2].split("/")[0].ljust(10)+pokemon[i].split("#")[2].split("/")[1].ljust(10))
#             else:
#                 print(pokemon[i].split("#")[0].ljust(5)+pokemon[i].split("#")[1].ljust(15)+pokemon[i].split("#")[2].ljust(10))
#
# def eliminarPokemon():
#     f = open("pokedex.txt", "r+")
#     pokemon = f.readlines()
#     f.close()
#     print(f"Hay un total de {len(pokemon)} Pokemon.\nCual quieres eliminar?")
#     nID = opciones(1, len(pokemon))
#     for i in range(len(pokemon)):
#         if i + 1 == nID:
#             f = open("pokedex.txt","w+")
#             del pokemon[nID-1]
#             print(pokemon)
#             print(f"El Pokemon: {pokemon[i-1].split('#')[1]}\nHa sido eliminado ")
#             f.writelines(pokemon)

from Pokemon.classPokemon import Pokemon


def get_option(min, max):
    while True:
        opt = input("Option: ")
        if opt.isdigit() == False:
            print("It must be a number!")
        else:
            if int(opt) < min or int(opt) > max:
                print("The number is out of range!")
            else:
                return int(opt)
#---------------------------BATTLE--------------------------------------------------------------------------

def start_Battle():
    print("How many Pokemon do you want to battle with? (1-6)")
    quantity = get_option(1, 6)
    team = []
    rivalTeam = []
    print("1. Choose Pokemon\n2. Play with random teams\n3. Go Back")
    opt = get_option(1, 3)
    if opt != 3:
        for i in range(quantity):
            newPoke = Pokemon()
            if opt == 1:
                while True:
                    print("Which ID do you want? (0 to see the Pokedex) ")
                    f = open("pokedex.txt", "r+")
                    pokemonList = f.readlines()

                    id = get_option(0, (len(pokemonList) - 1))
                    if id == 0:
                        for i in pokemonList:
                            print(i)
                    if id > 0:
                        newPoke.generatePokemon(id)
                        break
            elif opt == 2:
                newPoke.generatePokemon(newPoke.randomId())

            team.append(newPoke)

        for i in range(quantity):

            RivalPoke = Pokemon()
            RivalPoke.generatePokemon(RivalPoke.randomId())
            rivalTeam.append(RivalPoke)

        for i in team:
            print(i)

        while True:
            print("\nWhat do you want to do?\n1. Battle\n2. View Rival Pokemon\n3. Modify Moves\n4. Quit")
            opt = get_option(1, 4)
            if opt == 1:
                battle(team, rivalTeam)
            elif opt == 2:
                print("\n\n")
                for i in rivalTeam:
                    print(i)
            #todo End this
            elif opt == 3:
                print("Which Pokemon's moves do you want to see?")
                for i in team:
                    print(i + 1, ")", i.name)
            elif opt == 4:
                principal = True
    else:
        return

def battle(team, rivalTeam):
    #You need to know which Pokemon is selected at all times
    activePokemon = team[0]

    while True:
        print("1. Moves\n2. Items\n3. Switch Pokemon\n4. Quit Battle")

        opt = get_option(1, 4)
        if opt != 4:
            if opt == 1:
                print(activePokemon)

            elif opt == 2:
                print("Still need to implement objects in battle")

            elif opt == 3:
                while True:
                    for i in range(len(team)):
                        print(i + 1, ") ", team[i].name, "Health:", team[i].currentHealth, "/", team[i].health)
                        #todo Change the active Pokemon, and warn when swapping to the same Poke
                    print(len(team) + 1, ") Go Back ")
                    opt = get_option(1, len(team) + 1)
                    if opt == len(team) + 1:
                        break

                    if (team[opt - 1].name == activePokemon.name):
                        print("This Pokemon is already in use!")
                    else:
                        activePokemon = team[opt - 1]
                        break

        else:
            principal = True
            break

def modify_Rules():
    print("What do you want to modify?\n1. Use of items\n2. Damage modifiers\n3. Nothing")
    opt = get_option(1, 3)
    objects = True
    types = True

    if opt == 1:
        print("Do you want to allow the use of items?\n1. Yes\n2. No")
        opt = get_option(1, 2)
        if opt == 1:
            return objects
        elif opt == 2:
            objects = False
            return objects
    elif opt == 2:
        print("Do you want the type chart to influence damage dealt?\n1. Yes\n2. No")
        opt = get_option(1, 2)
        if opt == 1:
            return types
        elif opt == 2:
            types = False
            return types

# --------------------------POKEDEX--------------------------------------------------------------------------

#todo Implement an option to view all the listed Pokemon and after creating a Pokemon show the ID
def add_Pokemon():
    f = open("pokedex.txt", "r+")
    pokemon = f.readlines()
    nID = len(pokemon) + 1
    name = input("What is the name of the Pokemon?")
    print("How many types will your Pokemon have (1 or 2)?")
    cTypes = get_option(1, 2)
    f.write(f"\n{nID}#{name}#")
    typeList = ["Fire", "Water", "Grass", "Normal", "Fighting", "Bug", "Dragon", "Electric", "Ghost", "Ice",
                "Psychic", "Rock", "Ground", "Poison", "Flying", "Fairy"]

    for i in range(cTypes):
        print(f"Type {i + 1}\n")
        for j in range(len(typeList)):
            print(f"{j + 1}){typeList[j]}")
        opt = get_option(1, len(typeList))

        type = typeList[opt - 1]

        #Remove the selected type
        del typeList[opt - 1]

        if i > 0:
            f.write("/")
        f.write(type)

def modify_Pokemon():
    #todo I HAVE TO FINISH THIS MODULE
    f = open("pokedex.txt", "r+")
    pokemon = f.readlines()
    print(f"Which Pokemon do you want to modify? Total {len(pokemon)}")
    num = get_option(1, len(pokemon)) - 1
    for i in range(len(pokemon)):
        if i == num:
            print(pokemon[num])
            print("Which field do you want to modify\n1. ID\n2. Name\n3. Types\n4. Nothing")
            opt = get_option(1, 4)
            if opt == 1:
                newID = input("What number do you want the new ID to be?")
            elif opt == 2:
                newName = input("New name: ")
                line = pokemon[num]
                print(f"The new name will be {pokemon[num].split('#')[1]} -> {newName}")
                print(line.split("#")[1])
                line.split("#")[1] = newName
                print(line.split("#")[1])

                print(line)
            elif opt == 3:
                print("How many types does the Pokemon have? 1 or 2")
                opt = get_option(1, 2)
            elif opt == 4:
                return

def view_Pokemon():
    f = open("pokedex.txt", "r+")
    pokemon = f.readlines()
    print(f"There are a total of {len(pokemon)} Pokemon.\nWhich one do you want to view?")
    nID = get_option(1, len(pokemon))
    for i in range(len(pokemon)):
        secondT = False
        if i + 1 == nID:
            print("=" * 40 + "\n" + "ID".ljust(5) + "Name".ljust(15) + "Type 1".ljust(10), end="")
            try:
                if pokemon[i].split("#")[2].split("/")[1]:
                    print("Type 2".ljust(10), end="")
                    secondT = True
            except:
                print(end="")
            print("\n" + "=" * 40)
            if secondT == True:
                print(pokemon[i].split("#")[0].ljust(5) + pokemon[i].split("#")[1].ljust(15) + pokemon[i].split("#")[2].split("/")[0].ljust(10) + pokemon[i].split("#")[2].split("/")[1].ljust(10))
            else:
                print(pokemon[i].split("#")[0].ljust(5) + pokemon[i].split("#")[1].ljust(15) + pokemon[i].split("#")[2].ljust(10))

def delete_Pokemon():
    f = open("pokedex.txt", "r+")
    pokemon = f.readlines()
    f.close()
    print(f"There are a total of {len(pokemon)} Pokemon.\nWhich one do you want to delete?")
    nID = get_option(1, len(pokemon))
    for i in range(len(pokemon)):
        if i + 1 == nID:
            f = open("pokedex.txt", "w+")
            del pokemon[nID - 1]
            print(pokemon)
            print(f"The Pokemon: {pokemon[i - 1].split('#')[1]}\nHas been deleted ")
            f.writelines(pokemon)
