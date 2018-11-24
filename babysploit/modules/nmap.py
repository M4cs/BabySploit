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

    arg_map = {
        1:  "-sS",
        2:  "-sT",
        3:  "-sU",
        4:  "-sY",
        5:  "-sN",
        6:  "-sF",
        7:  "-sX",
        8:  "-sA",
        9:  "-sW",
        10:  "-sM",
        11:  "-sZ",
        12:  "-sO",
        13:  "-sP",
        14:  "-sI",
        15:  "-sV",
        16:  "-sR",
        17:  "-sL"
    }

    while True:
        terminal = input("> ")

        # Get all starting integers in the input
        # "223ss4" -> "223" 
        argstr = ""
        for c in terminal:
            if c.isnumeric():
                argstr += c
            else:
                break

        try:
            arugument = int(argstr)
        except TypeError as e:
            print("%s is not a number, sorry." % terminal)
            continue

        if arugument == 18:
            custom_args = input("Enter Arguments (format: nmap <arguments> %s): " % hosts)
            os.system("nmap %s %s > babysploit/logs/nmap_scan_%s.log" % (custom_args, hosts, now))
            exit()
        elif arugument in arg_map:
            os.system("nmap %s %s > babysploit/logs/nmap_scan_%s.log" % (arg_map[arugument], hosts, now))
            exit()
        else:
            print("%s not a choice sorry.")
