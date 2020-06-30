from gtts import gTTS
from playsound import playsound
import os
import pyttsx3


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


#process1

#def speak(text):
#    tts = gTTS(text=text, lang="en")
#    filename = "voice.mp3"
#    tts.save(filename)  # saves the audio file
#    playsound(filename)
#    os.remove(filename)


#process2

def speak(text):
    engine.say(text)
    engine.runAndWait()