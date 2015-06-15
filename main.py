import time
import speech_recognition as sr
from core import *
from definitions import *
import json

say("Test") 			#text to speech
#speak(getattr(TAMIL,'name') ,'ta') 		#play recorded audio files by mapping internal database

f = open('C:\wamp\www\Piyu-UI\interface.txt',"w")
f.write("\n\n")
f.close()


def callback(recognizer, audio):
    try:
        txtData = recognizer.recognize(audio)
        print(txtData)
        mappeddata = mapText(txtData)
        if(mappeddata=='repeat'):
        	speak('repeat','en')
        	print('repeating')
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

# r = sr.Recognizer()
# r.energy_threshold = 4000
# with sr.Microphone() as source:
# 	print('Adjusting ambient noise')
# 	r.adjust_for_ambient_noise(source, duration = 5)

# print('Starting Background Service')
# r.listen_in_background(sr.Microphone(), callback)

# while True: time.sleep(0.1)     


def listen():	
	with sr.Microphone() as source:
		while(1):
			log("Listening....")
			action(source)

def action(source):
    audio = r.listen(source)
    try:
    	txt = r.recognize(audio)
    	print(txt)
    	#read
    	readlisten = open('C:\wamp\www\Piyu-UI\interface.json',"r")
    	load = json.load(readlisten)
    	load['listen'] = "0"
    	readlisten.close()
    	#write
    	f = open('C:\wamp\www\Piyu-UI\interface.json',"w")
    	f.write(load)
    	f.close()

    except LookupError:
    	log("Error")
    	# speak(VOICE.repeat)
    	# sleepTime = getSleepTime(VOICE.repeat)
    	# print("Sleeping....")
    	# print(sleepTime)
    	# time.sleep(sleepTime)
    	# print("Wokeup...")

def listenBackend():
	try:
		#print("entering")
		readlisten = open('C:\wamp\www\Piyu-UI\interface.json',"r")
		option = json.load(readlisten)		
		if(option['listen']=="1"):
			listen()
		elif(option['listenTamil']=="1"):
			pass		
		log('looping')
		time.sleep(.5)
		listenBackend()
		readlisten.close()
	except():
		pass


listenBackend()