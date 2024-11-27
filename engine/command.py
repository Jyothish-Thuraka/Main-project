import pyttsx3
#import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    #eel.DisplayMessage(text)
    engine.say(text)
    #eel.receiverText(text)
    engine.runAndWait()
speak("helooo")