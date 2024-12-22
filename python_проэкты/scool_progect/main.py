from Func import *

                                #win
win = tk.Tk()
win.geometry("1000x1000")
win.resizable(False, False)
win.config(bg = "#6F4F28")


                                #canvas

canvas = tk.Canvas(win, height=1006, width=1006)
canvas.config(bg="#6F4F28", )
canvas.place(x = -3, y = -3)

                                #figuri

canvas.create_rectangle(300,1,700,50)



label = tk.Label(win, text = "-Helper-", font=("", "25", "bold"), bg = "#6F4F28")
label.place(x = 435, y = 5)

label = tk.Label(win, text = "разделы", font=("", "20", ""), bg = "#6F4F28")
label.place(x = 440, y = 75)



Converter = tk.Button(win, text = "конвертер", font=("", "20", ""), bg = "#B07D2B", height="1", width="10", command=Department_Converter)
Converter.place(x = 15, y = 130)

Weather = tk.Button(win, text = "погода", font=("", "20", ""), bg = "#B07D2B", height="1", width="10", command=Department_Wheather)
Weather.place(x = 215, y = 130)

Сurrency = tk.Button(win, text = "валюта", font=("", "20", ""), bg = "#B07D2B", height="1", width="10", command=Department_Currency)
Сurrency.place(x = 415, y = 130)

Time = tk.Button(win, text = "время", font=("", "20", ""), bg = "#B07D2B", height="1", width="10", command=Department_Time)
Time.place(x = 615, y = 130)

Translater = tk.Button(win, text = "переводчик", font=("", "20", ""), bg = "#B07D2B", height="1", width="10")
Translater.place(x = 815, y = 130)
win.mainloop()


