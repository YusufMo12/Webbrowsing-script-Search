
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)     # Speed of speech
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

text = input("Enter text to convert to sound: ")

engine.say(text)

engine.runAndWait()
