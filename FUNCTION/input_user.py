from datetime import datetime
import speech_recognition as sr
from random import choice

from FUNCTION.speak import speak
from FUNCTION.util import opening_text


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if 'exit' not in query or 'stop' not in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()

    except sr.UnknownValueError as e:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))
        query = 'None'
    return query
