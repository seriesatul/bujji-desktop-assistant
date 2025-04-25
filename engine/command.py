import pyttsx3
import eel
import time

def speak(text):
    eel.startMouthAnimation()  # JS trigger
    time.sleep(-1)  # tiny delay to sync
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 174)  # Speed of speech
    eel.DisplayMessage(text)  # Display message in the UI
    engine.say(text)
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
    query = takeCommand()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)

    elif "on youtube":
        from engine.features import openYoutube
        openYoutube(query)
     


    if 'hello' in query:
        speak("Hello! How can I assist you today?")
    elif 'how are you' in query:
        speak("I am fine, thank you! How can I help you?")
    elif 'what is your name' in query:
        speak("I am your virtual assistant.")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a great day!")
        exit()

    eel.showHeading()

   

