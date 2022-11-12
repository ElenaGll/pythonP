import pyttsx3


def speak(frase):
    speak = pyttsx3.init()
    speak.say(frase)
    speak.runAndWait()
    speak.stop()
