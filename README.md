

<p align="center">
  <a href="https://pepy.tech/project/babysploit"><img src="https://pepy.tech/badge/babysploit/week"></a>
  <a href="https://pepy.tech/project/babysploit"><img src="https://pepy.tech/badge/babysploit/month"></a>
  <a href="https://pepy.tech/project/babysploit"><img src="https://pepy.tech/badge/babysploit"></a></br>
  <a href="https://github.com/M4cs/BabySploit/network"><img src="https://img.shields.io/github/forks/M4cs/BabySploit.svg" alt="Forks"></a>
  <a href="https://github.com/M4cs/BabySploit/stargazers"><img src="https://img.shields.io/github/stars/M4cs/BabySploit.svg" atl="Stars"></a>
  <a href="https://github.com/M4cs/BabySploit/issues"><img src="https://img.shields.io/github/issues/M4cs/BabySploit.svg" alt="Issues"></a>
  <a href=""><img src="https://img.shields.io/badge/version-1.2-green.svg?syle=popout"></a>
  <a href="https://github.com/M4cs/BabySploit/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/M4cs/BabySploit.svg" alt="License"></a>
  <a href="http://www.python.org/download/"><img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-yellow.svg"></a>
  <a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FM4cs%2FBabySploit"><img src="https://img.shields.io/twitter/url/https/github.com/M4cs/BabySploit.svg?style=popout" alt="Twitter"></a>
  <a href="https://discord.gg/7VN9VZe"><img src="https://img.shields.io/badge/discord-join-blue.svg?syle=popout"></a>

<p align="center">
  <b>Made For Kali Linux. No Support For Other Distros If There Are Problems.</b>
  </br><a href="https://twitter.com/maxbridgland" alt="Twitter Link"><b>Developed by @maxbridgland</b></a></br>
  <a href="https://bit.ly/2Ke9uVi">Donate</a>
</p>
<p align="center">
  <a href="https://discord.gg/7VN9VZe"><img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans/27090541/8dd5c907f2a0eecb73dc6a4776fc9a25878ebcdd.png" alt="Forks"></a>

<p align="center">
  <b>BabySploit is a penetration testing toolkit aimed at making it easy to learn how to use bigger,</br> 
more complicated frameworks like Metasploit. With a very easy to use UI and toolkit, anybody</br>
from any experience level will find use out of BabySploit. Below are some screenshots of the framework.</b>
</p>
<p align="center">
  <a href="https://asciinema.org/a/FKAPSoELbeclWr8TxKClOxWd9" target="_blank"><img src="https://asciinema.org/a/FKAPSoELbeclWr8TxKClOxWd9.svg" /></a></br>
  <b> Video Demonstration </b>
</p>  

# Installation Instructions:

## Using Pip

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install exploitdb netcat nmap perl php7.0 
pip3 install babysploit
babysploit
```

In order to use `search` command you must follow steps [here](https://www.exploit-db.com/searchsploit/#install) to install the searchsploit binary!

## Building From Source
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install exploitdb netcat nmap perl php7.0
git clone https://github.com/M4cs/BabySploit.git
cd BabySploit/
python3 setup.py install
babysploit
```

## Docker Run Command

```
docker run --rm -idt --name babysploit xshuden/babysploit    # container is deleted when you're done
OR
docker run -idt --name babysploit xshuden/babysploit
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
  <img src="https://image.prntscr.com/image/dMlUOjFnQk_KSyru1gTQ2A.png" alt="Tools"/>
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
  - Raccoon
  - Cloudflare Bypasser
  
### Exploitation:
  
  - Searchsploit
  - ReverseShell Wizard
  - FTP Buffer Overflow Scan
  - WPSeku WordPress Vuln Scanner
  
### Post Exploitation:

  - In The Works
  
### Bruteforcing:

  - FTP Bruteforcer
  - WPSeku WordPress Login Bruteforce
  
### Phishing:

  - BlackEye Python
  
### Crypto/Stegano:

  - MetaKiller
  - PDFMeta
  
# Contributing

Feel free to contribute by making plugins or fixing bugs with a Pull Request. All contributions are helpful and will help make this a great tool.

Licensed Under [MIT](https://github.com/M4cs/BabySploit/blob/master/LICENSE.md).

Copyright (c) 2018 Syndicated Intelligence
