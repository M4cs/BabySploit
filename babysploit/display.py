def welcome():
    import socket, requests
    try:
      teddy = requests.get("https://hastebin.com/raw/oyifedagib", timeout=3).text
      print(teddy)
    except requests.exceptions.ReadTimeout:
      pass
    banner = """
              Welcome to BabySploit!
            Developed by @maxbridgland
      Learn Hacking The Easy Way With BabySploit
    """
    hostname = socket.gethostbyname(socket.gethostname())
    print(banner)
    print("        [i] Current Local IP: %s [i]" % hostname)

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
      ['censyslookup', 'censys api lookup | req api creds']
    ]
    table = SingleTable(infotable, "Information Gathering")
    print("")
    print(table.table)
    print("")
    exploittable = [
      ['\nTool', '\nDescription'],
      ['searchsploit', 'search available exploits (use search command)'],
      ['reverseshell', 'reverse shell tool for creating payloads']
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
      ['metakiller', 'grab metadata of an image'],
    ]
    cryptable = SingleTable(cryptotable, "Cryptography/Steganography")
    bftable = SingleTable(bruteforcetable, "Bruteforcing")
    print(cryptable.table)
    print("")
    print(bftable.table)