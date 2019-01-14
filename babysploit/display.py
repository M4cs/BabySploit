def welcome():
    import socket
    banner = """
                     BabySploit!
              Developed by @maxbridgland
          https://github.com/M4cs/BabySploit
        """
    gw = socket.gethostname()
    print("          [i] Default Gateway: %s [i]" % gw)
    print(banner)
    print("")

def tools():
    from terminaltables import SingleTable
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText("      Tools"))
    print("Simply enter the name of the tool you want to use to use it.\n")
    infotable = [
      ['\nTool', '\nDescription'],
      ['nmap', 'nmap port scanner tool'],
      ['iplookup', 'ip info tool'],
      ['dnslookup', 'dns lookup tool'],
      ['censyslookup', 'censys api lookup | req api creds'],
      ['raccoon', 'use raccoon scanner tool | command: raccoon --help'],
      ['cfbypass', 'cloudflare bypasser']
    ]
    table = SingleTable(infotable, "Information Gathering")
    print("")
    print(table.table)
    print("")
    exploittable = [
      ['\nTool', '\nDescription'],
      ['searchsploit', 'search available exploits (use search command)'],
      ['reverseshell', 'reverse shell tool for creating payloads'],
      ['ftpvulnscan', 'check for ftp buffer overflow'],
      ['wpseku', 'wordpress vulnerability scanner']
    ]
    exptable = SingleTable(exploittable, "Exploitation")
    print(exptable.table)
    print("")
    phishingtable = [
      ['\nTool', 'Description'],
      ['blackeye', 'BlackEye Phish Kit']
    ]
    phishtable = SingleTable(phishingtable, "Phishing")
    print("")
    print(phishtable.table)
    print("")
    bruteforcetable = [
      ['\nTool', '\nDescription'],
      ['ftpbruteforce', 'ftp brute force tool']
    ]
    cryptotable = [
      ['\nTool', '\nDescription'],
      ['pdfmeta', 'pdf meta data']
    ]
    cryptable = SingleTable(cryptotable, "Cryptography/Steganography")
    bftable = SingleTable(bruteforcetable, "Bruteforcing")
    print(cryptable.table)
    print("")
    print(bftable.table)
