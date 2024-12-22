import tkinter as tk
import os
import time
from  tkinter import ttk
import requests
from bs4 import BeautifulSoup
import lxml


def open_root():
    global root


    root = tk.Toplevel()
    root.geometry("500x500")
    root.resizable(False, False)
    root.config(bg = "#6F4F28")


def destroy():
    global root


    root.destroy()


                                #converter


def Department_Converter():
    global root, subtype_first, subtype_second, entr_Var, view, coeficent, coeficent_massa

    view = "massa"
    coeficent = ("мг", "г", "кг", "ц", "т")
    coeficent_massa = (1000, 1000, 100, 10)

    open_root()


    canvas = tk.Canvas(root, height=5006, width=5006)
    canvas.config(bg="#6F4F28", )
    canvas.place(x=-3, y=-3)

    canvas.create_rectangle(100, 1, 400, 50)
    canvas.create_rectangle(150, 277, 397, 310)


    convert_titel= tk.Label(root, text = "конвертер", font=("", "23", ""), bg = "#6F4F28")

    convert_titel.place(x = 175, y = 5)

    close = tk.Button(root, text = "<=", font=("", "15", ""), bg = "#6F4F28", command= destroy, width="5")
    close.place(x = 5, y = 5)


    massa = tk.Button(root, text = "massa", font=("", "15", ""), bg = "#6F4F28", command= Massa, width="7")
    massa.place(x = 25, y = 75)

    speed = tk.Button(root, text = "speed", font=("", "15", ""), bg = "#6F4F28", command= Speed, width="7")
    speed.place(x = 145, y = 75)

    distance = tk.Button(root, text = "distance", font=("", "15", ""), bg = "#6F4F28", command= Distance, width="7")
    distance.place(x = 265, y = 75)

    consoles = tk.Button(root, text = "Volume", font=("", "15", ""), bg = "#6F4F28", command= Volume, width="7")
    consoles.place(x = 385, y = 75)


    entr_Var_label = tk.Label(root, text = "введите число:", font=("", "15", ""), bg = "#6F4F28")
    entr_Var_label.place(x = 5, y = 170)

    entr_Var = tk.Entry(root, bg = "#846A20", width=27, font=("", "12", ""))
    entr_Var.place(x = 150, y = 177)

    subtype_first = ttk.Combobox(root, values=coeficent, font=("", "10", ""), width=8)
    subtype_first.current(0)
    subtype_first.place(x = 400, y = 177)

    subtype_second = ttk.Combobox(root, values=coeficent, font=("", "12", ""), width=5)
    subtype_second.current(1)
    subtype_second.place(x = 400, y = 277)

    entr_Var_label = tk.Label(root, text = " получилось: ", font=("", "16", ""), bg = "#6F4F28")
    entr_Var_label.place(x = 5, y = 275)


    run = tk.Button(root, text = " \\  / \nV", font=("", "7", "bold"), bg = "#6F4F28", width=10, command = Converter_math)
    run.place(x = 200, y = 215)


