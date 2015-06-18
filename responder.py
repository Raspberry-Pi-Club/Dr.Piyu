import time,os
import speech_recognition as sr
from core import *
from definitions import *
import sqlite3


while True:	
	SQLConnection = sqlite3.connect('C:\wamp\www\Piyu-UI\database\interface.db')
	c = SQLConnection.cursor()
	#Last Inserted ID
	toFetchID = -1
	toExeCommand = ''
	for lid in c.execute("SELECT sno,command FROM commands WHERE fetched=0"):
		toFetchID = lid[0]
		toExeCommand = lid[1]
		break
	print(toFetchID)
	print(toExeCommand)
	if(toFetchID==-1):
		time.sleep(1)
	else:
		mappeddata = mapText(toExeCommand)
		speak(mappeddata,'en')
		#Getting Insertion time
		insertionTime = ''
		for row in c.execute("SELECT datetime('now','localtime')"):
			insertionTime = row[0]

		#Setting Last Fetch Date to DB
		print(insertionTime)
		# 1. Set last fetch id
		# 2. Set last fetch time and date
		c.execute("""UPDATE last_fetch SET time='%s', lf_id=%d WHERE sid = 1"""% (insertionTime,toFetchID))
		SQLConnection.commit()
		
		# 3. Set both on the commands database
		c.execute("""UPDATE commands SET fetched = 1 WHERE sno = %d"""% toFetchID)
		SQLConnection.commit()
		c.close()

	