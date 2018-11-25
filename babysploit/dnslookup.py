import requests, json

def A_Records():
    try:
        r = requests.get(api + "A/" + domain)
        if r.status_code == 200:
            resp = r.text
            obj = json.loads(resp)
            ttl = obj[0]['ttl']
            ip = obj[0]['value']
            ttl2 = obj[1]['ttl']
            ip2 = obj[1]['value']
            print("First A Record: " + ip + " | TTL: " + ttl)
            print("Second A Record: " + ip2 + " | TTL " + ttl2)
            print("\nChecking For MX Records")
            print("-------------------------\n")
            MX_Records()
        else:
            print("[!] Failed To Connect or You Have Reached The 200 Request Quota! Max 200/HR [!]")
            MX_Records()
    except IndexError:
        print("\n[!] Failed To Find A Records [!]")
        print("\nChecking For MX Records")
        print("-------------------------\n")
        pass
        MX_Records()
    except KeyError:
        print("\n[!] Failed To Find A Records [!]")
        print("\nChecking For MX Records")
        print("-------------------------\n")
        pass
        MX_Records()

def MX_Records():
    try:
        rmx = requests.get(api + "MX/" + domain)
        if rmx.status_code == 200:
            respmx = rmx.text
            objmx = json.loads(respmx)
            value = objmx[0]['value']
            value2 = objmx[1]['value']
            ttlmx = objmx[0]['ttl']
            ttlmx2 = objmx[1]['ttl']
            print("First MX Record: " + value.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx)
            print("Second MX Record: " + value2.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx2)
            print("\nChecking For AAAA Records")
            print("-------------------------\n")
            AAAA_Records()
        else:
            print("[!] Failed To Connect or You Have Reached The 200 Request Quota! Max 200/HR [!]")
            AAAA_Records()
    except IndexError:
        print("\n[!] Failed To Find MX Records [!]")
        print("\nChecking For AAAA Records")
        print("-------------------------\n")
        pass
        AAAA_Records()
    except KeyError:
        print("\n[!] Failed To Find MX Records [!]")
        print("\nChecking For AAAA Records")
        print("-------------------------\n")
        pass
        AAAA_Records()

def AAAA_Records():
    try:
        r4a = requests.get(api + "AAAA/" + domain)
        if r4a.status_code == 200:
            resp4a = r4a.text
            respa = json.loads(resp4a)
            ttl4a = respa[0]['ttl']
            ttl4a2 = respa[1]['ttl']
            value4a = respa[0]['value']
            value4a2 = respa[1]['value']
            print("First AAAA Record: " + value4a + " | TTL: " + ttl4a)
            print("Second AAAA Record: " + value4a2 + " | TTL: " + ttl4a2)
            print("\nChecking For TXT Records")
            print("-------------------------\n")
            TXT_Records()
        else:
            print("[!] Failed To Connect or You Have Reached The 200 Request Quota! Max 200/HR [!]")
            TXT_Records()
    except IndexError:
        print("\n[!] Failed To Find A Records [!]")
        print("\nChecking For TXT Records")
        print("-------------------------\n")
        pass
        TXT_Records()
    except KeyError:
        print("\n[!] Failed To Find AAAA Records [!]")
        print("\nChecking For TXT Records")
        print("-------------------------\n")
        pass
        TXT_Records()

def TXT_Records():
    try:
        rtxt = requests.get(api + "TXT/" + domain)
        if rtxt.status_code == 200:
            resptxt = rtxt.text
            objtxt = json.loads(resptxt)
            valuetxt = objtxt[0]['value']
            valuetxt2 = objtxt[1]['value']
            ttltxt = objtxt[0]['ttl']
            ttltxt2 = objtxt[1]['ttl']
            print("First TXT Record: " + valuetxt + " | TTL: " + ttltxt)
            print("Second TXT Record: " + valuetxt2 + " | TTL: " + ttltxt2)
            print("\nDNS Lookup Complete!")
        else:
            print("[!] Failed To Connect or You Have Reached The 200 Request Quota! Max 200/HR [!]")
            pass
    except IndexError:
        print("\n[!] Failed To Find TXT Records [!]")
        print("\nDNS Lookup Complete!")
        pass
    except IndexError:
        print("\n[!] Failed To Find TXT Records [!]")
        print("\nDNS Lookup Complete!")
        pass
    except KeyError:
        print("\n[!] Failed To Find TXT Records [!]")
        print("\nDNS Lookup Complete!")
        pass


def start():
    global domain, api
    domain = input("[?] Please Enter The Domain You'd Like To Lookup: ")
    api = "https://dns-api.org/"
    print("\nChecking For A Records")
    print("----------------------\n")
    A_Records()
