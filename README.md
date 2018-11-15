<p align="center">
  <img src="https://i.imgur.com/cf2h0Vn.png" alt="BabySploit"/></br>
</p>

# BabySploit
[![GitHub forks](https://img.shields.io/github/forks/M4cs/BabySploit.svg)](https://github.com/M4cs/BabySploit/network)
[![GitHub stars](https://img.shields.io/github/stars/M4cs/BabySploit.svg)](https://github.com/M4cs/BabySploit/stargazers)
[![GitHub license](https://img.shields.io/github/license/M4cs/BabySploit.svg)](https://github.com/M4cs/BabySploit/blob/master/LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues/M4cs/BabySploit.svg)](https://github.com/M4cs/BabySploit/issues)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/M4cs/BabySploit.svg?style=popout)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FM4cs%2FBabySploit)
[![Discord](https://img.shields.io/badge/discord-join-blue.svg?syle=popout)](https://discord.gg/7VN9VZe)

Tested on Kali Linux. Should work with all Debian based distros (and other ones if you have the right packages installed)

Join the Discord For Support: https://discord.gg/7VN9VZe

BabySploit is a penetration testing framework aimed at making it easy to learn how to use bigger, 
more complicated frameworks like Metasploit. With a very easy to use UI and toolkit, anybody
from any experience level will find use out of BabySploit. Below are some screenshots of the framework.
<p align="center">
  <img src="https://image.prntscr.com/image/l35Yo-q5SHKBSWvOLb_mig.png" alt="Welcome"/></br>
</p>

# Changelog (from 0.0.6):

#### 0.0.6 Update:
  - Fix updater script
  - Remove tcpdump
  - Add ftpvulnscan and pdfmeta
  
# Installation Instructions:

BabySploit is best run out of the home directory so to clone it there run:
```
git clone git://github.com/M4cs/BabySploit ~/BabySploit
```

After cloning the installation you must install some pre-requisites. **If you are on Kali you should already have all of these installed but it doesn't hurt to do so anyways just in case**. Do so by running the following:
```
*from within the babysploit directory*
sudo apt-get update
sudo apt-get install exploitdb netcat nmap php7.0 perl -y
wget http://owl.phy.queensu.ca/~phil/exiftool/Image-ExifTool-11.17.tar.gz
tar xf Image-ExifTool-11.17.tar.gz
cd Image-ExifTool-11.17
perl MakeFile
make test
sudo make install
cd ..
sudo rm -rf Image-ExifTool-11.17
```

After installing these binaries you must install required Python 3 modules. To do so run the following:
```
*from within the BabySploit Directory*
pip3 install -r requirements.txt --user
```

# Getting Started:

#### Setting Configuration Values:

BabySploit uses ConfigParser in order to write and read configuration. Your config file is automatically
generated and located at `./babysploit/config/config.cfg`. You can manually change configuration settings
by opening up the file and editing with a text editor or you can use the set command to set a new value for
a key. Use the set command like so:
```
set rhost
>> Enter Value For rhost: 10
>> Config Key Saved!
```

If before running this command the rhost key had a value of 80, the rhost key after running this command has a
value of 10. You can also add configuration variables to the config by using the set command with a new key after it
like so:
```
set newkey
>> Enter Value For newkey: hello
>> Config Key Saved!
```

Before running this there was no key named "newkey". After running this you will have a key named "newkey" in your config
until you use the `reset` command which resets the saved configuration.

#### Running A Tool

In order to run a tool all you have to do is enter the name of the tool into BabySploit. You can use the `tools` command
to display a menu with all the currently availble tools. If we run tools we get the depiction:
<p align="center">
  <img src="https://image.prntscr.com/image/S-BrY0paRcGoliP1NPg5fA.png" alt="Tools"/>
</p>
*this depiction may be outdated*

This menu will display the tools available and the description of each tool. To run a tool simply enter the tool name
into BabySploit. Ex: `ftpbruteforce` - runs the ftpbruteforce tool.

# Features (Current, In The Works, Planned):

[Visit](https://github.com/M4cs/BabySploit/projects/1) project board for tools.

  - Information Gathering
  - Exploitation
  - Post Exploitation
  - Bruteforcing
  - Phishing
  - Cryptography/Stenography
 
### Information Gathering:

  - Nmap
  - IP Info
  - Tcpdump (In The Works)
  - Datasploit (In The Works)
  - Censys Lookup
  - DNS Lookup
  
### Exploitation:
  
  - Searchsploit
  - ReverseShell Wizard

### Post Exploitation:

  - In The Works
  
### Bruteforcing:

  - FTP Bruteforcer
  
### Phishing:

  - BlackEye Python
  
### Crypto/Stegano:

  - MetaKiller
  
# Contributing

Feel free to contribute by making plugins or fixing bugs with a Pull Request. All contributions are helpful and will help make this a great tool.

Licensed Under [MIT](https://github.com/M4cs/BabySploit/blob/master/LICENSE.md).

Copyright (c) 2018 Syndicated Intelligence
