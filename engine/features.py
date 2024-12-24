import logging
import webbrowser
from playsound import playsound
import eel
import os
import sqlite3
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit
import re

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

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
