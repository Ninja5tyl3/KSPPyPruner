#!/usr/bin/python3

import argparse
import os
import sys
from urllib.request import Request
import requests

__author__ = 'jacob'


class Core:

    def __init__(self):
        self.prunelists = 'PruneLists/'
        self.partfolder = 'GameDev/'

    @staticmethod
    def prune(partlist):
        for part in partlist:
            base = os.path.splitext(part)[0]
            os.rename(part, base + ".pruned")

    @staticmethod
    def unprune(partlist):
        for part in partlist:
            base = os.path.splitext(part)[0]
            os.rename(part, base + ".cfg")

    def pruneall(self):
        files = self.getallfiles()
        for file in files:
            self.prune(file)

    def unpruneall(self):
        files = self.getallfiles()
        for file in files:
            self.unprune(file)

    @staticmethod
    def filetolist(infile):
        with open(infile) as f:
            lines = f.read().splitlines()
        return lines

    def getallfiles(self):
        for root, dirs, files in os.walk(self.prunelists):
            for file in files:
                if file.endswith(".prnl"):
                    # print(os.path.join(root, file))
                    flist = os.path.join(root, file)
                    return flist

    def runprune(self, prunelist):
        self.prune(prunelist)

    def rununprune(self, unprunelist):
        self.unprune(unprunelist)

    def runpruneall(self):
        self.pruneall()

    def rununpruneall(self):
        self.unpruneall()

    def runlist(self):
        return self.getallfiles()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-prune', action='store_true')
    parser.add_argument('-unprune', action='store_true')
    parser.add_argument('-pruneall', action='store_true')
    parser.add_argument('-unpruneall', acton='store_true')
    parser.add_argument('-list', action='store_true')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    core = Core()

    if args.prune:
        core.runprune(args.args)
    elif args.unprune:
        core.rununprune(args.args)
    elif args.pruneall:
        core.runpruneall()
    elif args.unpruneall:
        core.rununpruneall()
    elif args.list:
        core.runlist()
    else:
        print('No arguments supplied')
