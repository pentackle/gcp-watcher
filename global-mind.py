#------imports--------
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uo
import re
import time
#---------------------

#set 30 second time to check website for updates and get colour
def timely_execution():
    while True:
        get_colour()
        time.sleep(30)

#determine colour from value
def get_colour():
    percent=float(get_value())
    if percent>.95:
        print('dark blue')
    elif .95 >=percent>=.90:
        print('cyan')
    elif .90>percent>=.40:
        print('green')
    elif .40>percent>=.10:
        print('yellow')
    elif .10>percent>.05:
        print("orange")        
    else:
        print('red')

#get value from website
def get_value():
    html = uo('http://global-mind.org/gcpdot/gcpindex.php')
    res = bs(html.read(),"html5lib");
    return((re.findall('">(.*?)</s><s t=',str(res.body)))[0])

if __name__ == '__main__':
    timely_execution()


