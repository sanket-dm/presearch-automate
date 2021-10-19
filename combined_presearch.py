import time
import random
from random_word import RandomWords
r = RandomWords()
rWords = r.get_random_words()	

for i in range(1,36):
	import webbrowser
	url = f'https://engine.presearch.org/search?q={random.choice(rWords)}+{random.choice(rWords)}'
	
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

	time.sleep(22)
	print ('iteration: ',i)     
	
	if i%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			os.system("TASKKILL /F /IM chrome.exe")
			os.system("TASKKILL /F /IM firefox.exe")
			break 
