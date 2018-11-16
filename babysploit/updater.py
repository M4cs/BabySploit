def checkupdate():
    import requests
    with open("babysploit/version", "r") as fwv:
        data = fwv.read().replace(" ", "")
    cv = requests.get("https://raw.githubusercontent.com/M4cs/BabySploit/master/babysploit/version").text.replace(" ", "")
    if data == cv:
        state = "uptodate"
    elif data != cv:
        state = "outofdate"
    return state, data, cv

def update():
    import os, subprocess
    ans = os.path.exists(".git")
    if ans == True:
        print("Starting Update...")
        pass
    elif ans == False:
        print("[!] Error Updating. You Did Not Clone The Repository. [!]")
        exit()
    print("Fetching New Version...")
    subprocess.check_output("git fetch --all", shell=True)
    print("Updating...")
    subprocess.check_output("git reset --hard origin/master", shell=True)
    subprocess.check_output("pip3 install -r requirements.txt", shell=True)
    print("Exiting Updater...")
    exit()
