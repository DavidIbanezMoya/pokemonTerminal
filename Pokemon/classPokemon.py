import random

class Pokemon():

    def __init__(self):
        self.nombre = ""
        self.tipos = []
        self.nivel = 1
        self.vida = 100
        self.vidaActual = self.vida
        self.velocidad = 50
        self.ataque = 25
        self.defensa = 25
        self.total = self.ataque+self.defensa+self.velocidad
    def __str__(self):

        tipos = self.mostrarTipos()

        caja = "-"*42+"\n|"+" "*40+"|"+"\n|"+self.nombre.rjust(10)+"Lvl = ".rjust(28)+str(self.nivel)+"|\n"+"|".ljust(15)+tipos.ljust(26)+"|\n"+"-"*42
        cajaStats = "\n|"+"Vida: ".ljust(11)+str(self.vidaActual)+"/"+str(self.vida).ljust(25)+"|\n|"+\
        "Ataque: ".ljust(11)+str(self.ataque).ljust(29)+"|\n|"+"Defensa: ".ljust(11)+str(self.defensa).ljust(29)\
        +"|\n|"+"Velocidad: ".ljust(11)+str(self.velocidad).ljust(29)+"|\n|"+"Total: ".ljust(11)+str(self.total).ljust(29)+"|\n"+"-"*42

        caja +=cajaStats
        return caja

    def mostrarTipos (self):
        #Un Pokemon solo puede tener 2 tipos como maximo, no deberia petar
        tipos = ""

        if len(self.tipos) == 1:
            tipos = self.tipos[0]
        else:
            tipos = self.tipos[0]+"/"+self.tipos[1]


        return str(tipos).replace("\n","")

    def idAleatorio(self):
        f = open("pokedex.txt", "r+")
        pokemon = f.readlines()
        return int(random.randint(0,(len(pokemon)-1)))

    def generarPokemon(self,id):
        #id = int(input("Que ID quieres? "))
        #print("Has elegido el Pokemon con ID ->"+str(id))
        f = open("pokedex.txt","r+")
        pokemon = f.readlines()
        linea = pokemon[id-1]
        self.nombre = linea.split("#")[1]
        monotype = True

        try:
            linea.split("#")[2].split("/")
            monotype = False
            self.tipos.append(linea.split("#")[2].split("/")[0])
            self.tipos.append(linea.split("#")[2].split("/")[1])
        except:
            print("",end="")
        if monotype == True:
            self.tipos.append(linea.split("#")[2])

        self.nivel = random.randint(75,88)
        self.vida = random.randint(50,100)
        self.vida += round(2.5*self.nivel)
        self.velocidad = random.randint(20,80)
        self.velocidad += round(1.4*self.nivel)
        self.ataque = random.randint(25,75)
        self.ataque += round(2.6*self.nivel)
        self.defensa = random.randint(35,65)
        self.defensa += round(2.2*self.nivel)
        self.total = self.ataque+self.defensa+self.velocidad

        self.vidaActual = self.vida
        #todo Que los tipos se impriman correctamente sin el \n

        #print("El Pokemon generado ha sido:\n"+self.nombre+"\nTipos = "+str(self.tipos)+"\nNivel: "+str(self.nivel)
        #      +"\nVida: "+str(self.vida)+"\nVelocidad: "+str(self.velocidad)+"\nAtaque: "+str(self.ataque)+"\nDefensa: "+str(self.defensa))

    def golpeado (self,dano):
        self.vidaActual = self.defensa - dano

    def golpear (self):
        dano = self.ataque
        return dano

