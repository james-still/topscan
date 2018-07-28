# topscan - created by james still

from pyfiglet import figlet_format
from bs4 import BeautifulSoup
import os
import re
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print(figlet_format('topscan', font='larry3d'))

# url we need to scrape
url = input("\n\nflavorwire url: ")
clear()

# amount of items in the list
items = re.sub("\D", "", url)
items = items[6:]
items = int(items) + 2

# complex freaking loop
for i in range(2, items):
    html = BeautifulSoup(urllib2.urlopen(url + "/" + str(i)), 'html.parser')
    print(html.find('strong').get_text())
    i += 1

print("\n\nenjoy your results :)")
