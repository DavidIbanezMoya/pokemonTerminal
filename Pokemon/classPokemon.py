# import random
#
# from Pokemon import tipos as t
#
#
# class Pokemon():
#
#     def __init__(self):
#         self.nombre = ""
#         self.tipos = []
#         self.nivel = 1
#         self.vida = 100
#         self.vidaActual = self.vida
#         self.velocidad = 50
#         self.ataque = 25
#         self.defensa = 25
#         self.total = self.ataque+self.defensa+self.velocidad
#         self.movimientos = []
#     def __str__(self):
#
#         tipos = self.mostrarTipos()
#
#         caja = "-"*42+"\n|"+" "*40+"|"+"\n|"+self.nombre.rjust(10)+"Lvl = ".rjust(28)+str(self.nivel)+"|\n"+"|".ljust(15)+tipos.ljust(26)+"|\n"+"-"*42
#         cajaStats = "\n|"+"Vida: ".ljust(11)+str(self.vidaActual)+"/"+str(self.vida).ljust(25)+"|\n|"+\
#         "Ataque: ".ljust(11)+str(self.ataque).ljust(29)+"|\n|"+"Defensa: ".ljust(11)+str(self.defensa).ljust(29)\
#         +"|\n|"+"Velocidad: ".ljust(11)+str(self.velocidad).ljust(29)+"|\n|"+"Total: ".ljust(11)+str(self.total).ljust(29)+"|\n"+"-"*42
#
#         caja +=cajaStats
#         return caja
#
#     def mostrarTipos (self):
#         #Un Pokemon solo puede tener 2 tipos como maximo, no deberia petar
#
#         #tipos = ""
#
#         if len(self.tipos) == 1:
#             tipos = t.tipo.nombre()
#         else:
#             tipos = self.tipos[0].nombre +"/"+self.tipos[1].nombre
#
#
#         return str(tipos).replace("\n","")
#
#     def idAleatorio(self):
#         f = open("pokedexES.txt", "r+")
#         pokemon = f.readlines()
#         return int(random.randint(0,(len(pokemon)-1)))
#
#     def generarPokemon(self,id):
#         #id = int(input("Que ID quieres? "))
#         #print("Has elegido el Pokemon con ID ->"+str(id))
#         f = open("pokedexES.txt", "r+")
#         pokemon = f.readlines()
#         linea = pokemon[id-1]
#         self.nombre = linea.split("#")[1]
#         monotype = True
#         cantidadTipos = 1
#         criterio = self
#
#         try:
#             #Si tiene 2 tipos o mas habra que dividrlos luego
#             linea.split("#")[2].split("/")
#             monotype = False
#
#
#             #Verificar si hay mas de un tipo
#             linea.split("#")[2].split("/")[0]
#             linea.split("#")[2].split("/")[1]
#
#             if linea.split("#")[2].split("/")[0] in t.tiposExistentes:
#                 cantidadTipos = 2
#             criterio = linea.split("#")[2].split("/")[0]
#
#         except:
#             print("",end="")
#         if monotype == True:
#             #Si no los tiene simplemente podremos anadir lo que haya despues
#             #self.tipos.append(linea.split("#")[2])
#             criterio = linea.split("#")[2]
#
#         print("Abans")
#         for i in range(cantidadTipos):
#             #Diccionario de tipos
#             for j in t.tiposExistentes:
#                 #Dentro de cada tipo
#                 for k in j:
#                 #Se ira buscando cual es el tipo, en la tabla para crear un nuevo objeto tipo y ponerselo al Poke
#                     try:
#                         #todo No coincide con el if con lo cual no se asigna y por eso peta, pq intenta buscar pero esta vacio
#                         if k.isalpha() and criterio and "Fuego" in k:
#                             print("Afegit")
#                             self.tipos.append(t.tipoFuego.nombre)
#                     except:
#                         print("",end="")
#
#         # todo if elif para instanciar el tipo del pokemon
#         self.nivel = random.randint(75,88)
#         self.vida = random.randint(50,100)
#         self.vida += round(2.5*self.nivel)
#         self.velocidad = random.randint(20,80)
#         self.velocidad += round(1.4*self.nivel)
#         self.ataque = random.randint(25,75)
#         self.ataque += round(2.6*self.nivel)
#         self.defensa = random.randint(35,65)
#         self.defensa += round(2.2*self.nivel)
#         self.total = self.ataque+self.defensa+self.velocidad
#
#         self.vidaActual = self.vida
#
#         #---Movimientos----
#
#
#
#         #todo Que los tipos se impriman correctamente sin el \n
#
#         #print("El Pokemon generado ha sido:\n"+self.nombre+"\nTipos = "+str(self.tipos)+"\nNivel: "+str(self.nivel)
#         #      +"\nVida: "+str(self.vida)+"\nVelocidad: "+str(self.velocidad)+"\nAtaque: "+str(self.ataque)+"\nDefensa: "+str(self.defensa))
#
#     def golpeado (self,dano):
#         self.vidaActual = self.defensa - dano
#
#     def golpear (self):
#         dano = self.ataque
#         return dano