def Converter_math():
    global root, coef1, subtype_first, entr_Var, view, coeficent, coeficent_massa, otvet, str_subtype_first, str_subtype_second, subtype_second, coeficent_volume

    int_entr_Var = int(entr_Var.get())

    try:
        str_subtype_first = subtype_first.get()
    except AttributeError:
        pass

    try:
        str_subtype_second = subtype_second.get()
    except AttributeError:
        pass

    index_suptype_first = coeficent.index(str_subtype_first)
    index_suptype_second = coeficent.index(str_subtype_second)

    if view == "massa":

        if index_suptype_first > index_suptype_second:
            while index_suptype_second <  index_suptype_first:
                int_entr_Var *= coeficent_massa[index_suptype_first - 1]
                index_suptype_first -= 1

        if index_suptype_first < index_suptype_second:
            while index_suptype_second >  index_suptype_first:
                int_entr_Var /= coeficent_massa[index_suptype_second - 1]
                index_suptype_second -= 1

    if view == "distance":

        if index_suptype_first > index_suptype_second:
            while index_suptype_second <  index_suptype_first:
                int_entr_Var *= coeficent_distance[index_suptype_first - 1]
                index_suptype_first -= 1

        if index_suptype_first < index_suptype_second:
            while index_suptype_second >  index_suptype_first:
                int_entr_Var = int_entr_Var / coeficent_distance[index_suptype_second - 1]
                index_suptype_second -= 1


    if view == "volume":

        if index_suptype_first > index_suptype_second:
            while index_suptype_second <  index_suptype_first:
                int_entr_Var *= coeficent_volume[index_suptype_first - 1]
                index_suptype_first -= 1

        if index_suptype_first < index_suptype_second:
            while index_suptype_second >  index_suptype_first:
                int_entr_Var = int_entr_Var / coeficent_volume[index_suptype_second - 1]
                index_suptype_second -= 1

    if view == "speed":

        if ((index_suptype_first < 5 ) and (index_suptype_second < 5)):

            if index_suptype_first > index_suptype_second:
                while index_suptype_second < index_suptype_first:
                    int_entr_Var *= coeficent_speed[index_suptype_first - 1]
                    index_suptype_first -= 1

            if index_suptype_first < index_suptype_second:
                while index_suptype_second > index_suptype_first:
                    int_entr_Var = int_entr_Var / coeficent_speed[index_suptype_second - 1]
                    index_suptype_second -= 1


        if ((index_suptype_first > 4 ) and (index_suptype_second > 4)) :

            if index_suptype_first > index_suptype_second:
                while index_suptype_second < index_suptype_first:
                    int_entr_Var *= coeficent_speed[index_suptype_first - 2]
                    index_suptype_first -= 1

            if index_suptype_first < index_suptype_second:
                while index_suptype_second > index_suptype_first:
                    int_entr_Var = int_entr_Var / coeficent_speed[index_suptype_second - 2]
                    index_suptype_second -= 1

        else:

            if index_suptype_first > index_suptype_second :
                int_entr_Var = int_entr_Var * 3600


            if index_suptype_first < index_suptype_second :
                int_entr_Var = int_entr_Var / 3600



            if ((index_suptype_first < 5) and (index_suptype_second > 4)):

                while (index_suptype_first < (index_suptype_second - 5)):
                    int_entr_Var = int_entr_Var / coeficent_speed[index_suptype_second - 6]
                    index_suptype_second -= 1

                while (index_suptype_first > (index_suptype_second - 5)):
                    int_entr_Var = int_entr_Var * coeficent_speed[index_suptype_first - 1]
                    index_suptype_first -= 1

                                            #compleat


            if ((index_suptype_first > 4) and (index_suptype_second < 5)):


                while (index_suptype_second < (index_suptype_first - 5)):
                    int_entr_Var = int_entr_Var / coeficent_speed[index_suptype_first - 6]
                    index_suptype_first -= 1

                while (index_suptype_second > (index_suptype_first - 5)):
                    int_entr_Var = int_entr_Var * coeficent_speed[index_suptype_second - 1]
                    index_suptype_second -= 1


    int_entr_Var = round(int_entr_Var, 10)

    try:
        otvet.destroy()
    except:
        pass

    otvet = tk.Label(root, text=int_entr_Var, font=("", "14", ""), bg="#6F4F28", width=20, anchor="center")
    otvet.place(x = 155, y =277 )


def Massa():
    global view, coeficent, subtype_first, subtype_second, coeficent_massa


    view = "massa"
    coeficent = ("мг", "г", "кг", "ц", "т")
    coeficent_massa = (1000, 1000, 100, 10)

    subtype_first.destroy()
    subtype_second.destroy()

    subtype_first = ttk.Combobox(root, values=coeficent, font=("", "10", ""), width=8)
    subtype_first.current(0)
    subtype_first.place(x = 400, y = 177)

    subtype_second = ttk.Combobox(root, values=coeficent, font=("", "12", ""), width=5)
    subtype_second.current(1)
    subtype_second.place(x = 400, y = 277)


def Speed():
    global view, coeficent, subtype_first, subtype_second, coeficent_speed
    view = "speed"
    coeficent = ("мм/ч", "см/ч", "дм/ч", "м/ч", "км/ч", "мм/с", "см/с", "дм/с", "м/с", "км/с")
    coeficent_speed = (10, 10, 10, 1000, 10, 10, 10, 1000)

    subtype_first.destroy()
    subtype_second.destroy()

    subtype_first = ttk.Combobox(root, values=coeficent, font=("", "10", ""), width=8)
    subtype_first.current(0)
    subtype_first.place(x=400, y=177)

    subtype_second = ttk.Combobox(root, values=coeficent, font=("", "12", ""), width=5)
    subtype_second.current(1)
    subtype_second.place(x=400, y=277)


