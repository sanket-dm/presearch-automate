print("Please wait 5 seconds...")

import webbrowser
import time
import random
from random_word import RandomWords

x = RandomWords()
randomWords1 = x.get_random_words()
time.sleep(random.uniform(0.2, 0.5))
randomWords2 = x.get_random_words()

combinedWords = randomWords1 + randomWords2 

resultantList = []
for i in combinedWords:
    if i not in resultantList:
        resultantList.append(i)

print("\n<---------- Round 1 ---------->\n")

for i in range(1,36):
	print ('iteration: ',i) 
	url1 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'
	url2 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url3 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'

	webbrowser.register('edge',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
	webbrowser.get('edge').open(url1)
	time.sleep(random.uniform(1, 1.7))

	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url2)
	time.sleep(random.uniform(1, 1.7))
	
	webbrowser.register('firefox',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
	webbrowser.get('firefox').open(url3)
	time.sleep(random.uniform(1, 1.7))

	time.sleep(random.randint(15,30))    
	
	if i%7 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM firefox.exe")
			time.sleep(random.uniform(2, 3))
			break 

time.sleep(random.randint(10,15))

x = RandomWords()
randomWords1 = x.get_random_words()
time.sleep(random.uniform(0.2, 0.5))
randomWords2 = x.get_random_words()	

combinedWords = randomWords1 + randomWords2 

resultantList = []
for i in combinedWords:
    if i not in resultantList:
        resultantList.append(i)

print("\n<---------- Round 2 ---------->\n")

for i in range(1,36):
	print ('iteration: ',i) 
	url4 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url5 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'
	url6 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'

	webbrowser.register('brave',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
	webbrowser.get('brave').open(url4)
	time.sleep(random.uniform(1, 1.7))

	webbrowser.register('opera',
		None,
		webbrowser.BackgroundBrowser("C://Users//sanke//AppData//Local//Programs//Opera//opera.exe"))
	webbrowser.get('opera').open(url5)
	time.sleep(random.uniform(1, 1.7))

	webbrowser.register('vivaldi',
		None,
		webbrowser.BackgroundBrowser("C://Users//sanke//AppData//Local//Vivaldi//Application//vivaldi.exe"))
	webbrowser.get('vivaldi').open(url6)
	time.sleep(random.uniform(1, 1.7))

	time.sleep(random.randint(15,30))    
	
	if i%7 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM opera.exe")
			os.system("TASKKILL /F /IM brave.exe")
			os.system("TASKKILL /F /IM vivaldi.exe")
			time.sleep(random.uniform(2, 3))
			break 
