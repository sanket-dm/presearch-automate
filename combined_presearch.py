print("Please wait: loading the necessary things...")

import webbrowser
import time
import random
from random_word import RandomWords

x = RandomWords()
randomWords1 = x.get_random_words()
time.sleep(1)
randomWords2 = x.get_random_words()	
combinedWords = randomWords1 + randomWords2

resultantList = []
for i in combinedWords:
    if i not in resultantList:
        resultantList.append(i)

for i in range(1,36):
	print ('iteration: ',i) 
	url1 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'
	url2 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'
	url3 = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'

	webbrowser.register('edge',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
	webbrowser.get('edge').open(url1)
	time.sleep(0.5)

	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url2)
	time.sleep(0.5)
	
	webbrowser.register('firefox',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
	webbrowser.get('firefox').open(url3)

	sleepTime = random.randint(15,30)
	time.sleep(sleepTime)    
	
	if i%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM firefox.exe")
			time.sleep(2)
			break 
