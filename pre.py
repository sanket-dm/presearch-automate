print("Please wait a few seconds... \nPopulating the lists...\n")

import webbrowser
import time
import random
from random_word import RandomWords

obj = RandomWords()
randomWords = []
for i in range(1,150):
	randomWords.append(obj.get_random_word())

print("\nEnjoy your PRE tokens :)\n")

resultantList = []
for i in randomWords:
    if i not in resultantList:
        resultantList.append(i)

print("\n<---------- Browser Set 1 ---------->\n")

for i in range(1,31):
	print ('Current Iteration: ',i) 
	url1 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url2 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url3 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'

	webbrowser.register('edge',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
	webbrowser.get('edge').open(url1)
	time.sleep(random.uniform(2, 3))

	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url2)
	time.sleep(random.uniform(2, 3))
	
	webbrowser.register('brave',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
	webbrowser.get('brave').open(url3)
	time.sleep(random.uniform(2, 3))

	time.sleep(random.randint(15,20))    
	
	if i%10 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM brave.exe")
			time.sleep(random.uniform(2, 3))
			break 

time.sleep(random.randint(10,15))

print("\n<---------- Browser Set 2 ---------->\n")

for i in range(1,31):
	print ('Current Iteration: ',i) 
	url4 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url5 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'
	url6 = f'https://presearch.com/search?q={random.choice(resultantList)}+{random.choice(resultantList)}+{random.choice(resultantList)}'

	webbrowser.register('edge-dev',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge Dev//Application//msedge.exe"))
	webbrowser.get('edge-dev').open(url4)
	time.sleep(random.uniform(2, 3))

	webbrowser.register('edge-canary',
		None,
		webbrowser.BackgroundBrowser("C://Users//sanke//AppData//Local//Microsoft//Edge SxS//Application//msedge.exe"))
	webbrowser.get('edge-canary').open(url5)
	time.sleep(random.uniform(2, 3))

	webbrowser.register('edge-beta',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge Beta//Application//msedge.exe"))
	webbrowser.get('edge-beta').open(url6)
	time.sleep(random.uniform(2, 3))

	time.sleep(random.randint(15,20))    
	
	if i%10 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			time.sleep(random.uniform(2, 3))
			break 
