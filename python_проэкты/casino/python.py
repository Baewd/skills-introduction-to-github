import random
bank = 100
otvet = 0
while True:
    play = 1
    while play != ("да") :
        play = input("хочешь сыграть?")

    print ("это хорошо")
    print ("игры : рулетка- 1, казино- 2")
    i=int(input ("выбери игру"))
    if i == 1:                                        #рулетка
        print ("рулетка это хороший выбор ")
        ran = random.random()
        if ran >= 0.5 :                               #рандом
            ran = 1
        else :
            ran = 0
        print("ваш банк = ", bank, "$")
        stavka =int(input ("ставьте ставку сир)"))
        while stavka > bank :
            data = ("снизьте ставку у вас есть только", bank , "$")
            stavka = int(input (data))
        input ("готовы? мне всёравно)")
        if ran == 0 :
           print ("ты выиграл) ", stavka)
           stavka *=2
           bank += stavka
        else:
            bank -= stavka
            print ("мне жаль) ты потерял", stavka)
    if i == 2 :                                        #казик
        print("казино это хороший выбор ")
        otvet = int(input ("как хотите поставить на число-1 или на цвет-2"))
    if otvet == 1 :
        ran =random. randint(1, 36)                               #рандом
        num = int (input ("введите число на кторое хотите поставить?"))
        stavka = int (input ("сколько хотите поставить сир?"))
        if num == ran :
            stavka *= 36
            bank += stavka
            print ("вы выиграли :", stavka, "$")
        if num != ran :
            bank -= stavka
            print ("увы ты проиграл и потерял", stavka, "$")
    if otvet== 2 :                                                         #цвет
        print  ("есть 3 цвета чёрный, зелёный, крастный")
        col = input ("введите цвет на которое хотите поставить(ТОЛЬКО БУКВЫ ТОЧ В ТОЧ)")
        stavka = int(input("сколько хотите поставить сир?"))
        ran = random.randint(0, 36)
        if ran== 0 and col == "зелёный"  :
            stavka *=100
            bank += stavka
            print ("вы выиграли :", stavka, "$")
        elif 0 < ran >= 18 and col == ("чёрный"):
            stavka *= 3
            bank += stavka
            print("вы выиграли :", stavka, "$")
        elif 18 < ran >= 36 and col == ("крастный"):
            stavka *= 3
            bank += stavka
            print("вы выиграли :", stavka, "$")
        else :
            print ("мне очень жаль ты проиграл")
            bank -=stavka