from os import listdir, getcwd
from os.path import *


def listdirectory(location):
    contents = listdir(location)
    for name in contents:
        child = join(location, name)
        if isdir(child):
            print("dir: %s/%s" % (location, name))
            # location += name
            listdirectory(child)
        elif isfile(child):
            print(" >>> file:", child)
        else:
            print("             >>>", child)


def main():
    location = input("Enter the directory name or C for current dir:")
    if location == "C":
        location = getcwd()
        print("cwd >> ", location)
    listdirectory(location)


main()
