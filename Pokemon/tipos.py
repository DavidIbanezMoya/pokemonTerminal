class tipo():

    def __init__(self):
        #tiposExistentes = [[1, "Fuego"], [2, "Agua"], [3, "Planta"], [4, "Hada"], [5, "Acero"], [6, "Siniestro"], [7, "Dragon"],
        #         [8, "Fantasma"], [9, "Roca"], [10, "Bicho"], [11, "Psiquico"], [12, "Volador"], [13, "Tierra"], [14, "Veneno"],
        #         [15, "Lucha"], [16, "Hielo"],[17, "Electrico"], [18, "Normal"]]
        self.nombre = ""
        self.idTipo = ""
        self.fuerteContra = []
        self.debilContra = []
        self.noFuerteContra = []
        self.inmune = []
        self.movimientos = []
    def nombre (self):
        self.nombre()

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
#Movimientos -> Nombre,Potencia,Precision

class tipoFuego(tipo):
    nombre = "Fuego"
    idTipo = 1
    fuerteContra = ["Acero","Hielo","Planta","Bicho"]
    noFuerteContra = ["Agua","Roca","Fuego","Dragon"]
    debilContra = ["Agua","Roca","Tierra"]
    movimientos = [["Rueda Fuego",60,100],["Llamarada",95,85]]


class tipoAgua(tipo):
    nombre = "Agua"
    idTipo = 2
    fuerteContra = ["Roca","Tierra","Fuego"]
    noFuerteContra = ["Agua","Planta","Dragon"]
    debilContra = ["Planta","Electrico"]
    movimientos = [["Pistola Agua",60,100],["HidroBomba",95,85]]

class tipoPlanta(tipo):
    nombre = "Planta"
    idTipo = 3
    fuerteContra = ["Agua","Roca","Tierra"]
    noFuerteContra = ["Acero","Volador","Planta","Bicho","Veneno","Fuego","Dragon"]
    debilContra = ["Volador","Hielo","Bicho","Fuego","Veneno"]
    movimientos = [["Hoja Afilada",60,100],["Energibola",95,85]]

class tipoHada(tipo):
    nombre = "Hada"
    idTipo = 4
    fuerteContra = ["Lucha","Dragon","Siniestro"]
    noFuerteContra = ["Acero","Veneno","Fuego"]
    debilContra = ["Acero","Veneno"]
    inmune = ["Dragon"]
    movimientos = [["Beso Dulce",60,100],["Fuerza Lunar",95,85]]

class tipoAcero(tipo):
    nombre = "Acero"
    idTipo = 5
    fuerteContra = ["Roca","Hielo","Hada"]
    noFuerteContra = ["Agua","Acero","Fuego","Electrico"]
    debilContra = ["Fuego","Lucha","Tierra"]
    inmune = ["Veneno"]
    movimientos = [["Puño Acero",60,100],["Cola Ferrea",95,85]]

class tipoSiniestro(tipo):
    nombre = "Siniestro"
    idTipo = 6
    fuerteContra = ["Psiquico","Fantasma"]
    noFuerteContra = ["Lucha","Hada","Siniestro"]
    debilContra = ["Bicho","Lucha","Hada"]
    inmune = ["Psiquico"]
    movimientos = [["Mordisco",60,100],["Triturar",95,85]]

class tipoDragon(tipo):
    nombre = "Dragon"
    idTipo = 7
    fuerteContra = ["Dragon"]
    noFuerteContra = ["Acero"]
    debilContra = ["Hielo","Hada","Dragon"]
    movimientos = [["Cola Dragon",60,100],["Cola Dragon",95,85]]

class tipoFantasma(tipo):
    nombre = "Fantasma"
    idTipo = 8
    fuerteContra = ["Psiquico","Fantasma"]
    noFuerteContra = ["Siniestro"]
    debilContra = ["Fantasma","Siniestro"]
    inmune = ["Normal","Lucha"]
    movimientos = [["Lenguetazo",60,100],["Golpe Vil",95,85]]

