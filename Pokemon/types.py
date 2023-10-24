# class tipo():
#
#     def __init__(self):
#         #tiposExistentes = [[1, "Fuego"], [2, "Agua"], [3, "Planta"], [4, "Hada"], [5, "Acero"], [6, "Siniestro"], [7, "Dragon"],
#         #         [8, "Fantasma"], [9, "Roca"], [10, "Bicho"], [11, "Psiquico"], [12, "Volador"], [13, "Tierra"], [14, "Veneno"],
#         #         [15, "Lucha"], [16, "Hielo"],[17, "Electrico"], [18, "Normal"]]
#         self.nombre = ""
#         self.idTipo = ""
#         self.fuerteContra = []
#         self.debilContra = []
#         self.noFuerteContra = []
#         self.inmune = []
#         self.movimientos = []
#     def nombre (self):
#         self.nombre()
#
#     def fuerte (self):
#         self.fuerte = True
#
#     def debil (self):
#         self.debil = False
#
#     def inmune (self):
#         self.inmune = False
#
#     def informacion (self):
#         print("Nombre: ",self.nombre,"\nId del Tipo: ",self.idTipo,"\nFuerte: ",self.fuerte
#               ,"\nDebil: ",self.debil,"\nNo fuerte contra: ",self.noFuerteContra,"\nInmune: ",self.inmune)
#
#
#
# #todo Reducir y aumentar el dano de los ataques que va a recibir
# #Movimientos -> Nombre,Potencia,Precision
#
# class tipoFuego(tipo):
#     nombre = "Fuego"
#     idTipo = 1
#     fuerteContra = ["Acero","Hielo","Planta","Bicho"]
#     noFuerteContra = ["Agua","Roca","Fuego","Dragon"]
#     debilContra = ["Agua","Roca","Tierra"]
#     movimientos = [["Rueda Fuego",60,100],["Llamarada",95,85]]
#
#
# class tipoAgua(tipo):
#     nombre = "Agua"
#     idTipo = 2
#     fuerteContra = ["Roca","Tierra","Fuego"]
#     noFuerteContra = ["Agua","Planta","Dragon"]
#     debilContra = ["Planta","Electrico"]
#     movimientos = [["Pistola Agua",60,100],["HidroBomba",95,85]]
#
# class tipoPlanta(tipo):
#     nombre = "Planta"
#     idTipo = 3
#     fuerteContra = ["Agua","Roca","Tierra"]
#     noFuerteContra = ["Acero","Volador","Planta","Bicho","Veneno","Fuego","Dragon"]
#     debilContra = ["Volador","Hielo","Bicho","Fuego","Veneno"]
#     movimientos = [["Hoja Afilada",60,100],["Energibola",95,85]]
#
# class tipoHada(tipo):
#     nombre = "Hada"
#     idTipo = 4
#     fuerteContra = ["Lucha","Dragon","Siniestro"]
#     noFuerteContra = ["Acero","Veneno","Fuego"]
#     debilContra = ["Acero","Veneno"]
#     inmune = ["Dragon"]
#     movimientos = [["Beso Dulce",60,100],["Fuerza Lunar",95,85]]
#
# class tipoAcero(tipo):
#     nombre = "Acero"
#     idTipo = 5
#     fuerteContra = ["Roca","Hielo","Hada"]
#     noFuerteContra = ["Agua","Acero","Fuego","Electrico"]
#     debilContra = ["Fuego","Lucha","Tierra"]
#     inmune = ["Veneno"]
#     movimientos = [["Puño Acero",60,100],["Cola Ferrea",95,85]]
#
# class tipoSiniestro(tipo):
#     nombre = "Siniestro"
#     idTipo = 6
#     fuerteContra = ["Psiquico","Fantasma"]
#     noFuerteContra = ["Lucha","Hada","Siniestro"]
#     debilContra = ["Bicho","Lucha","Hada"]
#     inmune = ["Psiquico"]
#     movimientos = [["Mordisco",60,100],["Triturar",95,85]]
#
# class tipoDragon(tipo):
#     nombre = "Dragon"
#     idTipo = 7
#     fuerteContra = ["Dragon"]
#     noFuerteContra = ["Acero"]
#     debilContra = ["Hielo","Hada","Dragon"]
#     movimientos = [["Cola Dragon",60,100],["Cola Dragon",95,85]]
#
# class tipoFantasma(tipo):
#     nombre = "Fantasma"
#     idTipo = 8
#     fuerteContra = ["Psiquico","Fantasma"]
#     noFuerteContra = ["Siniestro"]
#     debilContra = ["Fantasma","Siniestro"]
#     inmune = ["Normal","Lucha"]
#     movimientos = [["Lenguetazo",60,100],["Golpe Vil",95,85]]
#
# class tipoRoca(tipo):
#     nombre = "Roca"
#     idTipo = 9
#     fuerteContra = ["Agua","Hielo","Bicho","Fuego"]
#     noFuerteContra = ["Acero","Tierra","Lucha"]
#     debilContra = ["Acero","Agua","Planta","Tierra","Lucha"]
#     movimientos = [["Roca Afilada",60,100],["Avalancha",95,85]]
#
# class tipoBicho(tipo):
#     nombre = "Bicho"
#     idTipo = 10
#     fuerteContra = ["Planta","Psiquico","Siniestro"]
#     noFuerteContra = ["Acero","Agua","Fuego","Lucha","Hada","Veneno","Dragon"]
#     debilContra = ["Agua","Roca","Fuego"]
#     movimientos = [["Chupa Vidas",60,100],["Zumbido",95,85]]
#
# class tipoPsiquico(tipo):
#     nombre = "Psiquico"
#     idTipo = 11
#     fuerteContra = ["Lucha","Veneno"]
#     noFuerteContra = ["Acero","Psiquico"]
#     debilContra = ["Bicho","Dragon","Siniestro"]
#     movimientos = [["Confusion",60,100],["Psiquico",95,85]]
#
# class tipoVolador(tipo):
#     nombre = "Volador"
#     idTipo = 12
#     fuerteContra = ["Planta","Bicho","Lucha"]
#     noFuerteContra = ["Acero","Roca","Electrico"]
#     debilContra = ["Hielo","Roca","Electrico"]
#     movimientos = [["Golpe Aereo",60,100],["Vuelo",95,85]]
#
# class tipoTierra(tipo):
#     nombre = "Tierra"
#     idTipo = 13
#     fuerteContra = ["Acero","Electrico","Roca","Fuego","Veneno"]
#     noFuerteContra = ["Planta","Bicho"]
#     debilContra = ["Agua","Hielo","Planta"]
#     inmune = ["Electrico"]
#     movimientos = [["Terratemblor",60,100],["Terremoto",95,85]]
#
# class tipoVeneno(tipo):
#     nombre = "Veneno"
#     idTipo = 14
#     fuerteContra = ["Planta","Hada"]
#     noFuerteContra = ["Roca","Tierra","Veneno","Fantasma"]
#     debilContra = ["Tierra","Psiquico"]
#     movimientos = [["Lanza Mugre",60,100],["Cola Veneno",95,85]]
#
# class tipoLucha(tipo):
#     nombre = "Lucha"
#     idTipo = 15
#     fuerteContra = ["Acero","Hielo","Normal","Roca","Siniestro"]
#     noFuerteContra = ["Volador","Bicho","Hada","Psiquico","Veneno"]
#     debilContra = ["Volador","Hada","Psiquico"]
#     movimientos = [["Puntapie",60,100],["Patada S.Alta",95,85]]
#
# class tipoHielo(tipo):
#     nombre = "Hielo"
#     idTipo = 16
#     fuerteContra = ["Volador","Planta","Tierra","Dragon"]
#     noFuerteContra = ["Agua","Acero","Fuego","Hielo"]
#     debilContra = ["Fuego","Acero","Roca","Lucha"]
#     movimientos = [["Rayo Hielo",60,100],["Frio Polar",95,85]]
#
# class tipoElectrico(tipo):
#     nombre = "Electrico"
#     idTipo = 17
#     fuerteContra = ["Volador","Agua"]
#     noFuerteContra = ["Planta","Dragon","Electrico"]
#     debilContra = ["Tierra"]
#     movimientos = [["Rayo",60,100],["Trueno",95,85]]
#
# class tipoNormal(tipo):
#     nombre = "Normal"
#     idTipo = 18
#     fuerteContra = []
#     noFuerteContra = ["Acero","Roca"]
#     debilContra = ["Lucha"]
#     inmune = ["Fantasma"]
#     movimientos = [["Golpe Cuerpo",60,100],["Pisoton",95,85]]
#
#
# tiposExistentes = [[1, "Fuego"], [2, "Agua"], [3, "Planta"], [4, "Hada"], [5, "Acero"], [6, "Siniestro"], [7, "Dragon"],
#                    [8, "Fantasma"], [9, "Roca"], [10, "Bicho"], [11, "Psiquico"], [12, "Volador"], [13, "Tierra"],
#                    [14, "Veneno"],
#                    [15, "Lucha"], [16, "Hielo"], [17, "Electrico"], [18, "Normal"]]

