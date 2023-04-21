from os import listdir, getcwd
from os.path import *


def listdirectory(location):
    contents = listdir(location)
    for name in contents:
        if isdir(name):
            print("dir: %s/%s" % (location, name))
            location += name
            listdirectory(location)
        elif isfile(name):
            print("file:", name)
        else:
            print("             >>>", name)


def main():
    location = input("Enter the directory name or C for current dir:")
    if location == "C":
        location = getcwd()
        print("cwd >> ", location)
    listdirectory(location)


main()
