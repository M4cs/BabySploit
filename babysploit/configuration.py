from configparser import ConfigParser
import platform, os, sys
config = ConfigParser()

def firstTimeSetup(plat):
    try:
        if plat == "Linux":
            home = os.path.expanduser("~")
            configpath = home + 'BabySploit/configuration/'
            os.mkdir(configpath)
        elif plat == "Darwin":
            home = os.path.expanduser("~")
            configpath = home + 'BabySploit/configuration/'
            os.mkdir(configpath)
        elif plat == "Windows":
            home = os.path.expanduser("~")
            configpath = home + "/BabySploit/configuration/"
            os.mkdir(configpath)
            createuser(configpath)
    except:
        print('Error: Unable to setup configuration path! Try running this in sudo for the first time setup.')
        exit()
        
def createuser(configpath):
    system = platform.system()
    release = platform.release()
    config['DEFAULT'] = {
        'lhost': '0.0.0.0',
        'lport': '8080',
        'rhost': 'google.com',
        'rport': '80',
        'platform': '',
        'usernamelist': '/usr/bin/share/wordlists',
        'passwordlist': '/usr/bin/share/wordlists',
        'urlpath': '/connect'
    }
    config['DEFAULT']['platform'] = "%s %s" % (system, release)
    if platform.system() == "Linux":
        with open(configpath, "w") as configfile:
            config.write(configfile)
    elif platform.system() == "MacOS":
        with open(configpath, "w") as configfile:
            config.write(configfile)
    elif platform.system() == "Windows":
        with open(configpath, "w") as configfile:
            config.write(configfile)

def checkuser():
    if platform.system() == "Linux":
        home = os.path.expanduser("~")
        configpath = home + "/BabySploit/configuration"
        if os.path.exists(configpath) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")
    elif platform.system() == "Darwin":
        home = os.path.expanduser("~")
        configpath = home + "/BabySploit/configuration"
        if os.path.exists(configpath) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")
    elif platform.system() == "Windows":
        home = os.path.expanduser("~")
        configpath = home + "/BabySploit/configuration"
        if os.path.exists(configpath) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")

