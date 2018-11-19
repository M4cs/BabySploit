def run():
    import requests, json

    api = 'http://ip-api.com/json/'
    ip = input("\n[?] Enter IP or Domain To Lookup: ")
    print("[!] Sending Request... [!]")
    request = requests.get(api + ip).text
    response = json.loads(request)
    status = response['status']
    if status == "success":
        print("Request Successful Displaying Response:\n")
    else:
        print("[!] The Request Failed. Try again with a different IP or check your internet connection. [!]")
        exit()
    country = response['country']
    regionName = response['regionName']
    city = response['city']
    zipcode = response['zip']
    timezone = response['timezone']
    ip = response['query']
    isp = response['isp']
    print("Location: " + city + ", " + regionName + " " + country + " " + zipcode)
    print("IP: " + ip)
    print("ISP: " + isp + "\n")
    print("\nScan Complete. SneakyBoy..")