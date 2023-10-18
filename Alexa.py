import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices [1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        print("except")
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'search' in command:
        key = command.replace('search' , '')
        print('searching' + key)
        talk('searching ' + key)
        pywhatkit.search(key)


    elif 'send in whatsapp' in command:
        sending = command.replace('send in whatsapp ','')
        print(sending)
        talk("sending" + sending)
        this = input("type the mobile number:")
        pywhatkit.sendwhatmsg(this, sending, 13, 28)
        print('sent')


    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)


    elif 'joke' in command:
        l = pyjokes.get_joke()
        print(l)
        talk(l)
    elif 'i have no idea what you said' in command:
        print("that's because you are dumb")
        talk("That's because you are dumb")


    elif 'goodbye Alexa' in command:
        print('goodbye ')
        talk('goodbye')

    else:
        print('please say the command again')



def mymain():
    engine.say('Hi i am Siri. What can i do for you')
    engine.runAndWait()
    while True:
       run_alexa()

mymain()