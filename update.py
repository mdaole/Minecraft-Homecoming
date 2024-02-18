#!/usr/bin/python3

from os import system, chdir, path
from subprocess import Popen
from threading import Thread
from psutil import process_iter

def main():
    chdir(path.dirname(path.realpath(__file__)))
    system("git checkout HEAD -- index.toml pack.toml")
    if (system("git pull -q")!=0): 
        system("git stash")
        system("git pull")
        system("git stash pop")
        print("Merge conflict. Review in vscode.")
        exit(1)
    Popen(["packwiz", "serve"])

    chdir(path.join("..", ".minecraft"))
    system("java -jar packwiz-installer-bootstrap.jar ../packwiz/pack.toml")

    for i in process_iter():
        if "packwiz" in i.name(): i.kill()

if __name__=="__main__": main()