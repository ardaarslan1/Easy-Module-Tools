from gtts import gTTS
import os

text = input("Enter your text: ")
lang = input("Enter your lang: ")

tts = gTTS(text, lang=lang)

tts.save(text.replace(" ", "-")+".mp3")
os.system(text.replace(" ", "-")+".mp3")