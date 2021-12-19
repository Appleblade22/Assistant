from datetime import datetime

from FUNCTION.speak import speak
USERNAME = 'APPLE'
BOTNAME = 'TANISHA'


def greet_user():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning " + USERNAME)
    elif 12 <= hour < 16:
        speak("Good Afternoon " + USERNAME)
    elif 16 <= hour < 19:
        speak("Good Evening " + USERNAME)
    else:
        speak("Good Night " + USERNAME)
    speak("I am " + BOTNAME + " How may I help you?")