import tkinter as tk
from main import *


                #ВИД ОКНА_____________________________________
win= tk.Tk()

win.title("лабиринт")
win.geometry("600x600")
win.config(bg="black")
win.resizable(False, False)


                #ПЕРЕМЕННЫЕ __________________________________
play= None
lvl= None
label = None
E = True
                #DEF___________________________________________
def deliat_Play():
    Play.destroy()
    lvl_str.pack()
    lvl_1.pack()
    lvl_2.pack()
    lvl_3.pack()



def print_list():
    global list, label
    label_text = '\n'.join(' '.join(map(str, sublist)) for sublist in list)
    label = tk.Label(text=label_text, bg="black", fg="#00FA9A" , font=("Courier","15",""))

    label.pack()


def Button_lvl(lvl):
    global lvl_str, lvl_1, lvl_2, lvl_3, list, a, s, w, d

    lvl_str.destroy()
    lvl_1.destroy()
    lvl_2.destroy()
    lvl_3.destroy()

    list= random_list(lvl)
    print_list()

    w.place(x =280, y= 350)
    a.place(x =240, y= 400)
    s.place(x =280, y= 400)
    d.place(x =320, y= 400)




def Button_lvl_1():
    lvl = 1

    Button_lvl(lvl)

def Button_lvl_2():
    lvl = 2

    Button_lvl(lvl)

def Button_lvl_3():
    lvl = 3

    Button_lvl(lvl)


def Button_asd():
    global a, s, d, w, label

    label.destroy()
    w.destroy()
    a.destroy()
    s.destroy()
    d.destroy()

    if E == True:
        print_list()
        label.pack()

        w = tk.Button(win, text="^", font=("Courier", "15", "bold"), bg="#2F4F4F", fg="#00FA9A", bd=5, command=w_def)
        a = tk.Button(win, text="<", font=("Courier", "15", "bold"), bg="#2F4F4F", fg="#00FA9A", bd=5, command=a_def)
        s = tk.Button(win, text="v", font=("Courier", "15", "bold"), bg="#2F4F4F", fg="#00FA9A", bd=5, command=s_def)
        d = tk.Button(win, text=">", font=("Courier", "15", "bold"), bg="#2F4F4F", fg="#00FA9A", bd=5, command=d_def)

        w.place(x =280, y= 350)
        a.place(x =240, y= 400)
        s.place(x =280, y= 400)
        d.place(x =320, y= 400)
    else:
        label.destroy()
        w.destroy()
        a.destroy()
        s.destroy()
        d.destroy()
        wiin = tk.Label(win, text="ты победил ", font=("Courier", "45", "bold"), bg="Black", fg="#00FA9A", bd=15)
        wiin_win = tk.Label(win, text="поздравляю ", font=("Courier", "45", "bold"), bg="Black", fg="#00FA9A")
        wiin.place(x=90,y=150)
        wiin_win.place(x=105,y=250)





def w_def():

    logica("w")

    Button_asd()
    pass

def a_def():

    logica("a")

    Button_asd()
    pass

def s_def():

    logica("s")

    Button_asd()

    pass

def d_def():

    logica("d")

    Button_asd()



    pass


def logica(hod):
    global list, E
    global a, s, d, w, label
    index = my_index(list)
    if hod == "a":
        list = abc(index, list, " ", "-1")
        index -= 1
        list = abc(index, list, "p", "-1")
    elif hod == "d":
        list = abc(index, list, " ", "1")
        index += 1
        list = abc(index, list, "p", "1")
    elif hod == "w":
        list = abc(index, list, " ", "-5")
        index -= 10
        list = abc(index, list, "p", "-5")
    elif hod == "s":
        list = abc(index, list, " ", "+5")
        index += 10
        list = abc(index, list, "p", "+5")

    E = surch_e(list)






def my_index(list):
    a = 0
    for i in list :
        for ii in i :
            if ii == "p" :
                return a
            else :
                a+=1



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



                #label________________________________________
label_tityl= tk.Label(win, text="добро пожаловать в лабиринт)", bg="black" , fg="#00FA9A", font=("","10","bold"))

lvl_str = tk.Label(win, text="выберите уровень сложности :", pady = 20, anchor="n", bg="black", fg="#32CD32", font=("","15","bold"))


                #button________________________________________
Play=tk.Button(win, text=">",font=("","50","bold" ) , command=deliat_Play, bg="black", fg="#4B0082", height="40", width="90")

lvl_1 = tk.Button(win, text="уровень 1", command=Button_lvl_1, bg="black", fg="#9932CC", bd=5, font=("","20","bold"))
lvl_2 = tk.Button(win, text="уровень 2", command=Button_lvl_2, bg="black", fg="#9932CC", bd=5, font=("","20","bold"))
lvl_3 = tk.Button(win, text="уровень 3", command=Button_lvl_3, bg="black", fg="#9932CC", bd=5, font=("","20","bold"))


#кнопки перемещения

w = tk.Button(win, text="^", font=("Courier","15","bold"), bg="#2F4F4F", fg="#00FA9A",bd=5, command=w_def )
a = tk.Button(win, text="<", font=("Courier","15","bold"), bg="#2F4F4F", fg="#00FA9A",bd=5, command=a_def )
s = tk.Button(win, text="v", font=("Courier","15","bold"), bg="#2F4F4F", fg="#00FA9A",bd=5, command=s_def )
d = tk.Button(win, text=">", font=("Courier","15","bold"), bg="#2F4F4F", fg="#00FA9A",bd=5, command=d_def )


label_tityl.pack()
Play.pack()

win.mainloop()
















