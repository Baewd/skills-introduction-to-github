import tkinter as tk
import keyboard

go = True
max_index_list_snake = 1
list_snake = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ',  1 , ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]

def Turn_right():
    global  list_snake, go, max_index_list_snake
    new_list = []
    a = -1


    for i in list_snake:

        a += 1
        new_list_list = []
        index = -1
        index_turn = None

        for ii in i:
            index += 1

            if ii == 1:
                index_turn = index + 1

            if index_turn == index:     #добавление головы
                ii = 0

            if type(ii) == int:     #увеличение номера тела

                if ii < max_index_list_snake:
                    new_list_list.append(ii + 1)        #увеличение всех индексов на 1

                else:
                    new_list_list.append(" ")           #удаление хвоста

            else:
                new_list_list.append(ii)        #добавление пустоты


        new_list.append(new_list_list)
    list_snake = new_list


def Turn_left():
    global  list_snake, go, max_index_list_snake
    new_list = []
    a = -1
    index_turn = 0
    index_turn_list = 0
    index_turn = None

    for i in list_snake:

        a += 1
        new_list_list = []
        index = -1

        for ii in i:
            index += 1

            if ii == 1:                 #проверка на голову
                index_turn = index - 1
                index_turn_list = a

            if type(ii) == int:     #увеличение номера тела
                if ii < max_index_list_snake:
                    new_list_list.append(ii + 1)

                else:
                    new_list_list.append(" ")

            else:
                new_list_list.append(ii)        #добавление пустоты


        new_list.append(new_list_list)
    list_snake = new_list
    if index_turn > -1:
        (list_snake[index_turn_list])[index_turn] = 1


while go == True:
    new_go = False
    i = input()
    if i == "1":
        Turn_left()
    else:
        Turn_right()


    for i in list_snake:
        for ii in i:
            if ii == 1:
                new_go = True
    go = new_go

    if go == False:
        list_snake = "sory noob"

    for i in list_snake:
        print(i)