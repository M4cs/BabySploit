def checkupdate():
    import requests, os, subprocess
    from tqdm import tqdm, trange
    with open("babysploit/version", "r") as fwv:
        data = fwv.read().replace(" ", "")
    cv = requests.get("https://raw.githubusercontent.com/M4cs/BabySploit/master/babysploit/version").text.replace(" ", "")
    if data == cv:
        pass
    elif data != cv:
        print("[!] Update Found | Version: %s [!]" % cv)
        ask = str(input("[y\\n] ").lower())
        if ask == "y":
            for i in tqdm(range(int(100)), desc="Updating"):
                subprocess.check_output("git fetch --all", shell=True)
                subprocess.check_output("git reset --hard origin/master", shell=True)
                subprocess.check_output("pip3 install -r requirements.txt", shell=True)
