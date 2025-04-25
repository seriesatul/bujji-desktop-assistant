from playsound import playsound
from engine.config import ASSISTANT_NAME
from engine.command import speak
import os
import eel
import webbrowser
import sqlite3
import pywhatkit as kit
import re

connection = sqlite3.connect('bujji.db')
cursor = connection.cursor()

#playing Assistant Initialisation sound

def playAssistantInitSound():
    music_dir= "frontend\\assets\\audio\\videoplayback_CnNGD6UD.mp3"
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
        speak("Please specify what you want to search on YouTube.")
        print("Please specify what you want to search on YouTube.")        

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        return match.group(1)
    return None
    
