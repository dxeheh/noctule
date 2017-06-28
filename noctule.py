import argparse, urllib

sqli = ["'"]
xss = []

def get():
    i = input("\n1. SQLi\n2. XSS\n3. LFI\n4. RFI\n5. RCE\n")
    if i=="1":atk = sqli
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

print('''
                     __        __   	 ____       ____
   ____  ____  _____/ /___  __/ /__ 	 )   \     /   (
  / __ \/ __ \/ ___/ __/ / / / / _ \	  )_  \_V_/  _(
 / / / / /_/ / /__/ /_/ /_/ / /  __/	    )__   __(
/_/ /_/\____/\___/\__/\__,_/_/\___/	       `-'
''')

if args.method.lower() == 'get':
    get()
elif args.method.lower() == 'post'
