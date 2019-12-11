from configparser import ConfigParser
import platform, os, sys
config = ConfigParser()

def firstTimeSetup(plat):
    try:
        if plat == "Linux":
            home = os.path.expanduser("~")
            configpath = home + '/.babysploit'
            os.system('mkdir ' + configpath)
            os.system('mkdir ' + configpath + '/configuration')
        elif plat == "Darwin":
            home = os.path.expanduser("~")
            configpath = home + '/.babysploit/configuration'
            os.system('mkdir -p ' + configpath)
        elif plat == "Windows":
            home = os.path.expanduser("~")
            configpath = home + "/.babysploit/configuration"
            os.makedirs(configpath)
            createuser(configpath)
    except Exception as e:
        print('Error: Unable to setup configuration path! Try running this in sudo for the first time setup.')
        print(e)
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
        with open(configpath + '/config.cfg', "w") as configfile:
            config.write(configfile)
    elif platform.system() == "MacOS":
        with open(configpath + '/config.cfg', "w") as configfile:
            config.write(configfile)
    elif platform.system() == "Windows":
        with open(configpath + '/config.cfg', "w") as configfile:
            config.write(configfile)

def checkuser():
    if platform.system() == "Linux":
        home = os.path.expanduser("~")
        configpath = home + "/.babysploit/configuration"
        if os.path.exists(configpath) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")
    elif platform.system() == "Darwin":
        home = os.path.expanduser("~")
        configpath = home + "/.babysploit/configuration"
        if os.path.exists(str(configpath)) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")
    elif platform.system() == "Windows":
        home = os.path.expanduser("~")
        configpath = home + "/.babysploit/configuration"
        if os.path.exists(str(configpath)) == True:
            print("            [i] Loaded Configuration... [i]\n\n")
        else:
            firstTimeSetup(platform.system())
            print("       [i] Created New Configuration File... [i]")

