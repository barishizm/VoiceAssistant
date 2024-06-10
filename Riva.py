import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female voice, 0 for male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except Exception as e:
        print("Error: ", e)
        speak("I didn't understand. Please say that again.")
        return "None"
    return query

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", '')
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results for your query.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")
        print("Wikipedia error: ", e)

def open_website(url):
    speak(f"Opening {url}")
    webbrowser.open(url)

def open_local_disk(disk_letter):
    path = f"{disk_letter}:\\"
    if os.path.exists(path):
        speak(f"Opening local disk {disk_letter}")
        os.startfile(path)
    else:
        speak(f"Local disk {disk_letter} not found.")

def execute_command(query):
    if 'wikipedia' in query:
        search_wikipedia(query)
    elif 'are you' in query:
        speak("I am Riva, developed by PaiX.")
    elif 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'open github' in query:
        open_website("https://www.github.com")
    elif 'open stackoverflow' in query:
        open_website("https://www.stackoverflow.com")
    elif 'open spotify' in query:
        open_website("https://www.spotify.com")
    elif 'open whatsapp' in query:
        loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        if os.path.exists(loc):
            speak("Opening WhatsApp")
            os.startfile(loc)
        else:
            speak("WhatsApp application not found.")
    elif 'play music' in query:
        open_website("https://www.spotify.com")
    elif 'open local disk' in query:
        disk_letter = query.split()[-1].upper()
        open_local_disk(disk_letter)
    elif 'sleep' in query:
        speak("Goodbye!")
        exit(0)
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == '__main__':
    speak("Riva assistance activated")
    speak("How can I help you?")
    while True:
        query = take_command().lower()
        if query != "None":
            execute_command(query)