class tipoRoca(tipo):
    nombre = "Roca"
    idTipo = 9
    fuerteContra = ["Agua","Hielo","Bicho","Fuego"]
    noFuerteContra = ["Acero","Tierra","Lucha"]
    debilContra = ["Acero","Agua","Planta","Tierra","Lucha"]
    movimientos = [["Roca Afilada",60,100],["Avalancha",95,85]]

class tipoBicho(tipo):
    nombre = "Bicho"
    idTipo = 10
    fuerteContra = ["Planta","Psiquico","Siniestro"]
    noFuerteContra = ["Acero","Agua","Fuego","Lucha","Hada","Veneno","Dragon"]
    debilContra = ["Agua","Roca","Fuego"]
    movimientos = [["Chupa Vidas",60,100],["Zumbido",95,85]]

class tipoPsiquico(tipo):
    nombre = "Psiquico"
    idTipo = 11
    fuerteContra = ["Lucha","Veneno"]
    noFuerteContra = ["Acero","Psiquico"]
    debilContra = ["Bicho","Dragon","Siniestro"]
    movimientos = [["Confusion",60,100],["Psiquico",95,85]]

class tipoVolador(tipo):
    nombre = "Volador"
    idTipo = 12
    fuerteContra = ["Planta","Bicho","Lucha"]
    noFuerteContra = ["Acero","Roca","Electrico"]
    debilContra = ["Hielo","Roca","Electrico"]
    movimientos = [["Golpe Aereo",60,100],["Vuelo",95,85]]

class tipoTierra(tipo):
    nombre = "Tierra"
    idTipo = 13
    fuerteContra = ["Acero","Electrico","Roca","Fuego","Veneno"]
    noFuerteContra = ["Planta","Bicho"]
    debilContra = ["Agua","Hielo","Planta"]
    inmune = ["Electrico"]
    movimientos = [["Terratemblor",60,100],["Terremoto",95,85]]

class tipoVeneno(tipo):
    nombre = "Veneno"
    idTipo = 14
    fuerteContra = ["Planta","Hada"]
    noFuerteContra = ["Roca","Tierra","Veneno","Fantasma"]
    debilContra = ["Tierra","Psiquico"]
    movimientos = [["Lanza Mugre",60,100],["Cola Veneno",95,85]]

class tipoLucha(tipo):
    nombre = "Lucha"
    idTipo = 15
    fuerteContra = ["Acero","Hielo","Normal","Roca","Siniestro"]
    noFuerteContra = ["Volador","Bicho","Hada","Psiquico","Veneno"]
    debilContra = ["Volador","Hada","Psiquico"]
    movimientos = [["Puntapie",60,100],["Patada S.Alta",95,85]]

class tipoHielo(tipo):
    nombre = "Hielo"
    idTipo = 16
    fuerteContra = ["Volador","Planta","Tierra","Dragon"]
    noFuerteContra = ["Agua","Acero","Fuego","Hielo"]
    debilContra = ["Fuego","Acero","Roca","Lucha"]
    movimientos = [["Rayo Hielo",60,100],["Frio Polar",95,85]]

class tipoElectrico(tipo):
    nombre = "Electrico"
    idTipo = 17
    fuerteContra = ["Volador","Agua"]
    noFuerteContra = ["Planta","Dragon","Electrico"]
    debilContra = ["Tierra"]
    movimientos = [["Rayo",60,100],["Trueno",95,85]]

class tipoNormal(tipo):
    nombre = "Normal"
    idTipo = 18
    fuerteContra = []
    noFuerteContra = ["Acero","Roca"]
    debilContra = ["Lucha"]
    inmune = ["Fantasma"]
    movimientos = [["Golpe Cuerpo",60,100],["Pisoton",95,85]]


tiposExistentes = [[1, "Fuego"], [2, "Agua"], [3, "Planta"], [4, "Hada"], [5, "Acero"], [6, "Siniestro"], [7, "Dragon"],
                   [8, "Fantasma"], [9, "Roca"], [10, "Bicho"], [11, "Psiquico"], [12, "Volador"], [13, "Tierra"],
                   [14, "Veneno"],
                   [15, "Lucha"], [16, "Hielo"], [17, "Electrico"], [18, "Normal"]]