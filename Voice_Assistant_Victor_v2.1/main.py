# Voice Assistant Victor Version 2.1

import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
import webbrowser
import random
from num2t4ru import num2text

# Сообщение о старте программы (Инициализация)
print(f"{config.VA_NAME} ({config.VA_VER}) приветствует Вас!")
tts.va_speak("Здравствуйте. Это Виктор. Ваш голосовой ассистент версии два точка один. Я вас слушаю.   ")



def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak('Я Вас не расслышал. Повторите пожалуйста')
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, '').strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, '').strip()
    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейчас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код',
                 'Из комбинации лени и логики получаются программисты',
                 'Чем отличается программист от политика? Программисту платят деньги только за работающие программы.']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("yandex.ru")

    elif cmd == 'music':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("music.yandex.ru")
        tts.va_speak('Уже готово')

    elif cmd == 'weather':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("yandex.ru/pogoda")

    elif cmd == 'thanks':
        tts.va_speak('Всегда рад помочь')

    elif cmd == 'author':
        tts.va_speak('Меня создал человек с ником Миллер семьдесят девять')


# Прослушивание команд
stt.va_listen(va_respond)
