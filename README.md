# noctule
Noctule is a penetration testing tool designed to scan a target url for a selected vulnerability from a list of common vulnerabilities. These vulnerabilities include **SQL Injection, Cross-Site Scripting, Local File Inclusion, Remote File Inclusion,** and **Remote Code Execution** (in development).
## Getting Started
Noctule is not particurally difficult to install, but here's some basic information about the setup process.
### Prerequisites
This is a list of things you need to get before you can use Noctule. I'll update it when (if) there's any more, but there won't be.
```
Python 3.x
```
### Installing
Installing is as easy as clicking the green button that says `Clone or download` and then `Open in Desktop` or `Download Zip`.  
If you want you can use git to clone it using this command, but if you're reading this you probably don't have it installed.
```
git clone https://githib.com/dxeheh/noctule
```
## Using Noctule
Noctule is run from the command line. `python noctule.py [arguments]`.  
Below is the help menu.  
```
usage: noctule.py [-h] [-m METHOD] [-u URL] [-p PARAMETER] [-d DATA]

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        get or post
  -u URL, --url URL     url to target
  -p PARAMETER, --parameter PARAMETER
                        parameter to use
  -d DATA, --data DATA  data to use for the post module
  ```
Running Noctule will prompt you to choose the attack vector you wish to use.
```
                         __        __            ____       ____
       ____  ____  _____/ /___  __/ /__          )   \     /   (
      / __ \/ __ \/ ___/ __/ / / / / _ \          )_  \_V_/  _(
     / / / / /_/ / /__/ /_/ /_/ / /  __/            )__   __(
    /_/ /_/\____/\___/\__/\__,_/_/\___/                `-'


        1. SQLi
        2. XSS
        3. LFI
        4. RFI
        5. RCE
```
In this example, LFI is the selected attack vector. Noctule runs through a list of common files and attempts to open them from the server. At the end, it gives an overall result.
```
Trying: C:\boot.ini
Not found.

Trying: C:\WINDOWS\win.ini
File detected.


... many lines ommitted...


Trying: C:\php4\sessions\
Not found.


Overall: Vulnerable
```
This indicates that the webpage is very likely vulnerable to Local File Inclusion.
## Authors
* **dxeheh** - Literally everything
## Acknowledgments
* **jojo3NNN** - Praise Dice! for helping with issues.
* **Hitman142** - Feedback and focus group member.
