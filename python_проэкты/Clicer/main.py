import tkinter as tk
from PIL import ImageTk


win= tk.Tk()

                                            #экран
win.title("diner")
win.geometry("900x1000")
win.config(bg="#00008B")
win.resizable(False, False)

                                            #save

def red_data():
    global moni, lvl_up_Clik, Klic_mony, moni_label, Cake, lvl, cost

    file = open("D:\\програмирование\\python_проэкты\\Clicer\dist\\data.txt", "r")

    Klic_mony = None
    moni = None
    lvl=None
    cost = None



    a = 0
    for line in file :
        line = int(line)
        a +=1
        if a ==1:
            moni = line

        elif a ==2:
            Klic_mony = line

        elif a ==3:
            lvl = line

        elif a ==4:
            cost = line

    if moni == None:
        moni = 0

    if cost == None:
        cost = 10

    if lvl == None:
        lvl = 1

    if Klic_mony == None:
        Klic_mony = 1

    file.close()

red_data()

Cat = ImageTk.PhotoImage(file="D:\\програмирование\\python_проэкты\\Clicer\\Cat_2.jpg")


                                            #Def



def ol_label():

    global moni, lvl_up_Clik, Klic_mony, moni_label, Cake, lvl, repeat

    moni_label.destroy()

    moni_label = tk.Label(win, text=f"{moni}", bg="#00008B", fg="silver", font=("", "25", "bold"), bd=10)

    Cake.destroy()

    Cake = tk.Button(win, image=Cat, command=Klic, height=600, width=500,bg="#00008B")

    lvl_up_Clik.destroy()

    lvl_up_Clik = tk.Button(win, text=f"lvl {lvl+1}-{cost}", command=lvl_up, font=("", "25", "bold"), bg="#4169E1",fg="Silver")

    repeat.destroy()

    repeat = tk.Button(win, text="начать заново", command=clear_data, font=("", "25", "bold"), bg="#4169E1", fg="Silver")

    moni_label.pack()
    Cake.pack()
    lvl_up_Clik.pack()
    repeat.pack()



def Klic():

    global moni,lvl_up_Clik, Klic_mony, moni_label, Cake, lvl

    moni += Klic_mony

    ol_label()
    save_data()


def lvl_up():
    global lvl, moni, Klic_mony, cost
    if moni >= cost :
        if ((lvl >= 1) and (lvl <10)) :
            moni -=cost
            procent =round(cost * 0.1)
            cost = cost + procent
            Klic_mony += 1
            lvl += 1

        elif ((lvl >= 10) and (lvl < 20)):
            moni -= cost
            procent =round(cost * 0.25)
            cost = cost + procent
            Klic_mony += 1
            lvl += 1

        elif ((lvl >= 20) and (lvl < 40)):
            moni -= cost
            procent =round(cost * 0.5)
            cost = cost + procent
            Klic_mony += 1
            lvl += 2

        elif ((lvl >= 40) and (lvl < 100)):
            moni -= cost
            procent = round(cost * 2)
            cost = cost + procent
            Klic_mony += 1
            lvl += 2

    ol_label()
    save_data()


def save_data():
    global moni, Klic_mony, lvl, cost
    # file= open("file/data.txt", "a")
    # file.write(str(moni) + "\n")
    # file.close()
    file = open("D:\\програмирование\\python_проэкты\\Clicer\dist\\data.txt", "w")
    file.write(str(moni) + "\n")
    file.write(str(Klic_mony) + "\n")
    file.write(str(lvl) + "\n")
    file.write(str(cost) + "\n")
    file.close()


def clear_data():
    global moni, Klic_mony, lvl, cost

    moni = None
    Klic_mony= None
    lvl= None
    cost= None

    with open("D:\\програмирование\\python_проэкты\\Clicer\dist\\data.txt", "w"):
        pass

    red_data()
    ol_label()




                                #label
str_hele = tk.Label(win, text="Cat ", bg="#00008B" , fg="#D3D3D3", font=("","35","bold"),  bd=10 )

str_hele.pack()

moni_label = tk.Label(win, text=f"{moni}", bg="#00008B" , fg="Silver", font=("","25","bold"),  bd=10)

moni_label.pack()


                                  #Button

Cake = tk.Button(win, image=Cat, command=Klic, height=600,width=500, compound="center", bg="#F0FFF0")

Cake.pack()

lvl_up_Clik =tk.Button (win, text=f"lvl {lvl+1}-{cost}", command=Klic, font=("","25","bold"), bg="#4169E1", fg="Silver")

lvl_up_Clik.pack()

repeat = tk.Button(win, text="начать заново", command=clear_data, font=("","25","bold"), bg="#4169E1", fg="Silver")

repeat.pack()
                              #упаковка



                               #после этого не писать ничего

win.mainloop()
win.des