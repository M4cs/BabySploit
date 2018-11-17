#!/usr/bin/env python3
# Import Modules #
from configparser import ConfigParser
from babysploit import display, configuration, dnslookup, helper, iplookup, ftpv, nmap, reverseshell, searchsploit, censyslookup, blackeye, metakiller, ftpbruteforce, updater, pdfmeta
from pyfiglet import Figlet
import os, subprocess

try:
    # Clear Terminal #
    os.system("clear")
    # Display Welcome Message #
    display.welcome()
    # Check For Configuration File/Create New Configuration File #
    configuration.checkuser()
    updater.checkupdate()
    # Display Help Menu #
    banner = """    BabySploit is a framework aimed at helping aspiring
 penetration testers learn how to use the most common and
  useful tools in the field. Below is a table displaying 
      what commands are available and what they do.    
    """
    print(banner)
    helper.run()
    # Load Config #
    config = ConfigParser()
    config.read("babysploit/config/config.cfg")
    # Create Terminal/Input #
    def term():
        terminal = input("\n[babysploit]> ") # Define the name of the terminal
        if terminal[0:4] == "help": # From Char Space 0 - 4 if it = help run the help command.
            f = Figlet(font='slant')
            print(f.renderText("       Help"))
            helper.run()
            term()
        elif terminal[0:1] == "?": # Same as above
            f = Figlet(font='slant')
            print(f.renderText("       Help"))
            helper.run()
            term()
        elif terminal[0:4] == "info": # Same as above but for info command
            for key, value in config.items('DEFAULT'):
                print("%s: %s" % (key, value))
            term()
        elif terminal[0:5] == "tools": # Same as above but for tool command
            display.tools()
            term()
        elif terminal[0:6] == "search":
            searchsploit.search()
            term()
        elif terminal[0:3] == "set": # Set Config Key
            if terminal[4:] == terminal[4:]: # Take Input After `set ` 
                config['DEFAULT'][terminal[4:]] = input("Enter Value For %s: " % terminal[4:]) # Get Value for that key name
                with open("babysploit/config/config.cfg", "w") as configfile:
                    config.write(configfile) # Write the new config key
                print("Config Key Saved!")
                term()
        elif terminal[0:5] == "reset": # Reset configuration
            config['DEFAULT'] = {
                'lhost': '0.0.0.0',
                'lport': '8080',
                'rhost': 'google.com',
                'rport': '80',
                'platform': '',
                'usernamelist': 'lists/usernames',
                'passwordlist': 'lists/passwords',
                'urlpath': '/connect'
            }
            with open("babysploit/config/config.cfg", "w") as configfile:
                config.write(configfile)
            term()
        elif terminal[0:4] == "exit":
            print("Exiting...")
            exit()
        elif terminal[0:7] == "raccoon":
            if terminal[8:] == terminal[8:]:
                query = terminal[8:]
                os.system("raccoon %s" % query)
            else:
                print("Please use raccoon --help for arguments.")
            term()
        elif terminal[0:8] == "iplookup":
            iplookup.run()
            term()
        elif terminal[0:7] == "pdfmeta":
            pdfmeta.start()
            term()
        elif terminal[0:4] == "nmap":
            nmap.run()
            term()
        elif terminal[0:12] == "reverseshell":
            reverseshell.run()
            term()
        elif terminal[0:12] == "censyslookup":
            print("Broken Coming Soon")
            term()
        elif terminal[0:9] == "dnslookup":
            dnslookup.start()
            term()
        elif terminal[0:8] == "blackeye":
            blackeye.run()
            term()
        elif terminal[0:11] == "ftpvulnscan":
            ftpv.checkVulnerability()
            term()
        elif terminal[0:10] == "metakiller":
            metakiller.run()
            term()
        elif terminal[0:13] == "ftpbruteforce":
            ftpbruteforce.start()
        elif terminal[0:6] == "update":
            print("Would you like to check for updates?")
            ans = str(input("[y\\n] ").lower())
            if ans == "y":
                print("Checking for Updates...")
                state, data, cv = updater.checkupdate()
                print("Current Version: %s" % data)
                if state == "uptodate":
                    print("You are all up to date on version: %s" % data)
                else:
                    print("Found New Version: %s\nWould you like to update?" % cv)
                    ans2 = input("[y\\n] ").lower()
                    if ans2 == "y":
                        updater.checkupdate()
                    else:
                        print("Cancelling..")
                        pass
            term()


        else:
            print("Unknown Command")
            term()

    term()
except KeyboardInterrupt:
    print("Exiting...")
    exit()
