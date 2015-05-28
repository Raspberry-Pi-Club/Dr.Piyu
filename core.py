#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2015-04-26 21:03:32
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-05-27 21:42:55
import pyttsx,time,pyaudio,time,wave,sys
from definitions import *
import speech_recognition as sr


r = sr.Recognizer()

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
	print('PIYU CORE v.1.0 - [' + time.strftime("%Y-%m-%d %H:%M:%S") + '] :: ' + '[[Audio]]==>' + a_name + WAV + '\t\t' + '' )
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