#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyttsx,time,pyaudio,time,wave,sys
from definitions import *
import speech_recognition as sr


r = sr.Recognizer()

def log(d):
	t = '[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] :: '
	fileLocation = "C:\wamp\www\Piyu-UI\interface.txt"
	_file = open(fileLocation,"a")
	_file.write(t + d+"\n")
	_file.close()
	print(t + d)

def say(word):
	engine = pyttsx.init()
	engine.setProperty('rate', RATE)
	engine.say(word)
	engine.runAndWait()


def speak(a_name,lang):	
	CHUNK = 1024
	if(lang=='ta'):
		BASE_DIR	=	'voices\\tamil'
	else:
		BASE_DIR	=	'voices'
	audioFileName = BASE_DIR + '\\' + a_name + WAV
	try:
		wf = wave.open(audioFileName, 'rb')
	except FileNotFoundError:
		wf = wave.open('voices\\beep'+ WAV, 'rb')
	p = pyaudio.PyAudio()
	_log = '' + '[[Audio]]==>' + a_name + WAV + '\t\t' + ''
	print('PIYU CORE v.1.0 - '+ _log)
	log(_log)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)
	data = wf.readframes(CHUNK)

	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()
	p.terminate()
	


def action(source):
    audio = r.listen(source)
    try:
    	r.recognize(audio)
    	txtData = r.recognize(audio)
    	print(txtData)
    	#mapText(txtData);   
    except (KeyboardInterrupt, SystemExit):
        raise
    except LookupError:
    	speak(VOICE.repeat)
    	sleepTime = getSleepTime(VOICE.repeat)
    	print("Sleeping....")
    	print(sleepTime)
    	time.sleep(.1)
    	print("Wokeup...")
    

def listen():	
	with sr.Microphone() as source:                # use the default microphone as the audio source
		while(1):
			print("Listening....")
			action(source)                   # listen for the first phrase and extract it into audio data
			

def mapText(data):
    txts = TXT();
    txts =  [txts for txts in dir(txts) 
              if not txts.startswith('__')]

    var1 = TXT();
    obj_found = False
    for txt in txts:
        #print(var1.__getitem__(txt))
        if(data in var1.__getitem__(txt)):
            obj_found = True
            return str(txt)

    if(obj_found == False):
        return 'repeat'

def mapTextTamil(data):
    txts = TXTtamil();
    txts =  [txts for txts in dir(txts) 
              if not txts.startswith('__')]

    var1 = TXTtamil();
    obj_found = False
    for txt in txts:
        #print(var1.__getitem__(txt))
        if(data in var1.__getitem__(txt)):
            obj_found = True
            return str(txt)

    if(obj_found == False):
        return 'repeat'


class pre:
    def time():
        speak(getattr(TAMIL,'time'),'ta')
        speak(getattr(TAMIL,'_'+ time.strftime("%H")),'ta')
        speak(getattr(TAMIL,'hour'),'ta')
        speak(getattr(TAMIL,'_'+ time.strftime("%M")),'ta')
        speak(getattr(TAMIL,'minute'),'ta')

    def date():
        speak(getattr(TAMIL,'today'),'ta')
        speak(getattr(TAMIL,'twothousand'),'ta')
        speak(getattr(TAMIL,'_'+ time.strftime("%Y").strip('20')),'ta')
        speak(getattr(TAMIL,'aam'),'ta')
        speak(getattr(TAMIL,'year'),'ta')
        speak(getattr(TAMIL,time.strftime("%B").lower()),'ta')
        speak(getattr(TAMIL,'month'),'ta')
        speak(getattr(TAMIL,'_'+str(int(time.strftime("%d")))),'ta')
        speak(getattr(TAMIL,'aam'),'ta')
        speak(getattr(TAMIL,'day'),'ta')

