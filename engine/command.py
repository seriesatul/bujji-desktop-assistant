import pyttsx3
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 174)  # Speed of speech
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
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
        speak(query)
        eel.showHeading()
    except Exception as e:
        print(e)
        print("Sorry, I did not get that. Please repeat.")
        eel.DisplayMessage("Sorry, I did not get that. Please repeat.")
        return "None"
    return query.lower() 

   