def Distance():
    global view, coeficent, subtype_first, subtype_second, coeficent_distance


    view = "distance"
    coeficent = ("мм", "см", "дм", "м", "км")
    coeficent_distance = (10, 10, 10, 1000)


    subtype_first.destroy()
    subtype_second.destroy()

    subtype_first = ttk.Combobox(root, values=coeficent, font=("", "10", ""), width=8)
    subtype_first.current(0)
    subtype_first.place(x=400, y=177)

    subtype_second = ttk.Combobox(root, values=coeficent, font=("", "12", ""), width=5)
    subtype_second.current(1)
    subtype_second.place(x=400, y=277)


def Volume():
    global view, coeficent, subtype_first, subtype_second, coeficent_volume


    view = "volume"

    coeficent = ("мил л", "литр")
    coeficent_volume = (1000, 100)

    subtype_first.destroy()
    subtype_second.destroy()

    subtype_first = ttk.Combobox(root, values=coeficent, font=("", "10", ""), width=8)
    subtype_first.current(0)
    subtype_first.place(x=400, y=177)

    subtype_second = ttk.Combobox(root, values=coeficent, font=("", "12", ""), width=5)
    subtype_second.current(1)
    subtype_second.place(x=400, y=277)


def Department_Wheather():
    global run_button, sity_label, city, root

    open_root()

    close = tk.Button(root, text="<=", font=("", "15", ""), bg="#6F4F28", width="5", command=destroy)
    close.place(x=5, y=5)


    sity_label = tk.Label(root, text = "введите город:", font=("", "17", "bold"), bg = "#6F4F28")
    sity_label.place(x = 150, y = 50)


    city = tk.Entry(root, bg = "#846A20", width=25, font=("", "15", ""))
    city.place(x = 100, y = 100)


    Temperature_button = tk.Button(root, text="узнать", font=("", "15", ""), bg="#6F4F28", command=go, width="7")
    Temperature_button.place(x = 100, y = 150)


def go():
    global run_button, sity_label, city, root, eror_label

    try:
        eror_label.destroy()
    except:
        pass


    city_str = city.get()

    root_weather = tk.Toplevel()
    root_weather.geometry("500x500")
    root_weather.resizable(False, False)
    root_weather.config(bg="#6F4F28")

    citi_label = tk.Label(root_weather, text=f" t {city_str}", font=("", "20", ""), bg="#6F4F28")
    citi_label.place(x=125, y=25)


    params = {"appid": "c8bc3fa8c79c17c7e13fe06ab93e19a4", "units": "metric", "lang": "ru", "q": None}
    params["q"] = city_str

    res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    res = res.json()

    if res["cod"] == "404":
        eror_label = tk.Label(root_weather, text="введте город правильно", font=("", "13", ""), bg="#B07D2B")
        eror_label.place(x = 100, y = 100)

    else:
        temperature = res["main"]
        temp = temperature["temp"]
        feel_temp = temperature["feels_like"]
        humidity = temperature["humidity"]
        pressure = temperature["grnd_level"]
        visibility = res["visibility"]
        weather_list = res["weather"]
        weather_list = weather_list[0]

        temp_label = tk.Label(root_weather, text=f"температура : {temp}", font=("", "13", ""), bg="#B07D2B")
        temp_label.place(x=10, y=100)

        feel_temp_label = tk.Label(root_weather, text=f"ощущается как : {feel_temp}", font=("", "13", ""), bg="#B07D2B")
        feel_temp_label.place(x=10, y=135)

        humidity_label = tk.Label(root_weather, text=f"влажность : {humidity}%", font=("", "13", ""), bg="#B07D2B")
        humidity_label.place(x=10, y=170)

        pressure_label = tk.Label(root_weather, text=f"давление на уровне земли : {pressure}", font=("", "13", ""),bg="#B07D2B")
        pressure_label.place(x=10, y=205)

        visibility_label = tk.Label(root_weather, text=f"видимость {visibility}", font=("", "13", ""), bg="#B07D2B")
        visibility_label.place(x = 10, y = 240)

        if weather_list["main"] =="Clear":
            description = weather_list["description"]
            description_label = tk.Label(root_weather, text=f"небо {description}", font=("", "13", ""), bg="#B07D2B")
            description_label.place(x = 10, y = 275)

        else:
            description = weather_list["description"]
            description_label = tk.Label(root_weather, text=f" {description}", font=("", "13", ""), bg="#B07D2B")
            description_label.place(x = 10, y = 275)


        wind = res["wind"]
        speed_wind = wind["speed"]
        speed_wind_label = tk.Label(root_weather, text=f"скорсть ветра :  {speed_wind} м/с", font=("", "13", ""), bg="#B07D2B")
        speed_wind_label.place(x = 10, y = 310)


