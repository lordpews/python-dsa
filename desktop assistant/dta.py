import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')


engine.setProperty('voice', 'english')


rate = engine.getProperty('rate')
engine.setProperty('rate',150)
volume = engine.setProperty('volume',0.7)

def speak(audio):

    ''' text to speech function'''
    engine.say(audio)
    engine.runAndWait()

def wishme():

    '''wishes the user according to the system time'''

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good morning Master!")

    if hour >=12 and hour < 18:
        speak("Good afternoon Master!")
    
    else:
        speak("Good evening Master!")

    speak("I am your servent, I mean Assistant. How may i help you?")


def takecommand():
    ''' takes audio input from user and return text/string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print(e)

        print("Can you please repeat ?")

        return "None"
    return query


if __name__ == '__main__':
    # wishme()
    while True:
        query = takecommand().lower()

    # logic for doing stuff based on query
        if "wikipedia" in query:
            speak("searching wikipedia..........")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)