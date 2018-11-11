def run():
    import requests, json

    api = "https://censys.io/api/v1"
    creds = {
        "UID" : "",
        "SECRET" : ""
        }
    if creds['UID'] and creds['SECRET'] == "":
        print("Please add credentials to the plugin. Location: babysploit/censyslookup")
        exit()
    else:
        pass
    #UID = "9f4dd0df-9499-4e93-9d1a-2a3274739990"
    #SECRET = "OHDmWb5C31oyKunUMn49P0JMVY5S2QbK"
    res = requests.get(api+"/search/syndicated+intel", auth=(creds['UID'], creds['SECRET'])).text
    r = json.loads(res)
    print(r)

