import random
from math import factorial


def print_list(list) :
    for i in list :
        print(" ".join(i))    #готово

def random_list(lvl):
    ran = random.randint(1,3)
    if lvl == 1 :
        if ran ==1 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", "p", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 2 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", "p", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 3 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", "p", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
    if lvl == 2 :
        if ran ==1 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", "x", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", "x", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
                ["x", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
                ["x", " ", " ", " ", " ", "x", "x", "x", " ", "x"],
                ["x", "x", " ", "x", "x", "x", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", "x", "p", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 2 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", "x", "x", "x", "x", "x", "x", " ", "x"],
                ["x", " ", " ", "x", " ", " ", " ", "x", " ", "x"],
                ["x", " ", " ", "x", " ", " ", " ", "x", " ", "x"],
                ["x", " ", " ", "x", " ", "x", " ", "x", " ", "x"],
                ["x", " ", " ", "x", " ", "x", "p", "x", " ", "x"],
                ["x", " ", " ", "x", " ", "x", "x", "x", " ", "x"],
                ["x", " ", "E", "x", " ", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 3 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", "x", "x", " ", " ", " ", "x", " ", "x"],
                ["x", " ", " ", " ", "x", "x", "x", "x", " ", "x"],
                ["x", "x", " ", " ", "x", "E", "x", " ", "p", "x"],
                ["x", " ", "x", " ", "x", " ", "x", "x", "x", "x"],
                ["x", " ", " ", " ", "x", " ", " ", " ", " ", "x"],
                ["x", " ", " ", "x", "x", "x", "x", "x", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
    if lvl == 3 :
        if ran ==1 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", "x", " ", "x", "x", " ", " ", "x"],
                ["x", " ", "x", " ", "x", "x", " ", " ", " ", "x"],
                ["x", " ", "x", " ", " ", " ", "x", " ", " ", "x"],
                ["x", " ", " ", " ", "x", " ", " ", "x", " ", "x"],
                ["x", " ", " ", "x", " ", " ", "x", " ", " ", "x"],
                ["x", " ", "x", " ", " ", "x", " ", " ", " ", "x"],
                ["x", "E", " ", "x", " ", " ", " ", "p", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 2 :
            list1_1 = [
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", "p", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
        elif ran == 3 :
            list1_1 = [
               ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", "p", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
                ["x", " ", " ", " ", "E", " ", " ", " ", " ", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ]
    return list1_1

def my_index(list):
    a = 0
    for i in list :
        for ii in i :
            if ii == "p" :
                return a
            else :
                a+=1

def my_surch_index(a, list):
    e = 0
    for i in list :
        if e == a :
            break
        else:
            e+=1
    return i

def abc(a , list, e, ws) :
    otvet = False
    r = 0
    new_list = []
    list_11 = []
    for i in list:
        for ii in i :
            if r == a:
                if ii == "x":
                    r+=1
                    print("выберите дргое направление!!!!!!!")
                    otvet = True
                    list_11.append(ii)

                else:
                    list_11.append(e)
                    r +=1
            else:
                list_11.append(ii)
                r += 1
        new_list.append(list_11)
        list_11=[]
    if otvet == True :
        if ws == "+5" :
            a-=10
            new_list = abc(a, list, "p", "-5")
        elif ws == "-1":
            a += 1
            new_list = abc(a, list, "p", "-1")
        elif ws == "1" :
            a-=1
            new_list= abc(a, list, "p", "1")
        elif ws == "-5" :
            a+= 10
            new_list = abc(a, list, "p", "+5")
    return new_list

def surch_e(list) :
    otvet = False
    for i in list :
        for ii in i :
            if ii == "E" :
                otvet=True
    if otvet == True :
        return otvet
    else:
        return False