import random

from Pokemon import types as t


class Pokemon():

    def __init__(self):
        self.name = ""
        self.types = []
        self.level = 1
        self.hp = 100
        self.current_hp = self.hp
        self.speed = 50
        self.attack = 25
        self.defense = 25
        self.total_stats = self.attack + self.defense + self.speed
        self.moves = []

    def __str__(self):

        types = self.showTypes()

        box = "-" * 42 + "\n|" + " " * 40 + "|\n|" + self.name.rjust(10) + "Lvl = ".rjust(28) + str(self.level) + "|\n" + "|".ljust(15) + types.ljust(26) + "|\n" + "-" * 42
        stats_box = "\n|" + "HP: ".ljust(11) + str(self.current_hp) + "/" + str(self.hp).ljust(25) + "|\n|" + \
                    "Attack: ".ljust(11) + str(self.attack).ljust(29) + "|\n|" + "Defense: ".ljust(11) + str(self.defense).ljust(29) \
                    + "|\n|" + "Speed: ".ljust(11) + str(self.speed).ljust(29) + "|\n|" + "Total Stats: ".ljust(11) + str(self.total_stats).ljust(29) + "|\n" + "-" * 42

        box += stats_box
        return box

    def showTypes(self):

        if len(self.types) == 1:
            types = t.type.name()
        else:
            types = self.types[0].name + "/" + self.types[1].name

        return str(types).replace("\n", "")

    def randomID(self):
        f = open("pokedexEN.txt", "r+")
        pokemon = f.readlines()
        return int(random.randint(0, (len(pokemon) - 1)))

    def generatePokemon(self, id):
        f = open("pokedexEN.txt", "r+")
        pokemon = f.readlines()
        line = pokemon[id - 1]
        self.name = line.split("#")[1]
        monotype = True
        type_count = 1
        criteria = self

        try:
            line.split("#")[2].split("/")
            monotype = False

            line.split("#")[2].split("/")[0]
            line.split("#")[2].split("/")[1]

            if line.split("#")[2].split("/")[0] in t.existingTypes:
                type_count = 2
            criteria = line.split("#")[2].split("/")[0]

        except:
            print("", end="")

        if monotype == True:
            criteria = line.split("#")[2]

        print("Before")
        for i in range(type_count):
            for j in t.existingTypes:
                for k in j:
                    try:
                        if k.isalpha() and criteria and "Fire" in k:
                            print("Added")
                            self.types.append(t.FireType.name)
                    except:
                        print("", end="")

        self.level = random.randint(75, 88)
        self.hp = random.randint(50, 100)
        self.hp += round(2.5 * self.level)
        self.speed = random.randint(20, 80)
        self.speed += round(1.4 * self.level)
        self.attack = random.randint(25, 75)
        self.attack += round(2.6 * self.level)
        self.defense = random.randint(35, 65)
        self.defense += round(2.2 * self.level)
        self.total_stats = self.attack + self.defense + self.speed
        self.current_hp = self.hp

    def takeDamage(self, damage):
        self.current_hp = self.defense - damage

    def attack(self):
        damage = self.attack
        return damage
