def run():
    import os
    print("Place Images In images/")
    image = input("Enter Image Name: ")
    os.system("exiftool images/%s" % image)