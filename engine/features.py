import logging
import webbrowser
from playsound import playsound
import eel
import os
import sqlite3
import pyaudio
import struct
import pvporcupine
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit
import re
import time
import speech_recognition as sr

from engine.help import extract_yt_term

con = sqlite3.connect("Main.db")
cursor = con.cursor()

#playassisatnd sound
@eel.expose
def playAssistantSound():
    music_dir = "web\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()
    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM websites WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                # else:
                #     speak("Opening "+query)
                #     try:
                #         os.system('start '+query)
                #     except:
                #         speak("not found")
                else:
                    speak(f"Opening {query}")
                    try:
                        os.startfile(query)
                    except FileNotFoundError:
                        speak("Application not found")
                    except OSError:
                        speak("Unable to open the application")
                    except Exception as e:
                        speak("An unexpected error occurred")
                        logging.error(f"Unexpected error: {str(e)}")
                
        except:
            speak("some thing went wrong")



def PlayYoutube(query):
        search_term = extract_yt_term(query)
        speak("Playing "+search_term+" on YouTube")
        kit.playonyt(search_term)


def hotword():
    ls='siri'
    ls2="Siri"
    ls3="Amazon"
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('listening....')
            #eel.DisplayMessage('listening....')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print('recognizing')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

            qu=str(query)
            print(qu)
            qu.lower()
            print(type(qu))

            if ls in qu or ls2 in qu or ls3 in qu:
                print("hotword detected")
                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
            else:
                print("hotword not detected")
        except Exception as e:
            print("error")
