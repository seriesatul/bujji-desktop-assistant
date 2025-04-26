import subprocess
import hugchat
from hugchat.hugchat import ChatBot

from playsound import playsound
import pyautogui
from engine.config import ASSISTANT_NAME
from engine.command import speak
import os
import eel
import webbrowser
import sqlite3
import pywhatkit as kit
import re
import pvporcupine
import pyaudio
import time
import struct
from urllib.parse import quote as qoute

from engine.helper import extract_yt_term, remove_words

connection = sqlite3.connect('bujji.db')
cursor = connection.cursor()

#playing Assistant Initialisation sound

def playAssistantInitSound():
    music_dir= "frontend\\assets\\audio\\videoplayback_DvjNbfMZ.mp3"
    playsound(music_dir)


def openCommand(query):
    # This function will open a command prompt or terminal window
    query =query.replace(ASSISTANT_NAME, "")
    query =query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute('SELECT path FROM sys_commands WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak(f"Opening {query}")
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute('SELECT path FROM web_commands WHERE name IN (?)', (app_name,)) 
                results=cursor.fetchall()   

                if len(results) != 0:
                    speak(f"Opening {query}")
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening"+ query)    
                    try:
                        os.system('start'+ query)
                    except:
                        speak("Website not found")

        except:
            speak("Something went wrong")                    



def openYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Opening YouTube for {search_term}")
        kit.playonyt(search_term)
       
    else:
        speak("Please specify what you want to search.")
        print("Please specify what you want to search on YouTube.")        


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        porcupine =porcupine.create(keywords=["bujji","alexa","jarvis"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("Hotword Detected")
                

                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.keyDown("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if paud is not None:
            paud.terminate()                    

def findContact(query):
    words_to_remove = [ASSISTANT_NAME,"make","a","phone","call","to","tu","send","message","whatsapp","video","find", "contact", "search", "number", "mobile"]
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? or LOWER(name) LIKE ?", ('%' + query + '%',query + '%'))
        results = cursor.fetchall()
        print(results[0][0])

        mobile_number_str = str(results[0][0])
        if mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str

        return mobile_number_str, query

    except Exception as e:
        speak(query +" not exists in your contacts")   
        return 0, 0 
    

def whatsapp(mobile_no,message,flag,name):

    # This function will open whatsapp with the given mobile number and message
    try:
        if flag == "message":
            target_tab = 12
            bujji_message = "Message Sended Successfully to "+ name

        elif flag == "call":
            target_tab = 7
            message = ''
            bujji_message = "Calling to"+ name

        else:
            target_tab = 6
            message = ''
            bujji_message = " Started Video calling with"+ name   

        #Encode the message to URL format
        encoded_message = qoute(message)

        #construct the full command
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

        full_command = f'start "" "{whatsapp_url}"'

        #open whatsapp with constructed URL with cmd
        subprocess.run(full_command, shell=True)
        time.sleep(5)
        subprocess.run(full_command, shell=True)

        pyautogui.hotkey('ctrl', 'f')

        for i in range(1,target_tab):
            pyautogui.hotkey('tab')

        pyautogui.hotkey('enter')
        speak(bujji_message) 

    except Exception as e:
        print(e)   

def chatBot(query):
    user_input = query.lower()
    chatbot = ChatBot(cookie_path="engine\\cookies.json")  # Use the imported ChatBot class
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

        






