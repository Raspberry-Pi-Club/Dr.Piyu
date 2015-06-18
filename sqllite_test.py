import sqlite3

SQLConnection = sqlite3.connect('C:\wamp\www\Piyu-UI\database\interface.db')

c = SQLConnection.cursor()




#Getting Insertion time
insertionTime = ''
for row in c.execute("SELECT datetime('now','localtime')"):
	insertionTime = row[0]

#Setting Last Fetch Date to DB
print(insertionTime)
c.execute("UPDATE last_fetch SET time='%s' WHERE sid = 1" % insertionTime)

#Getting Last Fetch Time from DB
for lfTime in c.execute("SELECT time FROM last_fetch WHERE sid = 1"):
	print(lfTime[0])

#Last Inserted ID
toFetchID = 1
toExeCommand = ''
for lid in c.execute("SELECT sno,command FROM commands WHERE fetched=0"):
	toFetchID = lid[0]
	toExeCommand = lid[1]
	break

print(str(toFetchID) + toExeCommand)

# 1. Set last fetch id
# 2. Set last fetch time and date
# 3. Set both on the commands database
# LOOP