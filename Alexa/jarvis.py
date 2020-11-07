import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evaning sir")

    speak("i am alexa. please tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
   
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shewalepradhunya786@gmail.com','***your password***')
    server.sendmail('shewalepradhunya786@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'alexa can you' in query :
            print("yes sir, I can")
            speak("yes sir, I can")
        
        elif 'hi alexa' in query :
            print("yes sir, I can")
            speak("hi pradhunya, how can i help you")

        elif 'open youtube' in query :
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            webbrowser.open("google.com")

        elif 'current weather' in query :
            webbrowser.open("https://www.theweathernetwork.com/in/weather/maharashtra/malegaon")
        
        elif 'world covid cases' in query :
            webbrowser.open("https://www.worldometers.info/coronavirus/")

        elif 'india covid cases' in query :
            webbrowser.open("https://www.worldometers.info/coronavirus/country/india/")

        elif 'maharastra covid cases' in query :
            webbrowser.open("https://www.statista.com/statistics/1106919/india-maharashtra-covid-19-cases-by-type/")

        elif 'california covid cases' in query :
            webbrowser.open("https://www.worldometers.info/coronavirus/usa/california/")

        elif 'world top 10' in query :
            webbrowser.open("https://www.theweek.co.uk/people/57553/top-billionaires-who-richest-person-world")

        elif 'open stackoverflow' in query :
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query :
            music_dir = 'F:\\gr'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query :
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shubham' in query :
            try :
                speak("what should i say")
                content = takeCommand()
                to = "pdshewale777@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e :
                print(e)
                speak("sorry my friend pradhunya. i am not able to send thise email at that moment")      
  