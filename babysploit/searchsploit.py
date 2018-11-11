import subprocess
import os
import json
def platformcheck():
    if os.path.exists("/usr/share/exploitdb") == True:
            q1 = input("Platform [Windows, Linux, MacOS, PHP, All]: ").lower()
            if q1 == "windows":
                platform = "windows"
            elif q1 == "linux":
                platform = "linux"
            elif q1 == "macos":
                platform = "macos"
            elif q1 == "all":
                platform = ""
            elif q1 == "php":
                platform = "php"
            return platform
    else:
        print("[!] Couldn't find explpoit database. Try running install.py again. [!]")

def search():
    platform = platformcheck()
    search = platform + " " + input("Search: ")
    print("Running Search..")
    q = subprocess.check_output("searchsploit -j %s" % search, shell=True)
    resp = json.loads(q)
    print("=" * 46 + " Result " + "=" * 46)
    for exploit in resp['RESULTS_EXPLOIT']:
        print('-' * 100)
        print("Title: %s" % exploit['Title'])
        print("Platform: %s" % exploit['Platform'])
        print("Path: %s" % exploit['Path'])
        print("Author: %s" % exploit['Author'])
    print("=" * 100)