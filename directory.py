import os
from speak import speak, takeCommand, command, cross_check


def directory(filepath):
    """Searches for the file in the provides filepath as Argument and opens it"""
    file = 'empty'
    cmd = 'empty'
    count = 1
    ls1 = list()
    ls2 = list()
    for name in os.listdir(filepath):
        ls1.append(count)
        ls2.append(name)
        count += 1
    file_num = 0
    while file_num < len(os.listdir(filepath)):
        print(ls1[file_num], ls2[file_num])
        file_num += 1
    print("\nSpeak the file number to open. eg--4")
    speak("Sure Sir")

    # SPEAK THE FILE NUMBER TO PLAY THE SONG --- eg. - 4

    while file == 'empty':
        speak('Which File would you like to open')
        file = command(takeCommand())
        if file == 'None':
            return "None"
        elif file == 'exit':
            exit()
        file = cross_check(file)
        if file.isdigit():
            if int(file) < count:
                break
            else:
                file = 'empty'
                continue
        else:
            file = 'empty'
        speak('Please speak the file number to open')
    file = int(file)

    if 'series' in filepath.lower():
        web_series_particular = filepath + "\%s" % ls2[file - 1]
        web_series = os.listdir(filepath + "\%s" % ls2[file - 1])
        ls3 = list(web_series)
        count = 1
        for a in ls3:
            print(count, a)
            count += 1
        print("\nSpeak the folder number to open. eg--4\n")

        # SPEAK THE FILE NUMBER TO OPEN SEASON FOLDER

        file = 'empty'
        while file == 'empty':
            speak("Which season would you like to open")
            file = command(takeCommand())
            if file == 'None':
                return "None"
            elif file == 'exit':
                exit()
            file = cross_check(file)
            if file.isdigit():
                if int(file) < count:
                    break
                else:
                    file = 'empty'
                    continue
            else:
                file = 'empty'
            speak('Please speak the file number to open')
        file = int(file)
        count = 1
        for a in ls3:
            if count == file:
                break
        # noinspection PyUnboundLocalVariable
        web_series_season = web_series_particular + f"{a}"
        web_series_sea = os.listdir(web_series_particular + "\%s" % a)
        ls4 = list(web_series_sea)
        count = 1
        for a in ls4:
            print(count, a)
            count += 1
        print("\nSpeak the file number to play. eg--4\n")

        # SPEAK THE FILE NUMBER TO RUN THE EPISODE

        file = 'empty'
        while file == 'empty':
            speak("Which episode would you like to play")
            file = command(takeCommand())
            if file == 'None':
                return "None"
            elif file == 'exit':
                exit()
            elif file == 'empty':
                continue
            file = cross_check(file)
            if file.isdigit():
                if int(file) < count:
                    break
                else:
                    file = 'empty'
                    continue
            else:
                file = 'empty'
            speak('Please speak the file number to open')
        file = int(file)
        count = 1
        for a in ls4:
            if count == file:
                break
        while cmd == 'empty':
            speak('Should i close the program while playing series Sir')
            cmd = command(takeCommand())
        speak('playing series')
        os.startfile(web_series_season + "\%s" % a)
        if cmd == 'None':
            return 'None'
        elif cmd == 'exit':
            exit()

    else:
        while cmd == 'empty':
            speak('Should i close the program while opening File Sir')
            cmd = command(takeCommand())
        speak('opening file')
        os.startfile(filepath + '\%s' % ls2[file - 1])
        if cmd == 'None':
            return 'None'
        elif cmd == 'exit':
            exit()


if __name__ == "__main__":
    directory('C:\\Users\\DARSHIL\\OneDrive_1\\OneDrive\\Pictures\\Saved Pictures')
