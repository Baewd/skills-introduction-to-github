import os
import tkinter as tk
from sys import flags

win = tk.Tk()
win.title("pyinstaller")
win.geometry("600x700")
win.resizable(False, False)
win.config(bg = "Black")

tk_otvet = tk.StringVar()
tk_otvet.set("yes")

def pyinst():
    global tkint, pyt_ent, icon_ent, tk_otvet
    otvet = tk_otvet.get()
    pyt = pyt_ent.get()
    icon = icon_ent.get()
    whorld =""
    compleat_pyt= ""
    file = ""
    if pyt != "" and pyt[-3] + pyt[-2] + pyt[-1] == ".py" :
        ind = 0
        for i in pyt :
            whorld +=i
            if i == "\\":
                compleat_pyt += whorld + "\\"
                whorld = ""
                file = ""
            else:
                file += i


        command_consol = "pyinstaller --onefile "
        if otvet == "yes":
            command_consol += "-w "
        if icon != "":
            command_consol += "-i " +"\""+ f"{icon}" + "\" "

        os.chdir(compleat_pyt)

        command_consol += file
        os.system(command_consol)
        create = tk.Label(win, text = "готово", font = ("", "25", ""), fg = "green", bg = "Black")
        create.place(x = 250, y = 400)



hello = tk.Label(win, text = "добро пожаловать в installer", font = ("", "15", "bold"), fg = "green", bg = "Black")

pyt_pyt = tk.Label(win, text = "введите полый путь до файла :", font = ("", "13", ""), fg = "green", bg = "Black")
pyt_ent = tk.Entry(win, bg = "#006400",  width = 50)

icon_pyt = tk.Label(win, text = "введите полый путь до иконки :", font = ("", "13", ""), fg = "green", bg = "Black")
icon_ent = tk.Entry(win, bg = "#006400",  width = 50)

label_tk = tk.Label(win, text = "нужна консоль в проге?", font = ("", "12", ""), fg = "green", bg = "Black")
tkint = tk.Checkbutton(win, fg ="green", bg = "Black", variable = tk_otvet, offvalue="yes", onvalue="no")

compleat = tk.Button(win, text = "начать", fg = "green", bg = "Black", width=9, height=2, font = ("", "15", "bold"), command = pyinst)


hello.place(x = 160, y = 10)

pyt_pyt.place(x = 20, y = 60)
pyt_ent.place(x = 270, y= 65)

icon_pyt.place(x = 20, y = 120)
icon_ent.place(x = 270, y = 120)

label_tk.place(x = 20, y = 170)
tkint.place(x = 200, y = 171 )

compleat.place(x = 250, y = 300)

win.mainloop()
