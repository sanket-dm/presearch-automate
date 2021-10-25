print("Please wait: loading the necessary things...")

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
	import webbrowser
	url = f'https://engine.presearch.org/search?q={random.choice(resultantList)}+{random.choice(resultantList)}'
	
	webbrowser.register('edge',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
	webbrowser.get('edge').open(url)

	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)
	
	webbrowser.register('firefox',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
	webbrowser.get('firefox').open(url)

	sleepTime = random.randint(10,30)
	time.sleep(sleepTime)
	print ('iteration: ',i)     
	
	if i%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM firefox.exe")
			break 
