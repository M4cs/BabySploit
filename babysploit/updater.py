def checkupdate():
    import requests
    from subprocess import Popen, PIPE
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
            print("Fetching Update..")
            process1.communicate()
            print("Downloading Update..")
            process2.communicate()
            print("Installing Modules.. This may take a minute..")
            process3.communicate()
            Popen(["rm -rf babysploit/__pycache__/"], stdout=PIPE, stderr=PIPE)
