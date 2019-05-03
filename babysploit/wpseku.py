import os

from configparser import ConfigParser


def run():
    global rhost
    config = ConfigParser()
    path = str(os.path.expanduser('~')) + "/config.cfg"
    config.read(path)
    print("== Current Configuration: ==")
    print("Target: %s" % config['DEFAULT']['rhost'])
    print("[?] Is this configuration correct? [?]")
    ask = str(input("[y\\n] ").lower())
    if ask == "y":
        rhost = config['DEFAULT']['rhost']
    else:
        print("[?] Enter Target: [?]")
        rhost = str(input("> "))
    choose()


def choose():
    print("[?] What type of scan would you like to perform: [?]")
    ask = str(input("[bruteforce login | generic scan | wp plugin] ").lower())
    if ask[0:16] == "bruteforce login":
        bruteforce()
    elif ask[0:12] == "generic scan":
        generic()
    elif ask[0:9] == "wp plugin":
        pluginscan()
    else:
        print("\n[!] Error: Unknown Scan Type! [!]")
        choose()


def pluginscan():
    print("[!] Confirm Settings [!]")
    print("[i] Target: %s [i]" % rhost)
    input("Press ENTER To Start Scan")
    os.system("wget %s -O tmp/temp.php" % rhost)
    os.system("python3 wpseku/wpseku.py --scan tmp/temp.php --verbose")
    os.system("rm tmp/temp.php")


def bruteforce():
    config = ConfigParser()
    path = str(os.path.expanduser('~')) + "/config.cfg"
    config.read(path)
    print("[?] Would you like to use the directory in your config for the "
          "wordlist or a custom filepath? [?]")
    print("[i] Current Config: %s [i]" % config['DEFAULT']['passwordlist'])
    ask = str(input("[config | custom] ").lower())
    if ask == "config":
        print("[i] Reading Config File.. [i]")
        wordlist = str(config['default']['passwordlist'])
    else:
        print("[?] Enter Custom Filepath: [?]")
        wordlist = str(input("> "))
        if os.path.exists(wordlist) == True:
            pass
        else:
            print("[!] Error: %s is not a file! [!]" % wordlist)
            bruteforce()
    print("[?] Enter Username to attempt bruteforce on: [?]")
    username = str(input("> "))
    print("[!] Confirm Settings [!]")
    print("Target: %s" % rhost)
    print("Filepath: %s" % wordlist)
    print("Username: %s" % username)
    print("Scan Type: Brute Force")
    input("Press ENTER To Confirm")
    os.system("python3 wpseku/wpseku.py --url %s --brute --user %s --wordlist %s --verbose" %
              (rhost, username, wordlist))


def generic():
    print("[!] Confirm Settings [!]")
    print("Target: %s" % rhost)
    print("Scan Type: Generic")
    input("Press ENTER To Confirm")
    os.system("python3 wpseku/wpseku.py --url %s --verbose" % rhost)
