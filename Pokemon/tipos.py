class Tipo():

    def __init__(self):
        tipos = [[1, "Fuego"], [2, "Agua"], [3, "Planta"], [4, "Hada"], [5, "Acero"], [6, "Siniestro"], [7, "Dragon"],
                 [8, "Fantasma"], [9, "Roca"], [10, "Bicho"], [11, "Psiquico"], [12, "Volador"], [13, "Tierra"], [14, "Veneno"],
                 [15, "Lucha"], [16, "Hielo"],[17, "Electrico"], [18, "Normal"]]
        self.nombre = ""
        self.idTipo = ""
        self.fuerteContra = []
        self.debilContra = []
        self.noFuerteContra = []
        self.inmune = []

    def fuerte (self):
        self.fuerte = True

    def debil (self):
        self.debil = False

    def inmune (self):
        self.inmune = False

    def informacion (self):
        print("Nombre: ",self.nombre,"\nId del Tipo: ",self.idTipo,"\nFuerte: ",self.fuerte
              ,"\nDebil: ",self.debil,"\nNo fuerte contra: ",self.noFuerteContra,"\nInmune: ",self.inmune)

#todo Reducir y aumentar el dano de los ataques que va a recibir

class tipoFuego(Tipo):
    nombre = "Fuego"
    idTipo = 1
    fuerteContra = ["Acero","Hielo","Planta","Bicho"]
    noFuerteContra = ["Agua","Roca","Fuego","Dragon"]
    debilContra = ["Agua","Roca","Tierra"]


class tipoAgua(Tipo):
    nombre = "Agua"
    idTipo = 2
    fuerteContra = ["Roca","Tierra","Fuego"]
    noFuerteContra = ["Agua","Planta","Dragon"]
    debilContra = ["Planta","Electrico"]

class tipoPlanta(Tipo):
    nombre = "Planta"
    idTipo = 3
    fuerteContra = ["Agua","Roca","Tierra"]
    noFuerteContra = ["Acero","Volador","Planta","Bicho","Veneno","Fuego","Dragon"]
    debilContra = ["Volador","Hielo","Bicho","Fuego","Veneno"]

class tipoHada(Tipo):
    nombre = "Hada"
    idTipo = 4
    fuerteContra = ["Lucha","Dragon","Siniestro"]
    noFuerteContra = ["Acero","Veneno","Fuego"]
    debilContra = ["Acero","Veneno"]
    inmune = ["Dragon"]

class tipoAcero(Tipo):
    nombre = "Acero"
    idTipo = 5
    fuerteContra = ["Roca","Hielo","Hada"]
    noFuerteContra = ["Agua","Acero","Fuego","Electrico"]
    debilContra = ["Fuego","Lucha","Tierra"]
    inmune = ["Veneno"]

class tipoSiniestro(Tipo):
    nombre = "Siniestro"
    idTipo = 6
    fuerteContra = ["Psiquico","Fantasma"]
    noFuerteContra = ["Lucha","Hada","Siniestro"]
    debilContra = ["Bicho","Lucha","Hada"]
    inmune = ["Psiquico"]

class tipoDragon(Tipo):
    nombre = "Dragon"
    idTipo = 7
    fuerteContra = ["Dragon"]
    noFuerteContra = ["Acero"]
    debilContra = ["Hielo","Hada","Dragon"]

class tipoFantasma(Tipo):
    nombre = "Fantasma"
    idTipo = 8
    fuerteContra = ["Psiquico","Fantasma"]
    noFuerteContra = ["Siniestro"]
    debilContra = ["Fantasma","Siniestro"]
    inmune = ["Normal","Lucha"]

class tipoRoca(Tipo):
    nombre = "Roca"
    idTipo = 9
    fuerteContra = ["Agua","Hielo","Bicho","Fuego"]
    noFuerteContra = ["Acero","Tierra","Lucha"]
    debilContra = ["Acero","Agua","Planta","Tierra","Lucha"]

class tipoBicho(Tipo):
    nombre = "Bicho"
    idTipo = 10
    fuerteContra = ["Planta","Psiquico","Siniestro"]
    noFuerteContra = ["Acero","Agua","Fuego","Lucha","Hada","Veneno","Dragon"]
    debilContra = ["Agua","Roca","Fuego"]

class tipoPsiquico(Tipo):
    nombre = "Psiquico"
    idTipo = 11
    fuerteContra = ["Lucha","Veneno"]
    noFuerteContra = ["Acero","Psiquico"]
    debilContra = ["Bicho","Dragon","Siniestro"]

class tipoVolador(Tipo):
    nombre = "Volador"
    idTipo = 12
    fuerteContra = ["Planta","Bicho","Lucha"]
    noFuerteContra = ["Acero","Roca","Electrico"]
    debilContra = ["Hielo","Roca","Electrico"]

class tipoTierra(Tipo):
    nombre = "Tierra"
    idTipo = 13
    fuerteContra = ["Acero","Electrico","Roca","Fuego","Veneno"]
    noFuerteContra = ["Planta","Bicho"]
    debilContra = ["Agua","Hielo","Planta"]
    inmune = ["Electrico"]

class tipoVeneno(Tipo):
    nombre = "Veneno"
    idTipo = 14
    fuerteContra = ["Planta","Hada"]
    noFuerteContra = ["Roca","Tierra","Veneno","Fantasma"]
    debilContra = ["Tierra","Psiquico"]

class tipoLucha(Tipo):
    nombre = "Lucha"
    idTipo = 15
    fuerteContra = ["Acero","Hielo","Normal","Roca","Siniestro"]
    noFuerteContra = ["Volador","Bicho","Hada","Psiquico","Veneno"]
    debilContra = ["Volador","Hada","Psiquico"]

class tipoHielo(Tipo):
    nombre = "Hielo"
    idTipo = 16
    fuerteContra = ["Volador","Planta","Tierra","Dragon"]
    noFuerteContra = ["Agua","Acero","Fuego","Hielo"]
    debilContra = ["Fuego","Acero","Roca","Lucha"]

class tipoElectrico(Tipo):
    nombre = "Electrico"
    idTipo = 17
    fuerteContra = ["Volador","Agua"]
    noFuerteContra = ["Planta","Dragon","Electrico"]
    debilContra = ["Tierra"]

class tipoNormal(Tipo):
    nombre = "Normal"
    idTipo = 18
    fuerteContra = []
    noFuerteContra = ["Acero","Roca"]
    debilContra = ["Lucha"]
    inmune = ["Fantasma"]

fuego =tipoFuego()
fuego.informacion()