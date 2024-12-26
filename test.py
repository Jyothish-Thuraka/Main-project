import pvporcupine
import pyaudio
import struct
import time
import pyautogui
import speech_recognition as sr

# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None
#     try:
#         # pre trained keywords    
#         porcupine = pvporcupine.create(keywords=["jarvis", "alexa"]) 
#         paud = pyaudio.PyAudio()
#         audio_stream = paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#         )
#         print("Listening for hotwords 'jarvis' or 'alexa'...")
        
#         while True:
#             keyword = audio_stream.read(porcupine.frame_length)
#             keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
#             keyword_index = porcupine.process(keyword)there is
#             if keyword_index >= 0:
#                 print(f"Hotword detected! Index: {keyword_index}")
#                 # pressing shortcut key win+j
#                 pyautogui.keyDown("win")
#                 pyautogui.press("j")
#                 time.sleep(2)
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()

def hotword():
    ls='siri'
    ls2="Siri"
    r = sr.Recognizer()
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

        if ls in qu or ls2 in qu:
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
hotword()
 