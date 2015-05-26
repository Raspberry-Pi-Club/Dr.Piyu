#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2015-04-26 21:03:32
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-04-27 00:01:11
import pyttsx,pygame,time
from definitions import *
import speech_recognition as sr


r = sr.Recognizer()

def getSleepTime(a_name):
	pygame.init()	
	length = pygame.mixer.Sound(BASE_DIR + '\\' + a_name + WAV)
	return length.get_length()

def say(word):
	engine = pyttsx.init()
	engine.setProperty('rate', RATE)
	engine.say(word)
	engine.runAndWait()


def speak(a_name):	
	#pygame.init()
	pygame.mixer.init(22100)
	pygame.display.set_mode((1,1))
	pygame.mixer.music.load(BASE_DIR + '\\' + a_name + WAV)
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(10)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(10)  

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
    	#time.sleep(sleepTime)
    	print("Wokeup...")
    

def listen():	
	with sr.Microphone() as source:                # use the default microphone as the audio source
		while(1):
			print("Listening....")
			action(source)                   # listen for the first phrase and extract it into audio data
			

