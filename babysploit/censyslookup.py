def run():
    import requests, json

    api = "https://censys.io/api/v1"
    creds = {
        "UID": "",
        "SECRET": ""
        }
    if creds['UID'] and creds['SECRET'] == "":
        print("Please add credentials to the plugin. Location: babysploit/censyslookup")
        exit()
    else:
        pass
    res = requests.get(api+"/search/", auth=(creds['UID'], creds['SECRET'])).text
    r = json.loads(res)
    

