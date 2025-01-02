import logging
import pywhatkit as pwk
from shlex import quote
import subprocess
import webbrowser
from hugchat import hugchat
from playsound import playsound
import eel
import os
import sqlite3
import pyaudio
import pyautogui as autogui
import struct
import pvporcupine
import pyautogui
import pywhatkit as kit
import re
import smtplib
import time
import speech_recognition as sr
from langchain_community.llms import CTransformers 
from engine.config import ASSISTANT_NAME
from engine.config import password
from engine.command import speak
from engine.help import extract_yt_term, remove_words

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
                        query = query.replace("open", "")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")


                
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
    ls4="open"
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('hotword........')
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

            if ls in qu or ls2 in qu or ls3 in qu or ls4 in qu:
                from engine.command import speak
                print("hotword detected")
                # pressing shorcut key win+j

                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
            else:
                print("hotword not detected")
        except Exception as e:
            print("error")


#find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        ai_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        ai_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        ai_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(ai_message)

def sendEmail(re_mail,message):
    pwk.send_mail("jyothishalways@gmail.com", password,"",message,re_mail,)

    

# #chatbot raa lucha
# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response


from langchain_community.llms import CTransformers
#import CTransformers
def web_search_assistant(query):
    # Initialize the LLM
    llm = CTransformers(
        model='model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.5  # Slightly increased temperature for more creative responses
        }
    )
    
    # Create a template for web search assistance
    prompt_template = f"""You are a helpful web search assistant. Please help with the following quaery in 30-50 words. query:
    
Query: {query} 

"""

    # Get the response from the model
    response = llm.predict(prompt_template)
    print(response)
    speak(response)

    return response



# phone
def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

def sendMessage(message, mobileNo, name):
    from engine.help import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(960, 1225)
    speak("message send successfully to "+name)