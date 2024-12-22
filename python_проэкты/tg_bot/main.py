import json
from os import replace
import telebot
import time
import requests
from bs4 import BeautifulSoup
import lxml


marks_id = []
refactor_marks_id = []
sred_id = []
del_item_id = []
do = True


bot = telebot.TeleBot("7914466260:AAEP7lpVimlCbTL3tuRtTs7p8Wnj9DBSStQ")

file = open("./sred_marks.txt", "a")
file.close()

try:
    send_marks = ""
    file = open("./sred_marks.txt", "r")

    for i in file:

        txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))  # json из файла
        id = txt_dictionary["id"]
        for items in (txt_dictionary["item_marks"]):
            for item in items:
                send_marks += f"{item} - {items[item]} \n"
        bot.send_message(id, f" доброе утро! \n{send_marks}")

except:
    pass


@bot.message_handler(commands=["start"])
def Help(message):
    bot.send_message(message.chat.id,
                     "этот бот поможет вам следить за оценками, расчитывать средний бал, и напомнит про ваш бал")


@bot.message_handler(commands=["help"])
def Help(message):
    bot.send_message(message.chat.id, """
    /help - базавые команды \n
    /marks - можно высчитать средний бал он сохранится и будет напоминать о сибе каждый день \n
    /my_marks - выводит сохранённые балы с предметами \n
    /refactor_marks - позволяет поменять название предмета\n
    /sred - поможет высчитать среднее значение \n
    /del_marks - позволяет удалить предмет\n""")


@bot.message_handler(commands=["marks"])
def Marks(message):
    global marks_id
    marks_id_est = False
    id = -1

    for i in marks_id:
        id +=1
        print(i)

        if str(i) == str(message.chat.id):
            marks_id[id] = message.id
            marks_id_est = True

    if marks_id_est == False:
        marks_id.append({message.chat.id: message.id})

    bot.send_message(message.chat.id, "отправьте название предмета, запятую и оценки по нему через пробел например (русский,5 5 5 5 5)")


@bot.message_handler(commands=["my_marks"])
def My_marks(message):
    file = open("./sred_marks.txt", "r")
    my_marks_txt = ""
    for i in file:

        txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))

        if txt_dictionary["id"] == str(message.chat.id):

            for items in (txt_dictionary["item_marks"]):
                for item in items:
                    my_marks_txt += f"{item} - {items[item]} \n"
            bot.send_message(message.chat.id, my_marks_txt)


@bot.message_handler(commands=["refactor_marks"])
def Refactor_marks(message):
    global refactor_marks_id

    refactor_marks_id_est = False
    id = -1

    for i in refactor_marks_id:
        id += 1

        if str(i) == str(message.chat.id):
            refactor_marks_id[id] = message.id
            refactor_marks_id_est = True

    if refactor_marks_id_est == False:
        refactor_marks_id.append({message.chat.id: message.id})

    bot.send_message(message.chat.id, "отправьте название предмета которое хотите изменить,  запятую и название предмета на которое хатите заменить")


@bot.message_handler(commands=["sred"])
def Sred(message):
    global sred_id

    sred_id_est = False
    id = -1

    for i in sred_id:
        id += 1
        print(i)

        if str(i) == str(message.chat.id):
            sred_id[id] = message.id
            sred_id_est = True

    if sred_id_est == False:
        sred_id.append({message.chat.id: message.id})


    bot.send_message(message.chat.id, "отправьте цифры через пробел чтоб узнать их среднее значение")


@bot.message_handler(commands=["del_marks"])
def Sred(message):
    global del_item_id

    del_item_id_est = False
    id = -1

    for i in del_item_id:
        id += 1
        print(i)

        if str(i) == str(message.chat.id):
            del_item_id[id] = message.id
            del_item_id_est = True

    if del_item_id_est == False:
        del_item_id.append({message.chat.id: message.id})

    bot.send_message(message.chat.id, "название придмета который хотите удалить")


@bot.message_handler(commands = ["now_curs"])
def Curs_message(message):
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
    label = f"КУРС ВАЛЮТ НА {date}:\n \n"
    for i in Value:
        label += f" 1 {CharCode[a].text}   ({full_name[a]}) = {i.text} рублей  \n"
        a +=1

    bot.send_message(message.chat.id, label)


