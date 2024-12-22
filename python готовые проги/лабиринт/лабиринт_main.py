from def_my import random_list, print_list, my_index, abc, surch_e

E=True
print("вы можите двиготся вверх(w) влево(a) вправо(d) и вниз(s)")

lvl = int(input("какой уровень сложности выбирете(1,2,3)"))
list =random_list(lvl)



while E==True :
    print_list(list)
    hod = input("сделайте ход")
    index = my_index(list)
    if hod == "a" :
        list = abc(index, list, " ", "-1")
        index -=1
        list = abc(index, list, "p", "-1")
    elif hod == "d" :
        list = abc(index, list, " ", "1")
        index +=1
        list = abc(index, list, "p", "1")
    elif hod == "w" :
        list = abc(index, list, " ", "-5")
        index -=10
        list = abc(index, list, "p", "-5")
    elif hod == "s" :
        list = abc(index, list, " ", "+5")
        index +=10
        list = abc(index, list, "p", "+5")
    else:
        print("введите правильную букву")
    E=surch_e(list)
    if E == False :
        print_list(list)
        print("молодец ты победил")
