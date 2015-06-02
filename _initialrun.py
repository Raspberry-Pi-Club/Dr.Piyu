#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

class init(Exception):	
	try:
		try:
			import pip
			print("Module Found : pip")
		except ImportError as e:
			raise "Module Not Found : pip"

		try:
			import pygame
			print("Module Found : pygame")
		except ImportError as e:
			raise "Module Not Found : pygame"

		try:
			import pyttsx
			print("Module Found : pyttsx")
		except ImportError as e:
			raise "Module Not Found : pyttsx"

		try:
			import pyaudio
			print("Module Found : pyaudio")
		except ImportError as e:
			raise "Module Not Found : pyaudio"

		try:
			import speech_recognition
			print("Module Found : speech_recognition")
		except ImportError as e:
			raise "Module Not Found : speech_recognition"

		try:
			urllib.request.urlopen("http://aroliant.com", timeout=5)
			print("Internet Connected")
		except urllib.error.URLError:
			raise "Internet Connection Failed"

		print("========================")
		print("Runnning Tests : Level 1")

	except ImportError as error:
		raise "Error Occured !"