#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2015-04-26 23:09:28
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-04-26 23:09:31
import pyaudio,os
import speech_recognition as sr


def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize(audio)
    print(user)
    if user == "Excel":
        excel()
    elif user == "Internet":
        internet()
    elif user == "music":
        media()

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)