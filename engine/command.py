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

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "message" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance or "phone" in preferance:
 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    
                elif "whatsapp" in preferance:

                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
              
                        whatsApp(contact_no, query, message, name)
                else:
                        speak("please try again")
                
        elif "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                message = 'video call'                  
                whatsApp(contact_no, query, message, name)
            else:
                        speak("please try again")
        elif "call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance or "phone" in preferance:
                    speak("calling to "+name)
                    makeCall(name, contact_no)

                elif "whatsapp" in preferance:
                    message = 'call'
                    whatsApp(contact_no, query, message, name)
                else:
                    speak("please try again")


        # elif "send message" in query or "message" in query or  "call" in query or "video call" in query:
        #     from engine.features import findContact, whatsApp, makeCall, sendMessage
        #     contact_no, name = findContact(query)
        #     if(contact_no != 0):
        #         speak("Which mode you want to use whatsapp or mobile")
        #         preferance = takecommand()
        #         print(preferance)

        #         if "mobile" in preferance or "phone" in preferance:
        #             speak("which mode you want to use call or message")
        #             if "send message" in query or "send sms" in query: 
        #                 speak("what message to send")
        #                 message = takecommand()
        #                 sendMessage(message, contact_no, name)
        #             elif "phone call" in query or "call" in query:
        #                 speak("calling to "+name)
        #                 makeCall(name, contact_no)
        #             else:

        #                 speak("please try again")
        #         elif "whatsapp" in preferance:
        #             message = ""
        #             if "send message" in query:
        #                 message = 'message'
        #                 speak("what message to send")
        #                 query = takecommand()
                                        
        #             elif "phone call" in query:
        #                 message = 'call'
        #             else:
        #                 message = 'video call'
                                        
        #             whatsApp(contact_no, query, message, name)

        elif "send email" in query or "email" in query:
            from engine.features import sendEmail
            
            re_email = takecommand()
            message=takecommand()
            sendEmail(re_email, message)
            speak("email sent successfully")

        else:
            from engine.features import web_search_assistant
            print("i run")
            web_search_assistant(query)
            
            
    except:
        print("error1")
        speak("some thing went wrong")
        
    eel.ShowHood()
