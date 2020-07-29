import pyttsx3
import  datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from mail_list import mail, check_email
from difflib import get_close_matches
import json
import requests
from num import check

data = json.load(open('data.json'))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak_slow(audio):
    engine.setProperty('rate', 170)
    speak(audio)

def translate(word):
    word = word.lower()
    if word in data:
        speak('%s means'%word)
        speak(data[word])
        print(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        print(('Did you mean ' + x +
              ' instead,  respond with Yes or No.'))
        speak_slow('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand().lower()
        if 'yes' in ans:
            speak(data[x])
        elif 'no' in ans:
            print("Word doesn't exist. Please make sure you spelled it correctly.\n")
            speak("Word doesn't exist. Please make sure you spelled it correctly.")

        else:
            print("We didn't understand your entry.\n")
            speak("We didn't understand your entry.")

    else:
        print("Word doesn't exist. Please double check it.")
        speak("Word doesn't exist. Please double check it.")

def speak_news():
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=<API KEY>') # enter api key
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        print(int(index)+1, end=' ')
        print(articles['title']+'\n')
        speak_slow(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

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
        query = r.recognize_google(audio, language='en-US').lower()
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print('Say that again please...\n')
        return "None"
    return query

def cross_check(word):
    if word.isdigit():
        return(word)
    else:
        # if digit is not recognised spell number in words like --" o n e "
        word = word.lower()
        if len(get_close_matches(word, data.keys())) > 0:
            for a in range(len(get_close_matches(word, data.keys()))):
                x = get_close_matches(word, data.keys())[a]
                print(('Did you mean ' + x +
                    ' instead,  respond with Yes or No.\n'))
                speak_slow('Did you mean ' + x +
                    ' instead,  respond with Yes or No.')
                ans = takeCommand().lower()
                if 'no' in ans:
                    return 'None'
                else:
                    return(check(x))

        else:
            print("Word doesn't exist. Please double check it.\n")
            speak("Word doesn't exist. Please double check it.")
            return 'None'

        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # enter file_path of password stored in text file
    file = open('file_path\\pwd.txt','r')
    server.login('sender_mail-id',file.readline())
    server.sendmail('sender_mail-id', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        file = 'None'

        if 'wikipedia' in query:
            speak('What do you want me to search for ?')
            query = takeCommand()
            speak_slow('Searching, %s in Wikipedia...' %query)
            results = wikipedia.summary(query, sentences = 2)
            speak('According to Wikipedia')
            print(results+'\n')
            speak_slow(results)

        elif 'open youtube' in query:
            url = "https://www.youtube.com/"
            speak('Should i close the program while opening youtube Sir')
            cmd = takeCommand()
            speak('opening youtube')
            webbrowser.get().open_new_tab(url)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            continue
        
        elif 'open google' in query:
            url = "https://www.google.co.in/"
            speak('Should i close the program while opening google Sir')
            cmd = takeCommand()
            speak('opening google')
            webbrowser.get().open_new_tab(url)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            continue
            
        elif 'play song' in query:
            # enter the songs folder path 
            song_dir = 'songs_folder_path'

            #TO PRINT THE LIST OF THE SONGS 
            
            a=1
            ls1 = list()
            ls2 = list()
            for name in os.listdir(song_dir):
                ls1.append(a)
                ls2.append(name)
                a +=1
            b=0
            while b < len(os.listdir(song_dir)):
                print(ls1[b],ls2[b])
                b += 1
            print("Speak the file number to play. eg--4")
            speak("Sure Sir, Which File would you like to play")
            # SPEAK THE FILE NUMBER TO PLAY THE SONG --- eg. - 4
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            speak('Should i close the program while playing songs Sir')
            cmd = takeCommand()
            speak('playing song')
            os.startfile(song_dir+'\%s'%ls2[file-1])
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            
        elif 'video song' in query:
            # enter the video songs folder path
            video_dir = 'video-song_folder_path'

            #TO PRINT THE LIST OF THE VIDEO SONGS

            a=1
            ls1 = list()
            ls2 = list()
            for name in os.listdir(video_dir):
                ls1.append(a)
                ls2.append(name)
                a +=1
            b=0
            while b < len(os.listdir(video_dir)):
                print(ls1[b],ls2[b])
                b += 1
            print("Speak the file number to play. eg--4")
            speak("Sure Sir, Which File would you like to play")
            # SPEAK THE FILE NUMBER TO PLAY THE VIDEO SONG --- eg. - 4
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            speak('Should i close the program while playing video songs Sir')
            cmd = takeCommand()
            speak('playing video')
            os.startfile(video_dir+"\%s" %ls2[file-1])            
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            
        elif 'movie' in query:
            # enter the movies folder path
            movie_dir = 'movie_folder_path'

            #TO PRINT THE LIST OF THE MOVIE

            a=1
            ls1 = list()
            ls2 = list()
            for name in os.listdir(movie_dir):
                ls1.append(a)
                ls2.append(name)
                a +=1
            b=0
            while b < len(os.listdir(movie_dir)):
                print(ls1[b],ls2[b])
                b += 1
            print("Speak the file number to play. eg--4")
            speak("Sure Sir, Which File would you like to play")
            # SPEAK THE FILE NUMBER TO PLAY THE MOVIE --- eg. - 4
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            speak('Should i close the program while playing movie Sir')
            cmd = takeCommand()
            speak('playing movie')
            os.startfile(movie_dir+"\%s" %ls2[file-1])            
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()

        elif 'web series' in query:

            # path_syntax = "path\web_series_folder\web_series_particular\web_series_season\web_series_episode"
        
            # example = "D:\Web Series\Sherlock Holmes\Sherlock Holmes S02\Episode-1"
            
            # enter the web series folder path

            web_series_folder = 'web_series_path' #web_series_path = "D:\Web Series"
            a=1
            ls1 = list()
            ls2 = list()
            for name in os.listdir(web_series_folder):
                ls1.append(a)
                ls2.append(name)
                a +=1
            b=0
            while b < len(os.listdir(web_series_folder)):
                print(ls1[b],ls2[b])
                b += 1
            print("Speak the folder number to open. eg--4")
            speak_slow("Sure sir, which series would you like to open")
            # SPEAK THE FILE NUMBER TO OPEN FOLDER
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            web_series_particular = web_series_folder+"\%s" %ls2[file-1]
            web_series = os.listdir(web_series_folder+"\%s" %ls2[file-1])
            ls3 = list(web_series)
            a = 1
            for iter in ls3:
                print(a,iter)
                a+=1
            print("Speak the folder number to open. eg--4")
            speak_slow("Which season would you like to open")
            # SPEAK THE FILE NUMBER TO OPEN SEASON FOLDER
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            a=1
            for iter in ls3:
                if a == file:
                    break
            web_series_season = web_series_particular+"\%s" %iter
            web_series_sea = os.listdir(web_series_particular+"\%s" %iter)
            ls4 = list(web_series_sea)
            a=1 
            for iter in ls4:
                print(a,iter)
                a+=1
            print("Speak the file number to play. eg--4")
            speak_slow("Which episode would you like to play")
            # SPEAK THE FILE NUMBER TO RUN THE EPISODE
            file = cross_check(takeCommand())
            while file == 'None':
                speak_slow('Say file number again please')
                file = cross_check(takeCommand())
            file = int(file)
            a=1
            for iter in ls4:
                if a == file:
                    break
            web_series_episode = os.startfile(web_series_season+"\%s" %iter )


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_slow(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            
            codePath = 'vs_code_path' # enter the vs code application path
            speak('Should i close the program while opening VS-Code Sir')
            cmd = takeCommand()
            speak('opening vs code')
            os.startfile(codePath)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            
        elif 'search' in query:
            speak('What do you want me to search for ?')
            search = takeCommand()
            url = 'https://google.com/search?q='+search
            speak_slow('Should i close the program while searchig %s on google Sir' %search)
            cmd = takeCommand()
            speak('searching %s on google' %search)
            webbrowser.get().open_new_tab(url)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            

        elif 'find on youtube' in query:
            speak('What do you want me to search for ? ')
            search = takeCommand()
            url = 'https://www.youtube.com/results?search_query=' + search
            speak_slow('Should i close the program while searching %s on youtube Sir' %search)
            cmd = takeCommand()
            speak('searching %s on youtube' %search)
            webbrowser.get().open_new_tab(url)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()

        elif 'find location' in query:
            speak('What location should i search for')
            location = takeCommand()
            url = 'https://google.co.in/maps/place/'+location+'/&amp;'
            speak_slow('Should i close the program while searching %s on google maps Sir' %location)
            cmd = takeCommand()
            speak_slow('Here is the location of'+location)
            webbrowser.get().open_new_tab(url)
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
            
        
        elif 'email' in query:
            speak_slow('To whom should i send mail...')
            c = takeCommand()
            C = check_email(c.lower())
            while C!='True':
                # update mail_list.py by adding your receiver name and mail-id
                speak_slow('Sorry... The Receiver is not in the list')
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
                print(e+'\n')
                speak('Sorry Unable to send email at this moment')

        elif 'your master' in query:
            speak_slow('Darshil is my master. He created me...')
        
        elif 'your name' in query:
            speak_slow('My name is JARVIS...')
        
        elif 'stands for' in query:
            speak_slow('JARVIS stands for, JUST A RATHER VERY INTELLIGENT SYSTEM...')

        elif 'github' in query:
            speak_slow('Should i close the program while opening github Sir')
            cmd = takeCommand()
            # enter the github link
            webbrowser.get().open_new_tab('github_link')
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()
        elif 'linkedin' in query:
            speak_slow('Should i close the program while opening linkedin Sir')
            cmd = takeCommand()
            # enter linkedin account link
            webbrowser.get().open_new_tab('linkedin_link')
            if 'yes' in cmd or 'exit' in cmd or 'close' in cmd:
                speak('GoodBye Sir, Have a nice day..!')
                quit()

        elif 'dictionary' in query:
            speak_slow('What do you want me to search in dictionary ? ')
            search = takeCommand()
            translate(search)

        elif 'news' in query:
            speak('Sure sir...')
            speak_news()

        elif 'exit' in query:
            exit()

        elif 'what can you do' in query:
            print(
                ' 1. search wikipedia -- to search in wikipedia\n'+
                ' 2. open youtube -- to open youtube on ms edge\n'+
                ' 3. open google -- to open google on ms edge\n'+
                ' 4. email -- to send email \n'+
                ' 5. play video songs -- to open video song list\n'+
                ' 6. play web series -- to open webseries folder\n'+
                ' 7. play movie -- to open movie list\n'+
                ' 8. play song -- to play songs'
                ' 9. find on youtube -- to search on youtube\n'+
                '10. time -- to display the current time\n'+
                '11. search -- to search on ms edge\n'+
                '12. find location -- to search the user choice location\n'+
                '13. your master -- to know my master\n'+
                '14. your name -- to know my name\n'+
                "15. stands for -- to know my name's full form\n"+
                '16. open code -- to open vs code\n'+
                '17. github -- to open the github\n'+
                '18. linkedin -- to open linkedin account\n'+
                '19. dictionary -- to search for in dictionary\n'+
                '20. news -- to seach the current news\n'+
                '21. exit -- to exit this program\n'
                )
            speak('Sir, I can perform tasks stated below')

        else :
            speak('Cannot recognise the command given...Please speak again..!\n')
