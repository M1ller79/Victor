# Голосовой Ассистент Виктор (1.0) / Voice Assistant Victor (1.0)
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz # Библиотека для нечёткого сравнения команд
import pyttsx3
import datetime

options = {
    "alias" : ('Виктор', 'Привет', 'Привет, Виктор', 'Витя', 'Ви', 'Вить', 'виктор', 'витя', 'вить', 'ви'),
    "tbr" : ('скажи', 'сколько', 'расскажи', 'покажи', 'произнеси', 'который'),
    "cmds" : {
        "ctime": ('время', 'сейчас времени', 'настоящее время', 'который час', 'текущее время', 'сейчас час'),
        "joke": ('расскажи прикол', 'расскажи шутку', 'пошути', 'расскажи какой-нибудь прикол', 'расскажи какую-нибудь шутку', 'рассмеши меня', 'расскажи анекдот')
    }
}

#-------------------------------------------
# Функции / Functions

def speak(what): # Голосовой вывод / Voice output
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio): # Запись произнесённой фразы / Voice recording
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознанно: " + voice)

        if voice.startswith(options["alias"]):
            # Обратимся к Виктору / Ask Victor
            cmd = voice

            for x in options['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in options['tbr']:
                cmd = cmd.replace(x, "").strip()

            # Распознаём и выполняем команду / Recognition and execution
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан.")
    except sr.RequestError:
        print("[log] Неизвестная ошибка, проверьте подключение к сети.")
         
def recognize_cmd(cmd): # Нечёткий поиск команд, которые получил Виктор / Fuzzy command search 
    RC = {'cmd': '', 'percent': 0}
    for c, v in options['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

def execute_cmd(cmd): # Определение и преобразование команды в действие / Recognition and execution
    if cmd == 'ctime': # Текущее время / Current time
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'joke': # Рассказать анекдот / Make a joke
        speak('Я пока не умею шутить... Слишком серьёзный.')
    
    else:
        print('Команда не распознана. Повторите пожалуйста.')

#-------------------------------------------
# Запуск / Launch
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()



# Если вы установили новый голос / If you have already downloaded a new voice

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[3].id)

speak("Здравствуйте, я Виктор - Ваш голосовой ассистент. Можете звать меня Ви.")
speak('Я Вас слушаю.')
#-------------------------------------------

stop_listening = r.listen_in_background(m, callback)

while True:
        time.sleep(0.1) # Бесконечный цикл / Infinite loop
