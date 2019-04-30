import json

import requests


def run():
    api = 'http://ip-api.com/json/'
    ip = input("\n[?] Enter IP or Domain To Lookup: ")
    print("[!] Sending Request... [!]")
    response_text = requests.get(api + ip).text
    response_json = json.loads(response_text)

    if response_json.get('status') == "success":
        print("Request Successful Displaying Response:\n")
    else:
        print("[!] The Request Failed. Try again with a different IP "
              "or check your internet connection. [!]")
        exit(1)

    print("Location: {city}, {regionName} {country} {zip}".format(**response_json))
    print("IP: {query}".format(**response_json))
    print("ISP: {isp}\n".format(**response_json))
    print("\nScan Complete. SneakyBoy..")