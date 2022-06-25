print("Please wait 10 seconds... \nPopulating the lists...")

import webbrowser
import time
import random
from random_word import RandomWords

x = RandomWords()

randomWords1 = x.get_random_words()
time.sleep(random.uniform(0.2, 0.5))
randomWords2 = x.get_random_words()

time.sleep(1)

randomWords3 = x.get_random_words()
time.sleep(random.uniform(0.2, 0.5))
randomWords4 = x.get_random_words()	

combinedWords1 = randomWords1 + randomWords2 
combinedWords2 = randomWords3 + randomWords4

resultantList1 = []
for i in combinedWords1:
    if i not in resultantList1:
        resultantList1.append(i)

resultantList2 = []
for i in combinedWords2:
    if i not in resultantList2:
        resultantList2.append(i)

print("\n<---------- Round 1 ---------->\n")

for i in range(1,36):
	print ('iteration: ',i) 
	url1 = f'https://presearch.com/search?q={random.choice(resultantList1)}+{random.choice(resultantList1)}+{random.choice(resultantList1)}'
	url2 = f'https://presearch.com/search?q={random.choice(resultantList1)}+{random.choice(resultantList1)}+{random.choice(resultantList1)}'
	url3 = f'https://presearch.com/search?q={random.choice(resultantList1)}+{random.choice(resultantList1)}+{random.choice(resultantList1)}'

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

	time.sleep(random.randint(15,30))    
	
	if i%7 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM brave.exe")
			time.sleep(random.uniform(2, 3))
			break 

time.sleep(random.randint(10,15))

print("\n<---------- Round 2 ---------->\n")

for i in range(1,36):
	print ('iteration: ',i) 
	url4 = f'https://presearch.com/search?q={random.choice(resultantList2)}+{random.choice(resultantList2)}+{random.choice(resultantList2)}'
	url5 = f'https://presearch.com/search?q={random.choice(resultantList2)}+{random.choice(resultantList2)}+{random.choice(resultantList2)}'
	url6 = f'https://presearch.com/search?q={random.choice(resultantList2)}+{random.choice(resultantList2)}+{random.choice(resultantList2)}'

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

	time.sleep(random.randint(15,30))    
	
	if i%7 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			time.sleep(random.uniform(2, 3))
			break 
