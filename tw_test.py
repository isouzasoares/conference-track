# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # inputs
    print "Digite os itens, para salvar aperte ctrl + d:"
    talks = []
    for talk in sys.stdin.read().split("\n"):
        if talk:
            talks.append(talk)
