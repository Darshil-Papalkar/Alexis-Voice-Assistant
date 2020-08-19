import datetime
import json
import os
import smtplib
import webbrowser
from difflib import get_close_matches
import wikipedia
from directory import directory
from mail_list import mail, check_email
from speak import speak, speak_news, takeCommand, command

data = json.load(open('data.json'))


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0:
        if hour < 12:
            speak('Good Morning Sir!')
        elif hour >= 12:
            if hour < 18:
                speak('Good Afternoon Sir!')
        else:
            speak('Good Evening!')
    speak('I am, Alexis sir. How may i help you?')


def translate(word):
    word = word.lower()
    if word in data:
        speak('%s means' % word)
        print(data[word])
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        print(('Did you mean ' + x +
               ' instead,  respond with Yes or No.'))
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = 'empty'
        while ans == 'empty':
            ans = command(takeCommand().lower())
            if ans == 'exit':
                exit()
            else:
                ans = 'empty'
            speak("We didn't understand your entry.")
            speak('Please state yes or no..')
        if 'yes' in ans or 'ok' in ans:
            print(data[x])
        elif 'no' in ans:
            print("Word doesn't exist. Please make sure you spelled it correctly.\n")
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
    else:
        print("Word doesn't exist. Please double check it.")
        speak("Word doesn't exist. Please double check it.")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # enter file_path of password stored in text file

    file = open('file_path_of_text_file_of_password', 'r')
    server.login("sender's_main_id", file.readline())
    server.sendmail("sender's_mail_id", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        find = 'empty'
        cmd = 'empty'
        query = takeCommand().lower()

        if 'wikipedia' in query:
            while find == 'empty':
                speak('What do you want me to search for ?')
                find = command(takeCommand())
            if find == 'None':
                speak("Going back to main program...Continuing")
                continue
            elif find == 'exit':
                exit()
            speak('Searching, %s in Wikipedia...' % find)
            results = wikipedia.summary(find, sentences=2)
            speak('According to Wikipedia')
            print(results + '\n')
            speak(results)

        elif 'open youtube' in query:
            site = "https://www.youtube.com/"
            while cmd == 'empty':
                speak('Should i close the program while opening youtube Sir')
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('opening youtube')
            webbrowser.get().open_new_tab(site)
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'open google' in query:
            site = "https://www.google.co.in/"
            while cmd == 'empty':
                speak('Should i close the program while opening google Sir')
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('opening google')
            webbrowser.get().open_new_tab(site)
            if cmd == 'None':
                speak('Going back to main program, Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'video song' in query:

            # enter the video songs folder path

            video_dir = 'video_song_folder_path'
            file = directory(video_dir)
            if file == 'None':
                speak('Going back to main program, Continuing')
                continue

        elif 'song' in query or 'music' in query:

            # enter the songs folder path

            song_dir = 'music_folder_path'
            file = directory(song_dir)
            if file == 'None':
                speak('Going back to main program, Continuing')
                continue


        elif 'movie' in query:

            # enter the movies folder path

            movie_dir = 'movie_folder_path'
            file = directory(movie_dir)
            if file == 'None':
                speak('Going back to main program, Continuing')
                continue


        elif 'web series' in query:

            # path_syntax = "path\web_series_folder\web_series_particular\web_series_season\web_series_episode"
            # example = "D:\Web Series\Sherlock Holmes\Sherlock Holmes S02\Episode-1"
            # enter the web series folder path

            web_series_folder = 'path\web_series_folder_path'   # D:\Web Series
            file = directory(web_series_folder)
            if file == 'None':
                speak('Going back to main program, Continuing')
                continue

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:

            # enter the vs code application path

            codePath = 'vs_code_path'
            while cmd == 'empty':
                speak('Should i close the program while opening VS-Code Sir')
                cmd = command(takeCommand())
                if cmd == 'exit' or cmd == 'None':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('opening VS Code')
            os.startfile(codePath)
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            if cmd == 'exit':
                exit()

        elif 'find on youtube' in query or 'search on youtube' in query:
            while find == 'empty':
                speak('What do you want me to search for ? ')
                find = command(takeCommand())
            if find == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif find == 'exit':
                exit()
            site = 'https://www.youtube.com/results?search_query=' + find
            while cmd == 'empty':
                speak('Should i close the program while searching %s on youtube Sir' % find)
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('searching %s on youtube' % find)
            webbrowser.get().open_new_tab(site)
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'find location' in query or 'search location' in query:
            while find == 'empty':
                speak('What location should i search for')
                find = command(takeCommand())
            if find == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif find == 'exit':
                exit()
            site = 'https://google.co.in/maps/place/' + find + '/&amp;'
            cmd = 'empty'
            while cmd == 'empty':
                speak('Should i close the program while searching %s on google maps Sir' % find)
                cmd = command(takeCommand())
                if cmd == 'exit' or cmd == 'None':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('Here is the location of' + find)
            webbrowser.get().open_new_tab(site)
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'search' in query:
            while find == 'empty':
                speak('What do you want me to search for ?')
                find = command(takeCommand())
            if find == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif find == 'exit':
                exit()
            site = 'https://google.com/search?q=' + find
            while cmd == 'empty':
                speak('Should i close the program while searching %s on google Sir' % find)
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue
            speak('searching %s on google' % find)
            webbrowser.get().open_new_tab(site)
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'github' in query:
            while cmd == 'empty':
                speak('Should i close the program while opening github Sir')
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue

            # enter the github link

            webbrowser.get().open_new_tab('github_link')
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'linkedin' in query:
            while cmd == 'empty':
                speak('Should i close the program while opening linkedin Sir')
                cmd = command(takeCommand())
                if cmd == 'None' or cmd == 'exit':
                    break
                else:
                    cmd = 'empty'
                    continue

            # enter linkedin account link

            webbrowser.get().open_new_tab('linkedin_link')
            if cmd == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif cmd == 'exit':
                exit()

        elif 'dictionary' in query:
            while find == 'empty':
                speak('What do you want me to search in dictionary ? ')
                find = command(takeCommand())
            if find == 'None':
                speak('Going back to main program...Continuing')
                continue
            elif find == 'exit':
                exit()
            translate(find)

        elif 'mail' in query:
            C = 'False'
            completed = False
            while find == 'empty':
                done = False
                while C != 'True':
                    speak('To whom should i send mail...')
                    find = command(takeCommand())
                    if find == 'None':
                        done = True
                        break
                    elif find == 'exit':
                        exit()
                    C = check_email(find.lower())
                    if find == 'empty':
                        continue
                    elif C == 'False':
                        speak('Sorry.. The receiver is not in the list..')
                        continue
                if done:
                    completed = True
                    break
            if completed:
                speak("Going back to main program... Continuing")
                continue
            client, receiver = mail(find)
            try:
                content = 'empty'
                finish = False
                while content == 'empty':
                    speak(f'What should i deliver to {client} ?')
                    content = command(takeCommand())
                if content == "None":
                    speak('Going back to main program..Continuing')
                    continue
                elif content == 'exit':
                    exit()
                content = content.capitalize() + " ."
                to = receiver
                sendEmail(to, content)
                speak('Email Has been sent')
            except Exception as e:
                print(e, "\n")
                speak('Sorry Unable to send email at this moment')

        elif 'how are you' in query:
            speak('I am fine sir, Good to see you back')

        elif 'master' in query:
            speak('Darshil, is my master. He created me...')

        elif 'your name' in query or 'who are you' in query:
            speak('My name is Alexis...')

        elif 'stands for' in query:
            print(
                'Alexis is a given name derived from several saints venerated by the Eastern Orthodox and Roman '
                'Catholic churches, including Saint Alexis of Rome. Alexis means "helper, defender".')
            speak(
                'Alexis is a given name derived from several saints venerated by the Eastern Orthodox and Roman '
                'Catholic churches, including Saint Alexis of Rome. Alexis means "helper, defender".')

        elif 'news' in query:
            speak('Sure sir...')
            speak_news()

        elif 'back' in query:
            speak('Already in the main program sir')
            continue

        elif 'exit' in query:
            exit()

        elif 'what can you perform' in query:
            print(
                ' 1. search wikipedia -- to search in wikipedia\n' +
                ' 2. open youtube -- to open youtube on ms edge\n' +
                ' 3. open google -- to open google on ms edge\n' +
                ' 4. email -- to send email \n' +
                ' 5. open code -- to open vs code\n' +
                ' 6. github -- to open the github\n' +
                ' 7. linkedin -- to open linkedin account\n' +
                ' 8. dictionary -- to search for in dictionary\n' +
                ' 9. news -- to seach the current news\n' +
                '10. play video songs -- to open video song list\n' +
                '11. play web series -- to open webseries folder\n' +
                '12. play movie -- to open movie list\n' +
                '13. play song -- to play songs'
                '14. find on youtube -- to search on youtube\n' +
                '15. time -- to display the current time\n' +
                '16. search -- to search on ms edge\n' +
                '17. find location -- to search the user choice location\n' +
                '18. how are you -- to know the current condition\n' +
                '19. your master name -- to know my master\n' +
                '20. your name -- to know my name\n' +
                "21. stands for -- to know my name's full form\n" +
                '22. back -- to go back to the main program\n' +
                '23. exit -- to exit this program at any time\n'
            )
            speak('Sir, I can perform tasks stated below')

        else:
            speak('Cannot recognise the command given...Please speak again..!\n')
