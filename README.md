

# **The P.A.V.E.L Project**

P.A.V.E.L is a versatile, and helpful open source web testing framework. It provides lot of functions to be the best complement of a web porxy. The aim of this tool is to make everithing in one console, and also be compatible with third party tools

## **Functionality**


### Improve fuzzing
One of the main functions of this framework is to improve fuzzing tools through parsonalized wordlists; "if Muhammad doesn't go to the mountain, the mountain goes to Muhammad". With this method, every tool is perfect for fuzzing. A common example is when you want to use a fast tool, but it has no special modes and options; Now, this options can be combined with your wordlist, and exported as a file ready to fuzz.
Some examples include, burp intruder modes, encode and hashing, generating numbers and much more

### Requests
Another important part in the objective of P.A.V.E.L is to make different requests easy. Yo can make quickly HEAD or OPTIONS requests, see the output and save it in a file. Moreover, it is possible to use wappalyzer to detect tecnologies, all with this console.

### Loading to the proxy
My favorite part is this one. Did you ever where using dirb or gobuster for discovering content and you thought if there was a way for passing the output to your proxy? well, now there is one. Load every file to your proxy in seconds with P.A.V.E.L!

### Port Listening
You can set a listener in background for those situation where you need to test command injection or steal a cookie with XSS. This feature listen quietly to a port and, when something is recived, the output is printed at real time

## **Installation**
* git clone https://github.com/EddyNefa/P.A.V.E.L_Project.git

* cd P.A.V.E.L_Project

* python3 -m pip -r requirements.txt

* sudo python3 setup.py

* pavel

It is very important to run the setup with root permissions. You can use pavel in every directory because it is in the path by default
