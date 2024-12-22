import random
import tkinter as tk
import time
from my_def import *

win = tk.Tk()
win.resizable(False, False)
win.geometry("500x700")
win.config(bg = "black")



list = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

sleep = 1
compleat_play = False
old_number_figure = -1
new_figura = False

def Destroy():
    global hello_destroe_button, hello_label

    hello_label.destroy()
    hello_destroy_button.destroy()
    Start()


def Sleep():
    global sleep
    if sleep > 0.3:
        sleep -= 0.2


def Start():
    global canvas, button_left, button_right, button_revers

    canvas = tk.Canvas(win, bg="black", width=504, height=704, borderwidth=-2)          #create canvas
    canvas.create_rectangle( 100, 6, 400, 504, outline = "#006400", width = 5)          #create rectangle
    canvas.place(x = -2, y = -2)

    button_left = tk.Button(win,text = "<", fg = "black", bg= "#006400",                #create button_left
    font = ("", "17",""), activeforeground = "#006400", command = Turn_left)
    button_left.place(x = 180, y = 550)

    button_right = tk.Button(win,text = ">", fg = "black", bg= "#006400",                #create button_right
    font = ("", "17",""), activeforeground = "#006400", command = Turn_right)
    button_right.place(x = 280, y = 550)

    button_revers = tk.Button(win,text = "@", fg = "black", bg= "#006400",                #create button_revers
    font = ("", "17",""), activeforeground = "#006400", command =Sleep, width=2)
    button_revers.place(x = 230, y = 550)

    Play()


def Start_destroy():
    global canvas, button_left, button_right, button_revers


    button_left = tk.Button(win,text = "<", fg = "black", bg= "#006400",                #create button_left
    font = ("", "17",""), activeforeground = "#006400", command = Turn_left)
    button_left.place(x = 180, y = 550)

    button_right = tk.Button(win,text = ">", fg = "black", bg= "#006400",                #create button_right
    font = ("", "17",""), activeforeground = "#006400", command = Turn_right)
    button_right.place(x = 280, y = 550)

    button_revers = tk.Button(win,text = "@", fg = "black", bg= "#006400",                #create button_revers
    font = ("", "17",""), activeforeground = "#006400", command =Sleep, width=2)
    button_revers.place(x = 230, y = 550)



def Create_button():
    global  button_left, button_right, button_revers
    button_left.destroy()
    button_right.destroy()
    button_revers.destroy()

    button_left = tk.Button(win,text = "<", fg = "black", bg= "#006400",                #create button_left
    font = ("", "17",""), activeforeground = "#006400", command = Turn_left)
    button_left.place(x = 180, y = 550)

    button_right = tk.Button(win,text = ">", fg = "black", bg= "#006400",                #create button_right
    font = ("", "17",""), activeforeground = "#006400", command = Turn_right)
    button_right.place(x = 280, y = 550)

    button_revers = tk.Button(win,text = "@", fg = "black", bg= "#006400",                #create button_revers
    font = ("", "17",""), activeforeground = "#006400", command = Sleep , width=2)
    button_revers.place(x = 230, y = 550)


def Revers():
    pass


def Turn_left():
    global list

    can_return = True
    dop_list = list
    compleat = True


    for list_list in list:
        a = -1
        for i in list_list:
            a +=1
            if ((i == "o") and (a == 0)):
                can_return = False

    if can_return == True:
        for list_list in list:
            a = -1
            for i in list_list:
                a += 1

                if ((i == "o") and ((list_list[a - 1] == "x") or (list_list[a] == "x"))):
                    compleat = False

                if (compleat == True and a != 0 and (i == "o") and ((list_list[a - 1] == "o") or (list_list[a - 1] == " "))):
                    list_list[a-1] = "o"
                    list_list[a] = " "

    display_list(list)
    win.update()


def Turn_right():
    global list
    list_right = Revers(list)
    can_return = True
    dop_list = list
    compleat = True

    for list_list in list:
        a = -1
        for i in list_list:
            a +=1
            if ((i == "o") and (a == 9)):
                can_return = False

    if can_return == True:
        for list_list in list_right:
            a = -1
            for i in list_list:
                a += 1

                if i == "o" and list_list[a - 1] == "x":
                    compleat = False

                if ( a != 0 and (i == "o") and ((list_list[a - 1] == "o") or (list_list[a - 1] == " "))):
                    list_list[a-1] = "o"
                    list_list[a] = " "

        list = Revers(list_right)

    if compleat == False:
        list = dop_list

    display_list(list)
    win.update()


def Revers(list):
    new_list_list = []
    new_list = []
    for list_list in list:
        for i in reversed(list_list):
            new_list_list.append(i)
        new_list.append(new_list_list)
        new_list_list = []
    return new_list


def Turn_down():
    global list, new_figura
#все переменные:
    number_list = -1
    num_list = []
    dictionary_append = []
    new_list = []
    compleat = True
    compleat_2 = True
    compleat_3 = True
    dop_list = list
    nado_displey_list = False
    new_figura = True


#удаление всех o и сохранение их положения в "dictionary_append"
    for list_list in list:
        number_list +=1
        a = -1
        new_list_list = []

        for i in list_list:
            a += 1

            if i == "o" :
                i = " "

                # if number_list == 17:
                #     compleat = False
                dictionary_append.append([{number_list: a}])
            new_list_list.append(i)
        new_list.append(new_list_list)

    list = new_list
    new_list_list = []

