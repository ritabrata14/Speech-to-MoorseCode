# Program to convert speech to text
# Author @inforkgodara

import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()

print('start')
with mic as source:
    audio = r.listen(source)
print('end')
#print(r.recognize_google(audio))

from morse import MorseCodeTranslator

translator = MorseCodeTranslator()

# Translate text to morse code
morse = translator.translate_text(r.recognize_google(audio))

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)