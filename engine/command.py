import pyttsx3
import eel
import time

def speak(text):
    text = str(text)
    eel.startMouthAnimation()  # JS trigger
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 180)  # Speed of speech
    eel.DisplayMessage(text)  # Display message in the UI
    engine.say(text)
    eel.receiverText(text)  # JS trigger to show text in the UI
    engine.runAndWait()
    eel.stopMouthAnimation()  # JS trigger
    estimated_duration = len(text.split()) / 2.5  # avg 2.5 words per second
    time.sleep(estimated_duration)  # let animation play through



def takeCommand():
    eel.nodHead()
    # This function will take command from the user and return it as a string
    # You can use speech recognition or any other method to take input
    # For now, we will just return a static string for testing purposes
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,5,10)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(f"{query}\n")
        time.sleep(1)
        
    except Exception as e:
        print(e)
        print("Sorry, I did not get that. Please repeat.")
        eel.DisplayMessage("Sorry, I did not get that. Please repeat.")
        return "None"
    return query.lower() 

@eel.expose
def allCommand():

    try:
       
        query = takeCommand()
        print(query)
        eel.senderText(query)

        eel.DisplayMessage(query)  # Display message in the UI
        
        

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import openYoutube
            openYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact,whatsapp
            flag =""
            contact_no,name = findContact(query)
            if contact_no != 0:

                if "send message" in  query:
                    flag = "message"
                    speak("Tell me the message you want to send to"+" "+name)
                    query = takeCommand()

                elif "phone call" in query:
                    flag = "call"
                    speak("Calling to"+" "+name)   

                else:
                    flag = "video call"
                    speak("Starting video call with"+" "+name)  

                whatsapp(contact_no,query,flag,name)      

        else:
                from engine.features import chatBot
                chatBot(query)
                # takeCommand()
                eel.showHeading()

                return

        

        eel.showHeading()

    except Exception as error:    
        
        print(error)
        eel.DisplayMessage("Error in command execution")
        return "None" 

   