class Type:

    def __init__(self):
        self.name = ""
        self.type_id = ""
        self.strong_against = []
        self.weak_against = []
        self.not_strong_against = []
        self.immune = []
        self.moves = []

    def type_name(self):
        self.name()

    def strong(self):
        self.strong = True

    def weak(self):
        self.weak = False

    def immune(self):
        self.immune = False

    def information(self):
        print("Name: ", self.name, "\nType ID: ", self.type_id, "\nStrong: ", self.strong, "\nWeak: ",
              self.weak, "\nNot strong against: ", self.not_strong_against, "\nImmune: ", self.immune)


class FireType(Type):
    name = "Fire"
    type_id = 1
    strong_against = ["Steel", "Ice", "Grass", "Bug"]
    not_strong_against = ["Water", "Rock", "Fire", "Dragon"]
    weak_against = ["Water", "Rock", "Ground"]
    moves = [["Fire Wheel", 60, 100], ["Flamethrower", 95, 85]]


class WaterType(Type):
    name = "Water"
    type_id = 2
    strong_against = ["Rock", "Ground", "Fire"]
    not_strong_against = ["Water", "Grass", "Dragon"]
    weak_against = ["Grass", "Electric"]
    moves = [["Water Gun", 60, 100], ["Hydro Pump", 95, 85]]

