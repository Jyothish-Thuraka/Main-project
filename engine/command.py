import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,6,10)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ""
    
    return query.lower()

# re=takecommand()
# speak(re)
@eel.expose
def allCommands(message=1):
    if message==1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
            print("i run")
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "message" in query or  "call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message=""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                    if "video call" in query:
                        message = 'video call'
               
                    elif "call" in query:
                        message = 'call'
                    else:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                        
                                        
                    whatsApp(contact_no, query, message, name)


        else:
            from engine.features import web_search_assistant
            print("i run")
            web_search_assistant(query)
            
            
    except:
        print("error1")
        speak("some thing went wrong")
        
    eel.ShowHood()
