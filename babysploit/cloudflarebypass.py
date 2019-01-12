def run():
    import os
    from configparser import ConfigParser
    from socket import gethostbyname, error
    config = ConfigParser()
    path = str(os.path.expanduser('~')) + "/config.cfg"
    config.read(path)
    rhost = config['DEFAULT']['rhost']
    print("\n[!] Confirm Target: [!]")
    print("Target: %s" % rhost)
    print("Is This Correct?")
    ans = str(input("[y\\n] ").lower())
    if ans == "y":
        rhost = rhost
    else:
        print("[?] Enter Target: [?]")
        rhost = str(input("> "))
    subdoms = ['mail', 'webmail', 'ftp', 'direct', 'cpanel', 'admin', 'support', 'secure', 'wiki', 'mx1', 'mail', 'dns', 'dns2', 'ns', 'cp', 'plesk', 'panel', 'help',
                'beta', 'payment', 'backup', 'forum', 'host', 'www', 'www3', 'video', 'portal', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'perfect', 'test', 'sftp', 'api', 'ip',
                'zen', 'zenpanel', 'repo']
    site = rhost.replace("https://", "")
    site.replace("/", "")
    try:
        ip = gethostbyname(site)
    except error:
        pass
    print("\nRunning Scan...")
    for sub in subdoms:
        doo = sub + "." + site
        try:
            ddd = gethostbyname(doo)
            if ddd != ip:
                print("[!] IP Found: %s | %s" % (ddd, doo))
                break
        except error:
            pass
    print("Scan Complete\n")