class GrassType(Type):
    name = "Grass"
    type_id = 3
    strong_against = ["Water", "Rock", "Ground"]
    not_strong_against = ["Steel", "Flying", "Grass", "Bug", "Poison", "Fire", "Dragon"]
    weak_against = ["Flying", "Ice", "Bug", "Fire", "Poison"]
    moves = [["Razor Leaf", 60, 100], ["Energy Ball", 95, 85]]

class FairyType(Type):
    name = "Fairy"
    type_id = 4
    strong_against = ["Fighting", "Dragon", "Dark"]
    not_strong_against = ["Steel", "Poison", "Fire"]
    weak_against = ["Steel", "Poison"]
    immune = ["Dragon"]
    moves = [["Sweet Kiss", 60, 100], ["Moonblast", 95, 85]]

class SteelType(Type):
    name = "Steel"
    type_id = 5
    strong_against = ["Rock", "Ice", "Fairy"]
    not_strong_against = ["Water", "Steel", "Fire", "Electric"]
    weak_against = ["Fire", "Fighting", "Ground"]
    immune = ["Poison"]
    moves = [["Steel Punch", 60, 100], ["Iron Tail", 95, 85]]

class DarkType(Type):
    name = "Dark"
    type_id = 6
    strong_against = ["Psychic", "Ghost"]
    not_strong_against = ["Fighting", "Fairy", "Dark"]
    weak_against = ["Bug", "Fighting", "Fairy"]
    immune = ["Psychic"]
    moves = [["Bite", 60, 100], ["Crunch", 95, 85]]

class DragonType(Type):
    name = "Dragon"
    type_id = 7
    strong_against = ["Dragon"]
    not_strong_against = ["Steel"]
    weak_against = ["Ice", "Fairy", "Dragon"]
    moves = [["Dragon Tail", 60, 100], ["Dragon Tail", 95, 85]]

