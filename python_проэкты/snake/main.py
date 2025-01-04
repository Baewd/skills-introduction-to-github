import random
import time
import tkinter as tk
import keyboard

                            #tkinter_win
win = tk.Tk()
win.geometry("600x600")
win.config(bg="black")
win.resizable(False, False)



go = True
max_index_list_snake = 1
direction = None
start_time = time.time()
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
    global  list_snake, go, max_index_list_snake, direction
    # direction = "right"
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
                if ii == " " or ii == "A":
                    ii = 0
                else:
                    go = False

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
    global  list_snake, go, max_index_list_snake, direction
    # direction = "left"
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
        if (list_snake[index_turn_list])[index_turn] == " " or (list_snake[index_turn_list])[index_turn] == "A":
            (list_snake[index_turn_list])[index_turn] = 1
        else:
            go = False
    else:
        go = False


def Turn_up():
    global list_snake, max_index_list_snake, go, direction
    # direction = "up"

    new_list = []
    a = -1
    index_turn_list = None
    index_turn = None

    for i in list_snake:

        a += 1
        new_list_list = []
        index = -1


        for ii in i:
            index += 1

            if ii == 1:
                index_turn_list = a - 1
                index_turn = index



            if type(ii) == int:  # увеличение номера тела

                if ii < max_index_list_snake:
                    new_list_list.append(ii + 1)  # увеличение всех индексов на 1

                else:
                    new_list_list.append(" ")  # удаление хвоста

            else:
                new_list_list.append(ii)  # добавление пустоты

        new_list.append(new_list_list)
    list_snake = new_list

    a = -1
    new_list = []
    new_list_list = []


    for i in list_snake:
        a += 1
        index = -1
        new_list_list = []
        for ii in i:
            index += 1
            if index == index_turn:
                if a == index_turn_list:
                    if ii == " " or ii == "A":
                        ii = 1
                    else:
                        go = False

            new_list_list.append(ii)


        new_list.append(new_list_list)

    list_snake = new_list


def Turn_down():
    global list_snake, max_index_list_snake, go, direction
    # direction = "down"

    new_list = []
    a = -1
    index_turn_list = None
    index_turn = None

    for i in list_snake:

        a += 1
        new_list_list = []
        index = -1


        for ii in i:
            index += 1

            if ii == 1:
                index_turn_list = a + 1
                index_turn = index



            if type(ii) == int:  # увеличение номера тела

                if ii < max_index_list_snake:
                    new_list_list.append(ii + 1)  # увеличение всех индексов на 1

                else:
                    new_list_list.append(" ")  # удаление хвоста

            else:
                new_list_list.append(ii)  # добавление пустоты

        new_list.append(new_list_list)
    list_snake = new_list

    a = -1
    new_list = []
    new_list_list = []


    for i in list_snake:
        a += 1
        index = -1
        new_list_list = []
        for ii in i:
            index += 1
            if index == index_turn:
                if a == index_turn_list:
                    if ii == " " or ii == "A":
                        ii = 1
                    else:
                        go = False
            new_list_list.append(ii)


        new_list.append(new_list_list)

    list_snake = new_list


def aplee():
    global list_snake, max_index_list_snake

    new_apple = True
    append_apple = True

    for i in list_snake:
        for ii in i:
            if ii == "A":
                new_apple = False
                break

    if new_apple == True:
        max_index_list_snake += 1

        while append_apple == True:

            index_list = random.randint(0, 8)
            index_list_list = random.randint(0, 8)

            if ((list_snake[index_list])[index_list_list]) == " ":
                ((list_snake[index_list])[index_list_list]) = "A"
                append_apple = False


def direction_l():
    global direction
    direction = "left"

def direction_r():
    global direction
    direction = "right"

def direction_u():
    global direction
    direction = "up"

def direction_d():
    global direction
    direction = "down"


def button():
    global left_button, right_button, up_button, down_button, direction

    left_button = tk.Button(win, text = "<" ,bg = "black", fg = "green", command= direction_l)
    right_button = tk.Button(win, text = ">" , bg = "black", fg = "green", command= direction_r)
    up_button = tk.Button(win, text = "^" , bg = "black", fg = "green", command= direction_u)
    down_button = tk.Button(win, text = "v" ,bg = "black", fg = "green", command= direction_d)

    left_button.place(x = 100, y = 100)
    right_button.place(x = 200, y = 200)
    up_button.place(x = 300, y = 300)
    down_button.place(x = 400, y = 400)

button()


while go == True:                   #начало цикла игры


    win.update()



    if start_time + 2 < time.time() :       #проверка прошло ли 2 секуны
        start_time = time.time()


        if direction == "right":
            Turn_right()

        if direction == "left":
            Turn_left()

        if direction == "up":
            Turn_up()

        if direction == "down":
            Turn_down()

        aplee()

        print("")
        for i in list_snake:  # вывод
            print(i)
        print('')



    for i in list_snake:                #проверка на наличие головы
        for ii in i:
            if ii == 1:
                new_go = True
    go = new_go

    if go == False:                     #завершение игры
        list_snake = "sory noob"


    new_go = False
    # a = input("направление")
    #
    #
    # if a == "a" or a == "ф":        #left
    #     Turn_left()
    #
    # if a == "d" or a == "в":        #right
    #     Turn_right()
    #
    # if a == "w" or a == "ц":        #up
    #     Turn_up()
    #
    # if a == "s" or a == "ы":        #down
    #     Turn_down()


win.mainloop()





