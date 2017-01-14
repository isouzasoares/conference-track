# -*- coding: utf-8 -*-
import sys

from talk import Talk


if __name__ == '__main__':
    # inputs
    print "Digite os itens, para salvar aperte ctrl + d:"
    items = []
    for item in sys.stdin.read().split("\n"):
        if item:
            items.append(item)
    Talk(items)
