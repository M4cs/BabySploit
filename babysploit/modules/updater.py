def Command_exe(msg, cmd):
    i = "[STATUS] Processing"
    stdout.write("" + msg + " %s" % i)
    stdout.flush()
    if subprocess.call(cmd + ' >/dev/null 2>&1', shell=True) == 0:
        i = "Complete [WARNING] "
    else:
        i = "Error [WARNING] "
    stdout.write("\r" + msg + "[STATUS] %s" % i)

def checkupdate():
    import requests
    from subprocess import Popen, PIPE
    from configparser import ConfigParser
    with open("babysploit/version", "r") as fwv:
        data = fwv.read().replace(" ", "")
    cv = requests.get("https://raw.githubusercontent.com/M4cs/BabySploit/master/babysploit/version").text.replace(" ", "")
    if data == cv:
        pass
    elif data != cv:
        print("[!] Update Found | Version: %s [!]" % cv)
        ask = str(input("[y\\n] ").lower())
        if ask == "y":
            process1 = Popen(["git", "fetch", "--all"], stdout=PIPE, stderr=PIPE)
            process2 = Popen(["git", "reset", "--hard", "origin/master"], stdout=PIPE, stderr=PIPE)
            process3 = Popen(["pip3", "install", "-r", "requirements.txt"], stdout=PIPE, stderr=PIPE)
            print(Command_exe("["+time.strftime('%H:%M:%S')+"] Fetching Update...             ",'git fetch --all'))
            print(Command_exe("["+time.strftime('%H:%M:%S')+"] Updating BabySploit...         ",'git reset --hard origin/master'))
            print(Command_exe("["+time.strftime('%H:%M:%S')+"] Updating Required Modules...   ",'pip3 install -r requirements.txt'))
            print(Command_exe("["+time.strftime('%H:%M:%S')+"] Removing Cache...                ",'apt-get update'))
            f = open("babysploit/version", "w")
            f.write(cv)
            f.close()

