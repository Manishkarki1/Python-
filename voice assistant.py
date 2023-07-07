import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
# import time

def sptext():
    while True:
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening!Please speak..")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("recognizing....")
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not Understand")

def speechtotext(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",130)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__" :

    if "hey stranger" in sptext().lower():
        speechtotext("yes please ask me whatever you want")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                speechtotext("my name is manoj")
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtotext(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                jokes = pyjokes.get_joke(language="en", category="neutral")
            elif "play song" in data1:
                addaddress = ""
                listsong = os.listdir(addaddress)
                print(listsong)
                os.startfile(os.path.join(addaddress, listsong[0]))
            elif "wish me" in data1:
                speechtotext("First tell me your name")
            elif "my name is" in data1:
                speechtotext(f"happy birthday to you {data1[11:20]}")
            elif "exit" in data1:
                speechtotext("thank you see you soon")


            # time.sleep(3)
    else:
        print("can't understand")

