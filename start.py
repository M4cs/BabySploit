#!/usr/bin/env python3
# Import Modules #
from configparser import ConfigParser
from babysploit import configuration
from babysploit import display
from babysploit import helper
from babysploit import searchsploit
from babysploit import iplookup
from babysploit import nmap
from babysploit import reverseshell
import os

try:
    # Clear Terminal #
    os.system("clear")
    # Display Welcome Message #
    display.welcome()
    # Check For Configuration File/Create New Configuration File #
    configuration.checkuser()
    # Display Help Menu #
    helper.run()
    # Load Config #
    config = ConfigParser()
    config.read("babysploit/config/config.cfg")
    # Create Terminal/Input #
    def term():
        terminal = input("\n[babysploit]> ") # Define the name of the terminal
        if terminal[0:4] == "help": # From Char Space 0 - 4 if it = help run the help command.
            helper.run()
            term()
        elif terminal[0:1] == "?": # Same as above
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
        elif terminal[0:8] == "iplookup":
            iplookup.run()
            term()
        elif terminal[0:4] == "nmap":
            nmap.run()
        elif terminal[0:12] == "reverseshell":
            reverseshell.run()  
        else:
            print("Unknown Command")
            term()

    term()
except KeyboardInterrupt:
    print("Exiting...")
    exit()