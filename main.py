# -*- coding: utf-8 -*-
import sys

from talk import Talk


if __name__ == '__main__':
    # inputs
    print("Digite os itens, um por linha. Para salvar aperte ctrl + d:")
    items = []
    for item in sys.stdin.read().split("\n"):
        if item:
            items.append(item)
    Talk(items).output()
