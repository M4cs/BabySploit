def welcome():
    import socket
    from pyfiglet import Figlet
    f = Figlet(font="slant")
    print(f.renderText(" BabySploit"))
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
      ['tcpdump', 'tcpdump plugin']
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