@bot.message_handler()
def Command_none(message):
    global marks_id, refactor_marks_id, now_time, sred_id
    file_dictionary_list = []
    key_est = False

    # marks

    try:

        for keys in marks_id:

            for key in keys:
                print(key)
                print(keys)

                if ((str(key) == str(message.chat.id)) and (str(message.id - 2) == str(keys[key]))):  # проверка надо ли обрабатывать сообщение

                    text = message.text  # отправленный текст
                    item = ""  # предмет
                    compleat_item = False  # переменная для расграничевания названия и оценок
                    a = 0
                    sum_marks = 0  # сред оценка

                    for i in text:  # перебор для нахождения предмета и оценки

                        if ((i != " ") and (i != ",") and (compleat_item == False)):

                            item += i  # определение предмета

                        elif ((i == ",") or (compleat_item == True)):

                            compleat_item = True

                            if ((i != " ") and (i != ",")):  # определение оценки

                                a += 1
                                try:

                                    i = int(i)
                                    sum_marks += i
                                except:

                                    sum_marks - 1
                                    a -= 1

                    sred_marks = round(sum_marks / a, 1)  # средняя оценка
                    bot.send_message(message.chat.id, f"{item} = {sred_marks}")  # отправка средней оценки

                    item = str(item)
                    sred_marks = str(sred_marks)

                    sred_marks_txt = {"id": str(message.from_user.id), "item_marks": [{item: sred_marks}]}  # json строка

                    file = open("./sred_marks.txt", "r")

                    index_item = -1
                    item_est = False
                    txt_dictionary = None
                    file_dictionary_list = []
                    key_index = -1
                    id_est = False

                    for i in file:

                        txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))  # json из файла

                        if int(txt_dictionary["id"]) == int(sred_marks_txt["id"]):
                            id_est = True
                            for keys in (txt_dictionary["item_marks"]):
                                for key in keys:
                                    key_index += 1
                                    if str(key) == str(item):
                                        (((txt_dictionary["item_marks"])[key_index])[item]) = sred_marks
                                        item_est = True

                            if item_est == False:
                                (txt_dictionary["item_marks"]).append({item: sred_marks})

                        file_dictionary_list.append(str(txt_dictionary))

                    if id_est == False:
                        file_dictionary_list.append(str(sred_marks_txt))

                        # запись в файл
                    file = open("./sred_marks.txt", "w")

                    if file_dictionary_list != []:

                        file.close()
                        file = open("./sred_marks.txt", "a")

                        for i in file_dictionary_list:
                            file.write(str(i) + "\n")

                    else:
                        file.write(str(sred_marks_txt) + "\n")

                    file.close()

    except:
        bot.send_message(message.chat.id, "введите правильные значения")



    # Refactor_marks

    try:

        for keys in refactor_marks_id:

            for key in keys:

                if (str(key) == str(message.chat.id)) and (str(message.id - 2) == str(keys[key])):

                    old_item = ""  # предмет который надо поменять
                    compleat_item = False  # переменная для расграничевания названия и оценок
                    new_item = ""  # предмет на который надо поменять
                    key_index = -1
                    for i in message.text:

                        if ((i != " ") and (i != ",") and (compleat_item == False)):

                            old_item += i  # определение предмета

                        elif ((i == ",") or (compleat_item == True)):

                            compleat_item = True

                            if ((i != " ") and (i != ",")):  # определение оценки
                                new_item += str(i)

                    if old_item != new_item:
                        file = open("./sred_marks.txt", "r")

                        item_marks = []

                        for i in file:
                            txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))  # json из файла

                            if int(txt_dictionary["id"]) == int(message.chat.id):

                                for keys in txt_dictionary["item_marks"]:

                                    for key in keys:
                                        key_index += 1

                                        if ((key == old_item) and (key != "") and (new_item != "")):
                                            new_key = new_item
                                            item_marks.append({new_key: keys[key]})
                                            bot.send_message(message.chat.id, f"новое значение {new_key} {keys[key]}")
                                            key_est = True

                                        else:
                                            item_marks.append({key: keys[key]})
                            else:
                                file_dictionary_list.append(str(txt_dictionary))

                        txt_dictionary["item_marks"] = item_marks

                        if key_est == True:

                            file = open("./sred_marks.txt", "w")

                            if file_dictionary_list != []:
                                file.close()
                                file = open("./sred_marks.txt", "a")

                                for i in file_dictionary_list:
                                    file.write(str(i) + "\n")

                            else:
                                file.write(str(txt_dictionary) + "\n")

                            file.close()

                        else:
                            if ((key != "") and (new_item != "")):
                                bot.send_message(message.chat.id, "такой предмет не найден")

                            else:
                                bot.send_message(message.chat.id, "введите новое значение")

                    else:
                        bot.send_message(message.chat.id, "новое название совпадает со старым")

    except:
        bot.send_message(message.chat.id, "введите правильные значения")

    #sred

    try:
        for keys in sred_id:

            for key in keys:

                if (str(key) == str(message.chat.id)) and (str(message.id - 2) == str(keys[key])):
                    sum_num = 0
                    id_num = 0
                    num = ""

                    for i in (message.text + " "):
                        if i != " ":
                            num += i
                        else:
                            sum_num += int(num)
                            id_num += 1
                            num = ""
                    bot.send_message(message.chat.id, f"{sum_num / id_num}")

    except:
        pass

    #del_marks

    try:
        for keys in del_item_id:

            for key in keys:

                if (str(key) == str(message.chat.id)) and (str(message.id - 2) == str(keys[key])):

                    item = message.text
                    file = open("./sred_marks.txt", "r")
                    item_marks = []
                    item_est = False

                    for i in file:
                        txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))  # json из файла

                        for keys in txt_dictionary["item_marks"]:

                            for key in keys:

                                if key == item:
                                    item_est = True

                                else:
                                    item_marks.append({key: keys[key]})

                        txt_dictionary["item_marks"] = item_marks
                        file_dictionary_list.append(str(txt_dictionary))

                    if item_est == False:
                        bot.send_message(message.chat.id, "предмет не найден")

                    elif item_est == True:
                        file = open("./sred_marks.txt", "w")

                        if file_dictionary_list != []:
                            file.close()
                            file = open("./sred_marks.txt", "a")

                            for i in file_dictionary_list:
                                file.write(str(i) + "\n")

                        else:
                            file.write(str(txt_dictionary) + "\n")

                        file.close()

                        bot.send_message(message.chat.id, f"{item} успешно удалён")

    except:
        pass


def Curs():
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
    label = f"КУРС ВАЛЮТ НА {date}:\n\n"
    for i in Value:
        label += f" 1 {CharCode[a].text}   ({full_name[a]}) = {i.text} рублей  \n"
        a +=1

    file = open("./sred_marks.txt", "r")

    for i in file:

        txt_dictionary = json.loads((i.replace("'", '"').replace("\n", "")))

        bot.send_message(txt_dictionary["id"], label)

    file.close()

try:

    Curs()

except:
    pass

bot.polling(none_stop = True)