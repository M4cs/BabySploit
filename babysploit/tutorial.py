def run():
    from pyfiglet import Figlet
    f = Figlet(style='slant')
    f.renderText("Tutorial")
    start = """
Welcome to the BabySploit Tutorial

In this tutorial you will learn how to navigate and use
BabySploit. The framework is geared towards beginners so
it shouldn't be too hard to get the hang of things.
    """
    input("Press Enter To Continue...")

def animated(msg):
    import sys, time
    for char in msg:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()