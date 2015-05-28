import time
import speech_recognition as sr
from core import *
from definitions import *

#say("Hello") 			#text to speech
#speak('name') 		#play recorded audio files by mapping internal database


def callback(recognizer, audio):
    try:
        txtData = recognizer.recognize(audio)
        print(txtData)
        mappeddata = mapText(txtData)
        if(mappeddata=='repeat'):
        	speak('repeat','en')
        	print('repeat')
        else:
        	speak(mappeddata,'en')
        	print(txtData)
    except LookupError:
        speak('repeat','en')


#Tamil Version
def callbackTamil(recognizer, audio):
	try:
		txtData = recognizer.recognize(audio)
		print(txtData)
		mappeddata = mapTextTamil(txtData)
		if(mappeddata=='repeat'):
			speak(getattr(TAMIL,'repeat'),'ta')
			print('repeat')
		else:
			speak(getattr(TAMIL,mappeddata),'ta')
			print(txtData)
	except LookupError:
		speak(getattr(TAMIL,'repeat'),'ta')

r = sr.Recognizer()
r.energy_threshold = 4000
with sr.Microphone() as source:
	print('Adjusting ambient noise')
	r.adjust_for_ambient_noise(source, duration = 1)

print('Starting Background Service')
r.listen_in_background(sr.Microphone(), callbackTamil)

while True: time.sleep(0.1)     