class GhostType(Type):
    name = "Ghost"
    type_id = 8
    strong_against = ["Psychic", "Ghost"]
    not_strong_against = ["Dark"]
    weak_against = ["Ghost", "Dark"]
    immune = ["Normal", "Fighting"]
    moves = [["Lick", 60, 100], ["Shadow Punch", 95, 85]]

class RockType(Type):
    name = "Rock"
    type_id = 9
    strong_against = ["Water", "Ice", "Bug", "Fire"]
    not_strong_against = ["Steel", "Ground", "Fighting"]
    weak_against = ["Steel", "Water", "Grass", "Ground", "Fighting"]
    moves = [["Rock Slide", 60, 100], ["Avalanche", 95, 85]]

class BugType(Type):
    name = "Bug"
    type_id = 10
    strong_against = ["Grass", "Psychic", "Dark"]
    not_strong_against = ["Steel", "Water", "Fire", "Fighting", "Fairy", "Poison", "Dragon"]
    weak_against = ["Water", "Rock", "Fire"]
    moves = [["Leech Life", 60, 100], ["Buzz", 95, 85]]

class PsychicType(Type):
    name = "Psychic"
    type_id = 11
    strong_against = ["Fighting", "Poison"]
    not_strong_against = ["Steel", "Psychic"]
    weak_against = ["Bug", "Dragon", "Dark"]
    moves = [["Confusion", 60, 100], ["Psychic", 95, 85]]

class FlyingType(Type):
    name = "Flying"
    type_id = 12
    strong_against = ["Grass", "Bug", "Fighting"]
    not_strong_against = ["Steel", "Rock", "Electric"]
    weak_against = ["Ice", "Rock", "Electric"]
    moves = [["Sky Attack", 60, 100], ["Fly", 95, 85]]

class GroundType(Type):
    name = "Ground"
    type_id = 13
    strong_against = ["Steel", "Electric", "Rock", "Fire", "Poison"]
    not_strong_against = ["Grass", "Bug"]
    weak_against = ["Water", "Ice", "Grass"]
    immune = ["Electric"]
    moves = [["Earthquake", 60, 100], ["Earthquake", 95, 85]]

class PoisonType(Type):
    name = "Poison"
    type_id = 14
    strong_against = ["Grass", "Fairy"]
    not_strong_against = ["Steel", "Ground", "Poison", "Ghost"]
    weak_against = ["Ground", "Psychic"]
    moves = [["Sludge", 60, 100], ["Poison Tail", 95, 85]]

class FightingType(Type):
    name = "Fighting"
    type_id = 15
    strong_against = ["Steel", "Ice", "Normal", "Rock", "Dark"]
    not_strong_against = ["Flying", "Bug", "Fairy", "Psychic", "Poison"]
    weak_against = ["Flying", "Fairy", "Psychic"]
    moves = [["Low Kick", 60, 100], ["High Jump Kick", 95, 85]]

class IceType(Type):
    name = "Ice"
    type_id = 16
    strong_against = ["Flying", "Grass", "Ground", "Dragon"]
    not_strong_against = ["Water", "Steel", "Fire", "Ice"]
    weak_against = ["Fire", "Steel", "Rock", "Fighting"]
    moves = [["Ice Beam", 60, 100], ["Blizzard", 95, 85]]

class ElectricType(Type):
    name = "Electric"
    type_id = 17
    strong_against = ["Flying", "Water"]
    not_strong_against = ["Grass", "Dragon", "Electric"]
    weak_against = ["Ground"]
    moves = [["Thunderbolt", 60, 100], ["Thunder", 95, 85]]

class NormalType(Type):
    name = "Normal"
    type_id = 18
    strong_against = []
    not_strong_against = ["Steel", "Rock"]
    weak_against = ["Fighting"]
    immune = ["Ghost"]
    moves = [["Body Slam", 60, 100], ["Stomp", 95, 85]]

existingTypes = [
    [1, "Fire"], [2, "Water"], [3, "Grass"], [4, "Fairy"], [5, "Steel"], [6, "Dark"], [7, "Dragon"],
    [8, "Ghost"], [9, "Rock"], [10, "Bug"], [11, "Psychic"], [12, "Flying"], [13, "Ground"], [14, "Poison"],
    [15, "Fighting"], [16, "Ice"], [17, "Electric"], [18, "Normal"]
]
