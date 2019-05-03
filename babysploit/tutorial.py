import os
import sys
import time

from pyfiglet import Figlet


def run():
    f = Figlet(font='slant')
    f.renderText("Tutorial")
    start = """
Welcome to the BabySploit Tutorial

In this tutorial you will learn how to navigate and use
BabySploit. The framework is geared towards beginners so
it shouldn't be too hard to get the hang of things.
    """
    animated(start)
    input("Press Enter To Continue...")
    os.system("clear")
    second = """
What is BabySploit?

BabySploit is a penetration testing/social engineering
framework aimed towards beginners in the field. Any person,
with any amount of experience may find use out of BabySploit.
The framework comes equipped with different types of tools
use for Information Gathering, Cryptology, Exploitation, and more.

BabySploit is actively being developed and will constantly be
gaining more and more tools. I plan to spread the framework out
to more subcategories of tools and creating an extremely large
tool box that will be able to do a multitude of things but very
easily for the end user. That is the main goal of BabySploit
    """
    animated(second)
    input("Press Enter To Continue...")


def animated(msg):
    for char in msg:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