def Department_Time():
    global time_label, root


    a = ""

    open_root()

    close = tk.Button(root, text = "<=", font=("", "15", ""), bg = "#6F4F28", command= destroy, width="5")
    close.place(x = 5, y = 5)
    Now_time = time.ctime()
    list_data_ime = Create_time(Now_time)
    month = list_data_ime[1]
    day = list_data_ime[0]
    number = list_data_ime[3]
    now_time =list_data_ime[4]
    years = list_data_ime[5]
    print(list_data_ime)

    label_tooday = tk.Label(root, text = f"сегодня {number} {month} {years}", font=("", "22", "bold"), bg = "#6F4F28")
    label_tooday.place(x = 70, y = 50)

    day_label = tk.Label(root, text = f"{day}", font=("", "25", "bold"), bg = "#6F4F28")
    day_label.place(x = 130, y = 110)


    time_label = tk.Label(root, text=f"{now_time}", font=("", "40", "bold"), bg="#B07D2B", height=3, width=10)
    time_label.place(x = 80, y = 170)


def Create_time(time):
    a = ""
    compleat_time = []

    for i in time:

        if i == " ":

            compleat_time.append(a)
            a = ""

        else:
            a += str(i)
    compleat_time.append(a)

    if compleat_time[0] == "Mon":
        compleat_time[0] = "Понедельник"

    elif compleat_time[0] == "Tue":
        compleat_time[0] = "вторник"

    elif compleat_time[0] == "Wed":
        compleat_time[0] = "среда"

    elif compleat_time[0] == "Thu":
        compleat_time[0] = "четверг"

    elif compleat_time[0] == "Fri":
        compleat_time[0] = "пятница"

    elif compleat_time[0] == "Sat":
        compleat_time[0] = "субота"

    elif compleat_time[0] == "Sun":
        compleat_time[0] = "воскресенье"


    if compleat_time[1] == "Jan":
        compleat_time[1] = "январь"

    elif compleat_time[1] == "Feb":
        compleat_time[1] = "февраль"

    elif compleat_time[1] == "Mar":
        compleat_time[1] = "март"

    elif compleat_time[1] == "Apr":
        compleat_time[1] = "апрель"

    elif compleat_time[1] == "May":
        compleat_time[1] = "май"

    elif compleat_time[1] == "Jun":
        compleat_time[1] = "июнь"

    elif compleat_time[1] == "Jul":
        compleat_time[1] = "июль"

    elif compleat_time[1] == "Jul":
        compleat_time[1] = "август"

    elif compleat_time[1] == "Sep":
        compleat_time[1] = "сентябрь"

    elif compleat_time[1] == "Oct":
        compleat_time[1] = "октябрь"

    elif compleat_time[1] == "Nov":
        compleat_time[1] = "ноябрь"

    elif compleat_time[1] == "Dec":
        compleat_time[1] = "декабрь"


    return compleat_time


def Department_Currency():
    global root
    open_root()
    full_name = ["Австралийский доллар", "Азербайджанский манат", "Фунт стерлингов",
                 "Армянский драм", "Белорусский рубль", "Болгарский лёв", "Бразильский реал",
                 "Венгерский форинт", "Вьетнамский донг", "Гонконгский доллар", "Грузинский лари",
                 "Датская крона", "Дирхам ОАЭ", "Доллар США", "Евро", " Египетский фунт"]

    res = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?")
    res = BeautifulSoup(res.text, features="xml")

    date = res.find("ValCurs")
    date = date.get("Date")

    CharCode = res.find_all("CharCode")

    Value = res.find_all("VunitRate")

    a = 0
    y_place = 50


    close = tk.Button(root, text = "<=", font=("", "15", ""), bg = "#6F4F28", command= destroy, width="5")
    close.place(x = 5, y = 5)

    date_label = tk.Label(root, text = f"данные на {date}", font=("", "20", "bold"), bg = "#6F4F28")
    date_label.place(x = 80, y = 10)


    for i in Value:
        label_CharCode = tk.Label(root, text=f"1 {CharCode[a].text} ({full_name[a]})  ", font=("", "13", ""), bg="#6F4F28", fg="#B07D2B")
        label_CharCode.place(x=20, y=y_place)
        label_Value= tk.Label(root, text=f"=     {i.text} рублей", font=("", "13", ""), bg="#6F4F28", fg="#B07D2B")
        label_Value.place(x=280, y=y_place)
        a +=1
        y_place += 25