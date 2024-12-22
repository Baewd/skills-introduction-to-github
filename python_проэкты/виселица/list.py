import random

def ran_wor() :
    list = {
        1: "дом",
        2: "машина",
        3: "квадрат",
        4: "триугольник",
        5: "дорога",
        6: "красный",
        7: "ананас",
    }

    ran =random.randint(1, 7)
    data = list[ran]
    return data


def list_data(data) :
    a=[]
    for i in data:
        a.append(i)
    return a


def num1(word):
    a=0
    for i in word:
        a += 1
    return a