import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell' in command:
        person = command.replace('tell', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'dating' in command:
        talk('sorry, I have a headache')
    elif 'what are you doing' in command:
        talk('I am ready for your takecare')
    elif 'what is your name' in command:
        talk('My name is Alexa')
    elif 'thank you' in command:
        talk('you are wellcome')
    elif 'bye' in command:
        talk('ok go and sleep')
    elif 'how are you' in command:
        talk('i am fine and how about you?')
    elif 'fine' in command:
        talk('oh good')
    elif 'how old are you' in command:
        talk('I am 20')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()