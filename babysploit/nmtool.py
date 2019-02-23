def run():
    import os, datetime

    now = datetime.datetime.now()
    hosts = input("Host/Host Range: ")
    print("""
SneakyBoy NMap Module

Choose A Type of Scan From Below (Default -sV):

[1] -sS | TCP SYN Scan           [2] -sT | TCP Connect Scan

[3] -sU | UDP Scan               [4] -sY | SCTP INIT Scan

[5] -sN | TCP Null Scan          [6] -sF | TCP FIN Scan

[7] -sX | TCP Xmas Scan          [8] -sA | TCP ACK Scan

[9] -sW | TCP Window Scan        [10] -sM | TCP Maimon Scan

[11] -sZ | SCTP Cookie Echo Scan [12] -sO | IP Protocol Scan

[13] -sP | Ping Scan             [14] -sI | Idle Scan

[15] -sV | Version Detection     [16] -sR | RPC Scan

[17] -sL | List Scan             [18] Custom Argument Scan

For More Info On Scan Types Visit:

https://nmap.org/bennieston-tutorial/
and
https://nmap.org/book/man-port-scanning-techniques.html

        """)
    while True:
        terminal = input("> ")
        if terminal[0:2] == "10":
            arg = "-sM"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "11":
            arg = "-sZ"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "12":
            arg = "-sO"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "13":
            arg = "-sP"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "14":
            arg = "-sI"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "15":
            arg = "-sV"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "16":
            arg = "-sR"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "17":
            arg = "-sL"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:2] == "18":
            arg = input("Enter Arguments (format: nmap <arguments> %s): " % hosts)
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "1":
            arg = "-sS"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "2":
            arg = "-sT"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "3":
            arg = "-sU"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "4":
            arg = "-sY"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "5":
            arg = "-sN"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "6":
            arg = "-sF"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "7":
            arg = "-sX"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "8":
            arg = "-sA"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        elif terminal[0:1] == "9":
            arg = "-sW"
            os.system("nmap %s %s > logs/nmap_scan_%s.log" % (arg, hosts, now))
            exit()
        else:
            print("That's not a choice sorry.")
