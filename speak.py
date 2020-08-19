import json
from difflib import get_close_matches
import pyttsx3
import requests
import speech_recognition as sr
from num import check

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 180)
data = json.load(open('data.json'))


def speak(audio):
    """This function converts text arguments given into voice"""
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    """This function reads the current news going on.
    Return -> None """

    site = ('http://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey= #############')  # enter api key (Find API key in the Readme section
    news = requests.get(site).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        print(int(index) + 1, end=' ')
        print(articles['title'] + '\n')
        speak(articles['title'])
        if index == len(arts) - 1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')


def takeCommand():
    """Uses the microphone as input source and recognizes the user command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening...')
        r.pause_threshold = 1
        r.energy_threshold = 495
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)
    try:
        print('Recognizing...\n')
        query = r.recognize_google(audio, language='en-US').lower()
        print(f"User said: {query} .\n")
    except Exception:
        print('Say that again please...')
        speak('Say that again please')
        return "empty"
    return query


def command(query):
    """Checks for the statement to break the program or to go back in main program """
    if 'back' in query or 'cancel' in query or 'no' in query:
        return 'None'
    elif 'exit' in query or 'quit' in query or 'close' in query or 'yes' in query or 'sure' in query:
        speak('Exiting program, Have a Good Day Sir..!')
        return 'exit'
    return query


def cross_check(word):
    """It cross checks a word whether it exists in number or not"""
    for letter in word.split():
        if letter.isdigit():
            return letter
        else:
            continue

    # if digit is not recognised spell number in words like --" o n e "

    word = word.lower()
    if len(get_close_matches(word, data.keys())) > 0:
        for _ in range(len(get_close_matches(word, data.keys()))):
            x = get_close_matches(word, data.keys())[_]
            print(('Did you mean ' + x +
                   ' instead,  respond with Yes or No.\n'))
            speak('Did you mean ' + x +
                  ' instead,  respond with Yes or No.')
            ans = takeCommand().lower()
            if 'no' in ans:
                return 'None'
            else:
                return check(x)
    else:
        print("Word doesn't exist. Please double check it.\n")
        speak("Word doesn't exist. Please double check it.")
        return 'None'


if __name__ == "__main__":
    speak('Hello Sir')
    speak_news()
