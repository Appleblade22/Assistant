import pyttsx3 as p

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("Hello How Are You Doing?")
engine.say("What is your name?")
engine.runAndWait()