#замена пустаты на "x" ниже положения чем "o" был до этого
    try:
        for keys in dictionary_append:

            for i in keys:

                for key in i:
                    a = -1
                    new_list_list = []

                    # проход по нужному листу
                    for O in list[key + 1]:
                        a+=1

                        # проверка можно ли двигаться в низ
                        if i[key] == a:
                            if O == "x":
                                compleat_3 = False

                        # замена пустоты на "x"
                        if i[key] == a:
                            O = "o"

                        new_list_list.append(O) #перезапись нужного листа


                    list[key + 1] = new_list_list   #перезапись самого листа
                    a = -1

                    # проверка можно ли двигаться в низ
                    try:
                         for O in list[key + 2]:
                            a+=1
                            if i[key] == a:
                                if O == "x":
                                    compleat_2 = False

                    except:
                        pass
    except:
        pass
# else:
# new_list_list = []
# new_list = []
        # for list_list in list:
        #     new_list_list = []
        #     for i in list_list:
        #         if i == "o":
        #             i = "x"
        #         new_list_list.append(i)
        #     new_list.append(new_list_list)
        # list = new_list


    dictionary_append = []
    new_list_list = []
    number_list = -1

    #пост проверка дошёл ли o до конца
    for list_list in list:
        number_list +=1
        a = -1
        new_list_list = []

        for i in list_list:
            a += 1

            if i == "o" :

                if number_list == 21:
                    compleat = False
                    new_figura = True

    #замена o на x если o дошёл до конца
    if compleat == False:
        new_list_list = []
        new_list = []
        for list_list in list:
            new_list_list = []
            for i in list_list:
                if i == "o":
                    i = "x"
                new_list_list.append(i)
            new_list.append(new_list_list)
        list = new_list

    # замена o на x при прямрой встрече с  x
    if compleat_2 == False:

        new_list_list = []
        new_list = []
        for list_list in list:
            new_list_list = []
            for i in list_list:
                if i == "o":
                    i = "x"
                new_list_list.append(i)
            new_list.append(new_list_list)
        list = new_list

    #замена o на x если сдвинуть перед x
    if compleat_3 == False:
        new_list_list = []
        new_list = []
        for list_list in dop_list:
            new_list_list = []
            for i in list_list:
                if i == "o":
                    i = "x"
                new_list_list.append(i)
            new_list.append(new_list_list)
        list = new_list


    new_list = []
    empty_list = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    #замена 10 x в ряд на пробел
    for list_list in list:
        int_X = 0
        empty_for_list = empty_list
        for i in list_list:
            if i == "x":
                int_X += 1
        if int_X == 10:
            new_list = empty_for_list + new_list
            nado_displey_list = True

        else:
            new_list.append(list_list)


    if nado_displey_list == True:
        display_list(list)
        win.update()
        time.sleep(0.2)
        display_list(new_list)
        win.update()
        time.sleep(0.2)
        display_list(list)
        win.update()
        time.sleep(0.2)

    list = new_list


    #обновление данных на экране
    display_list(list)
    win.update()

    for i in list:
        for m in i:
            if m == "o":
                new_figura = False

    if new_figura == True:
        new_figura = True
        Create_figure()


def Create_figure():
    global list_figure, list, old_number_figure, compleat_play
    new_list = []
    go = False

    number_figure = random.randint(0, 15)

    for i in list[0:4]:
        for list_list in i :
            if list_list == "x":
                compleat_play = True


    while go == False:
        if number_figure != old_number_figure:
            old_number_figure = number_figure
            go = True
        else:
            number_figure = random.randint(0, 15)

    list_a = list_figure[number_figure]

    list[4] = list_a[0]
    list[3] = list_a[1]
    list[2] = list_a[2]
    list[1] = list_a[3]



def display_list(list):
    global  label_list_tetris

    try:
        label_list_tetris.destroy()
    except:
        print("1")

    str_list_tetris = ""

    for i in list[4 : ]:  # создание  label листа

        str_list_tetris += ((str(i) + "\n").replace((","), ""))
        str_list_tetris = str_list_tetris.replace("'", "")
        str_list_tetris = str_list_tetris.replace("[", "")
        str_list_tetris = str_list_tetris.replace("]", "")

    label_list_tetris = tk.Label(win, text=f"{str_list_tetris[0: -1]}", bg="black", fg="#006400",
                                 font=("Courier", "18", ""))
    label_list_tetris.place(x=110, y=8)


def Play():
    global list, compleat_play

    Create_figure()
    display_list(list)

    now_time = time.time()
    while compleat_play == False:

        display_list(list)
        win.update()
        if (now_time + sleep) <= (time.time()):
            now_time = time.time()
            Turn_down()



hello_label = tk.Label(win,text = "добро пожадовать \n \nв тетрис",bg = "black",fg = "#006400",font = ("", "38", "bold"))
hello_label.place(x = 10, y = 200)

hello_destroy_button = tk.Button(win,text = "начать", fg = "#006400", bg= "#051a09", font = ("", "17",""),
                                 borderwidth = -2, command = Destroy)
hello_destroy_button.place(x = 200, y = 400)


win.mainloop()
