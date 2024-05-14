import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import os;
import subprocess
# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold=0.5;
        recognizer.non_speaking_duration=0.5;
        print("Listening...");
        recognizer.adjust_for_ambient_noise(source);  # Adjust for noise
        audio = recognizer.listen(source, timeout=5);  # Listen for 5 seconds
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-US");
        print(f"User said: {query}");
        return query;
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return "UnknownValueError"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return "RequestError"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error"


if __name__ == "__main__":
    speak("hello sir I am jarvis AI");
    while True:

        query = takeCommand().lower()
        if query == "exit":
            speak("Exiting. Goodbye!")
            break
        elif "open" in query:
            websites = {
                "youtube": "https://www.youtube.com",
                "wikipedia": "https://www.wikipedia.com",
                "google": "https://www.google.com",
                "facebook": "https://www.facebook.com"
            }
            for site, url in websites.items():
                if site in query:
                    speak(f"Opening {site}")
                    webbrowser.open(url)
                    break
        speak(query);
        if 'the time' in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strfTime}");
            print(strfTime);
        # todo: add more app paths  to open
        if 'open netflix'.lower() in query.lower():
            # os.system(f"open C:\Program Files\Google\Chrome\Application\chrome_proxy.exe");
            try:
                application_path = ("T:\\unity\\Unity Hub.exe");
                subprocess.Popen(application_path);
                print("Application opened successfully!")
            except Exception as e:
                print(f"Error: {e}");





