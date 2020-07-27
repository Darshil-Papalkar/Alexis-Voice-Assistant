import pyttsx3
import  datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from app_opening import mail, check_email

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Jarvis sir. How may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold =  1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN').lower()
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return "None"
    return query
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open('C:\\Users\\DARSHIL\\OneDrive_1\\OneDrive\\Desktop\\python-Voice Recognizer\\JARVIS\\pwd.txt','r')
    server.login('papalkardarshil12@gmail.com',file.readline())
    server.sendmail('papalkardarshil12@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            # print(query)
            results = wikipedia.summary(query, sentences = 2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            url = "https://www.youtube.com/"
            webbrowser.get().open_new_tab(url)
        
        elif 'open google' in query:
            url = "https://www.google.co.in/"
            webbrowser.get().open_new_tab(url)
        
        elif 'play video songs' in query:
            music_dir = 'D:\\Video Songs'
            songs = os.listdir(music_dir)
            # print(songs)
            file = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[file]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = 'D:\\MI\\VSCode-win32-x64-1.47.2\\Code.exe'
            os.startfile(codePath)
        
        elif 'email' in query:
            speak('To whom should i send mail...')
            c = takeCommand()
            C = check_email(c.lower())
            while C!='True':
                speak('Sorry, The Receiver is not in the list')
                c = takeCommand()
                C = check_email(c.lower())
            c = mail(c) 

            try:
                speak('What should i say?')
                content = takeCommand().capitalize()+'.'
                to = c
                sendEmail(to, content)
                speak('Email Has been sent')

            except Exception as e:
                print(e)
                speak('Sorry Unable to send email at this moment')
