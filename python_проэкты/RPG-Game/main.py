from VS import *


class Pers :
    name = None
    HP = None
    inventory = None
    class_plaer = None
    chans = None
    ATK = None

    def __init__(self, inp_name, inp_class_plaer, HP, inventory, chans,ATK):  # готово
        self.name = inp_name
        self.class_plaer = inp_class_plaer
        self.Hp = HP
        self.inventory = inventory
        self.chans = chans
        self.ATK = ATK

class vrag :
    ATK = None
    HP = None
    def __init__(self, ATK, HP):
        self.ATK= ATK
        self.HP= HP

print("приветствую в моей RPG игре")
inp_name = input("введи ник игрока>> ")
print("есть 3 класса ")
print("1- разбойник (+10 к шансу уклонится от атаки) ")            #готово
print("2- халк (+50 HP  -10 ATK) ")                                #готов
print("3 - медик- (восттонавливает 1% Hp ) ")                      #неготов
inp_class_plaer = input("выберите класс перснажа")                 #готово

ATK = 20
repit =True
chans = 10
HP = 100
inventory = None

if inp_class_plaer == 1 :
    chans +=10
elif inp_class_plaer == 2 :
    HP += 50                                                       #готово
    ATK -= 10


Plaer = Pers(inp_name, inp_class_plaer, HP, inventory, chans, ATK)
input("1 бой будет обучающий готовы начать?")
list_start = [
    [" ", " ", " ", " ", " "],
    [" ", " ", "V", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", "I", " ", " "],
]
first_vrag= vrag(5, 50)

# while first_vrag.HP > 0 :
#     baf = input("хотите выпить зелье?")
#     print("у вас пока нет зелий)")
#     print_list(list_start)
#     print("I - это вы V - это враг")
#     print("у врага ", first_vrag.HP, "хп")
#     print("вы отакуете 1вым")
vrag.HP= 100
Figh_Hp= Plaer.Hp
while repit == True :
    play= int(input("выбирите игру 1- прокачка 2 - +зельки 3- бос(+ броня/оружие)"))
    list= VS_list(play)
    # print_list(list)

    fight_D(list, play,Figh_Hp, vrag.HP)
