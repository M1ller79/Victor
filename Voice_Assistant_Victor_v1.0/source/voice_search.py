import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')

print(voices[3].name) # Alexander
