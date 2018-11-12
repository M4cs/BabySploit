def checkupdate():
    with open("version", "r") as fwv:
        data = fwv.read()
        print(data)

checkupdate()