#!/usr/bin/python3
def star_arrow(width):
    for row in range(width):
        print(row*"*"+"\n")
    for row in range(width, 0, -1):
        print(row*"*"+"\n")

star_arrow(3)