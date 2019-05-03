import os
import subprocess
import json

from pyfiglet import Figlet
from babysploit.utils import get_terminal_width


def platform_check():
    if not os.path.exists("/usr/share/exploitdb"):
        print("[!] Couldn't find exploit database. Try running install.py again. [!]")
        return

    f = Figlet(font='slant')
    print(f.renderText("     Search"))
    supported_platforms = ['windows', 'linux', 'macos', 'php']
    message = "Platform [{}, all]: ".format(",".join(supported_platforms))
    q1 = input(message).lower()
    if q1 == 'all':
        return ""
    elif q1 in supported_platforms:
        return q1
    else:
        print("[!] Unknown platform '{}'. Use 'all'".format(q1))
        return ""


def do_search():
    platform = platform_check()
    search = platform + " " + input("Search: ")
    print("Running Search..")
    q = subprocess.check_output("searchsploit -j {}".format(search), shell=True)
    resp = json.loads(q)

    term_width = get_terminal_width()
    print("=" * 46 + " Result " + "=" * 46)
    hl = '-' * term_width

    for exploit in resp['RESULTS_EXPLOIT']:
        print(hl)
        message = ("Title: {Title}"
                   "Platform: {Platform}"
                   "Path: {Path}"
                   "Author: {Author}").format(**exploit)
        print(message)
    print("=" * term_width)
