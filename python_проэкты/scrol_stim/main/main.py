import tkinter as tk
# from PIL import ImageTk

                                        #создание окна

win = tk.Tk()

win.title("скрол")
win.geometry("1000x1000")
win.config(bg="#1b2838")
win.resizable(False, False)


                                        #логика скрола

def scrol(list, storona):
    global index_photo, max_index, post, win, canvas, cub_1, cub_2, cub_3, cub_4



    if storona == "right":
        index_photo += 1
        if index_photo > max_index:
            index_photo = 0

    elif storona == "left":
        index_photo -= 1
        if index_photo < 0 :
            index_photo = max_index
    canvas.destroy()
    index = list[index_photo]

    canvas = tk.Canvas(win, width=750, height=400, bg="#1b2838", bd=-2)

    canvas.place(x=120, y=200)

    post = tk.PhotoImage(file = index)

    canvas.create_image(0,0,anchor="nw", image=post)

    cub_1.destroy()
    cub_2.destroy()
    cub_3.destroy()
    cub_4.destroy()


    if index_photo == 0:
        cub_1 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="White")
        cub_2 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_3 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_4 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")


    elif index_photo == 1:
        cub_1 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_2 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="White")
        cub_3 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_4 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")


    elif index_photo == max_index:
        cub_1 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_2 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_3 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_4 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="White")


    else:
        cub_1 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_2 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
        cub_3 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="White")
        cub_4 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")

    if max_index >=0 :

        cub_1.place(x=450, y=605)

    if max_index >= 1:

        cub_2.place(x=465, y=605)

    if max_index >= 3:

        cub_3.place(x=480, y=605)

    if max_index >= 2:
        if max_index == 2:
            cub_4.place(x=480, y=605)
        else:
            cub_4.place(x=495, y=605)








                                        #скролы в стороны

def left():
    global list, index_photo
    scrol(list, "left")


def right():
    global list, index_photo
    scrol(list, "right")



                                        #индекс фото


def def_max_index(list):
    a = -1
    for i in list:
        a += 1
    return a


                                        #переменныее


index_photo = 0
list = []


file = open("data_photo/data", "r")

for line in file:
    line = line[:-1]
    list.append(line)



file.close()


max_index = def_max_index(list)





hello = tk.Label(text="старые но не забытые", font=("","30",""), bg="#1b2838", fg="white", bd=15)



left_scrol= tk.Button(command=left, text="<", font=("","20",""), bg="#1b2838", fg="white", bd=15, height=5)

right_scrol= tk.Button(command=right, text=">", font=("","20",""), bg="#1b2838", fg="white", bd=15, height=5)

canvas = tk.Canvas(win, width=750, height=400, bg="#1b2838", bd=-2)

canvas.place(x=120, y=200)

post = tk.PhotoImage(file="photo/1.png")

canvas.create_image(0, 0, anchor="nw", image=post)

cub_1 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="White")
cub_2 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
cub_3 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")
cub_4 = tk.Label(win, text=".", font=("", "30", ""), bg="#1b2838", fg="Black")

if max_index >= 0:
    cub_1.place(x=450, y=605)

if max_index >= 1:
    cub_2.place(x=465, y=605)

if max_index >= 3:
    cub_3.place(x=480, y=605)

if max_index >= 2:
    if max_index == 2:
        cub_4.place(x=480, y=605)
    else:
        cub_4.place(x=495, y=605)



hello.pack()
left_scrol.place(x=35, y =300)
right_scrol.place(x=900, y = 300)


win.mainloop()

