from Pokemon.classPokemon import Pokemon


def opciones(min,max):
    while True:
        opt = input("Opcion: ")
        if opt.isdigit() == False:
            print("Tiene que ser un numero!")
        else:
            if int(opt) < min or int(opt) > max:
                print("El numero esta fuera del rango!")
            else:
                return int(opt)
#---------------------------COMBATE--------------------------------------------------------------------------

def empezarCombate():
    print("Con cuantos Pokemon quieres combatir?(1-6)")
    cantidad = opciones(1,6)
    equipo = []
    equipoRival = []
    print("1.Elegir los Pokemon\n2.Jugar con equipos aleatorios\n3.Volver Atras")
    opt = opciones(1,3)
    if opt != 3:
        for i in range (cantidad):
            newPoke = Pokemon()
            if opt == 1:
                print("Que ID quieres? ")
                f = open("pokedex.txt", "r+")
                listapokemon = f.readlines()
                id = opciones(1,(len(listapokemon) - 1))
                newPoke.generarPokemon(id)
            elif opt == 2:
                newPoke.generarPokemon(newPoke.idAleatorio())

            equipo.append(newPoke)

        for i in range (cantidad):

            PokeRival = Pokemon()
            PokeRival.generarPokemon(PokeRival.idAleatorio())
            equipoRival.append(PokeRival)

        for i in equipo:
            print(i)

        print("\nQue quieres hacer?\n1.Combatir\n2.Observar Pokemon Rival\n3.Abandonar")

        if opt == 1:
            print("Aqui ya debe ser la funcion de pegarse")
        elif opt == 2:
            print("\n\n")
            for i in equipoRival:
                print(i)
        elif opt == 3:
            principal = True
    else:
        return

def modificarReglas():
    print("Que quieres modificar?\n1.Uso de objetos\n2.Modificadores de dano\n3.Nada")
    opt = opciones(1,3)
    objetos = True
    tipos = True

    if opt == 1:
        print("Quieres permitir el uso de objetos?\n1.Si\n2.No")
        opt = opciones(1,2)
        if opt == 1:
            return objetos
        elif opt == 2:
            objetos = False
            return objetos
    elif opt == 2:
        print("Quieres que la tabla de tipos influya en el dano ocasionado?\n1.Si\n2.No")
        opt = opciones(1,2)
        if opt == 1:
            return tipos
        elif opt == 2:
            tipos = False
            return tipos

# --------------------------POKEDEX--------------------------------------------------------------------------

def anadirPokemon():
    f = open("pokedex.txt","r+")
    pokemon = f.readlines()
    nID = len(pokemon)+1
    nombre = input("Cual es el nombre del Pokemon?")
    print("Cuantos tipos va a tener tu Pokemon (1 o 2)?")
    cTipos = opciones(1,2)
    f.write(f"\n{nID}#{nombre}#")
    lista_Tipos = ["Fuego", "Agua", "Planta","Normal","Lucha","Bicho","Dragon","Electrico","Fantasma","Hielo",
                   "Psiquico","Roca","Tierra","Veneno","Volador","Hada"]

    for i in range (cTipos):
        print(f"Tipo {i+1}\n")
        for j in range (len(lista_Tipos)):
            print(f"{j+1}){lista_Tipos[j]}")
        opt = opciones(1,len(lista_Tipos))

        tipo = lista_Tipos[opt-1]

        #Eliminar el tipo seleccionado
        del lista_Tipos[opt-1]

        if i>0:
            f.write("/")
        f.write(tipo)

def modPokemon():
    #todo TENGO QUE TERMINAR ESTE MODULO CUANDO NO ME DE PEREZA xD
    f = open("pokedex.txt","r+")
    pokemon = f.readlines()
    print(f"Que Pokemon quieres modificar? Total {len(pokemon)}")
    num = opciones(1,len(pokemon))-1
    for i in range(len(pokemon)):
        if i == num:
            print(pokemon[num])
            print("Que campo quieres modificar\n1.ID\n2.Nombre\n3.Tipos\n4.Nada")
            opt = opciones(1,4)
            if opt == 1:
                nuevaID = input("Que numero quieres que sea la nueva ID?")
            elif opt == 2:
                nuevoNombre = input("Nuevo nombre: ")
                linea = pokemon[num]
                print(f"El nuevo nombre sera {pokemon[num].split('#')[1]} -> {nuevoNombre}")
                print(linea.split("#")[1])
                linea.split("#")[1] = nuevoNombre
                print(linea.split("#")[1])

                print(linea)
            elif opt == 3:
                print("Cuantos tipos tiene el Pokemon? 1 o 2")
                opt = opciones(1,2)
            elif opt == 4:
                return 

def verPokemon():
    f = open("pokedex.txt","r+")
    pokemon = f.readlines()
    print(f"Hay un total de {len(pokemon)} Pokemon.\nCual quieres ver?")
    nID = opciones(1,len(pokemon))
    for i in range (len(pokemon)):
        segundoT = False
        if i+1 == nID:
            print("="*40+"\n"+"ID".ljust(5)+"Nombre".ljust(15)+"Tipo 1".ljust(10),end="")
            try:
                if pokemon[i].split("#")[2].split("/")[1]:
                    print("Tipo 2".ljust(10),end="")
                    segundoT = True
            except:
                print(end="")
            print("\n"+"="*40)
            if segundoT == True:
                print(pokemon[i].split("#")[0].ljust(5)+pokemon[i].split("#")[1].ljust(15)+pokemon[i].split("#")[2].split("/")[0].ljust(10)+pokemon[i].split("#")[2].split("/")[1].ljust(10))
            else:
                print(pokemon[i].split("#")[0].ljust(5)+pokemon[i].split("#")[1].ljust(15)+pokemon[i].split("#")[2].ljust(10))

def eliminarPokemon():
    f = open("pokedex.txt", "r+")
    pokemon = f.readlines()
    f.close()
    print(f"Hay un total de {len(pokemon)} Pokemon.\nCual quieres eliminar?")
    nID = opciones(1, len(pokemon))
    for i in range(len(pokemon)):
        if i + 1 == nID:
            f = open("pokedex.txt","w+")
            del pokemon[nID-1]
            print(pokemon)
            print(f"El Pokemon: {pokemon[i-1].split('#')[1]}\nHa sido eliminado ")
            f.writelines(pokemon)